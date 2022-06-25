import math

from PyQt5 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc, QtPrintSupport as qtps
from ui.raporlarUI import Ui_MainWindow
from messageBox import msg
import datetime
from database import db

class ReportsPage(qtw.QMainWindow):
    dpi = 72 *2
    doc_width = int(8.5 * dpi)
    doc_height = int(11 * dpi)

    def __init__(self):
        super(ReportsPage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            self.kurumAdi    = db.getData("OkulBilgiTablosu", "*")[0][2]
        except Exception as E:
            print("Kurum bilgileri bulunamıyor")
            self.kurumAdi = "Kurum bilgileri bulunamıyor"

        self.doc = MakeDocument()

        self.ui.btn_due.clicked.connect(self.handlePreviewDue)
        self.ui.btn_printAllBarkodes.clicked.connect(self.handlePreviewBarkodes)
        self.ui.btn_printQueuedUpBarkodes.clicked.connect(self.handlePreviewBarkodes)
        self.ui.btn_printMemberList.clicked.connect(self.handlePreviewMemberList)

    def handlePreviewBookList(self):
        try:
            data        = db.getMemberDataForReport()
            headings = ("Barkod", "Kitap Adı", "Yazarı", )
            document    = self.doc.makeDocumentList(
                data            = data,
                kurumAdi        = self.kurumAdi,
                title           = "Kütüphane Kitap Listesi",
                headings        = headings,
                alignCenterCols = (0,1,4,5,6,7)     )
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreviewBookList   \t\t{E}")

    def handlePreviewMemberList(self):
        try:
            data        = db.getMemberDataForReport()
            headings = ('Üye No','Okul No',"Ad","Soyad",'Sınıf','Şube', "Doğum Tarihi", "Üyelik Tarihi")
            document    = self.doc.makeDocumentList(
                data            = data,
                kurumAdi        = self.kurumAdi,
                title           = "Aktif Üye Listesi",
                headings        = headings,
                alignCenterCols = (0,1,4,5,6,7)     )
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreviewMemberList   \t\t{E}")

    def handlePreviewDue(self):
        try:
            data        = db.getEscrowBooksReturnToday_orderBySinif()
            headings = ('Barkod',"Eser Adı","Yazarı","Alma Tarihi","Süre","İade Tarihi",'Üye No','Okul No',"Ad","Soyad",'Sınıf','Şube')
            document = self.doc.makeDocumentList(
                data            = data,
                kurumAdi        = self.kurumAdi,
                title           = "İade Zamanı Gelen/Geçen Eserler",
                headings        = headings,
                alignCenterCols = (0,3,4,5,6,7,10,11)       )
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreviewDue   \t\t{E}")

    def handlePreviewBarkodes(self):
        secenekler = {"Tüm Barkodlar":0, "Kuyruktaki Barkodlar":1}
        secim = secenekler[self.sender().text()]
        try:
            data        = db.getBookDataForPrintBarkode(secim)               # data [Kitap Adı, Section, Raf, ImgData]
            document    = self.doc.makeDocumentBarkode( datas=data )
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            result = dialog.exec_()
            if result:
                sonuc,_ = msg.MesajBox("Dikkat", "Barkodları başarı ile yazdırdıysanız kuyruk temizlensin mi?")
                print(sonuc)
                if sonuc:
                    db.updateState("KitapTablosu", BarkodPrint=(0,), kitapId=tuple(i[0] for i in data))
        except Exception as E:
            print(f"Fonk: handlePreviewBarkodes   \t\t{E}")




class MakeDocument:
    dpi = 72 *2
    doc_width = int(8.5 * dpi)
    doc_height = int(11 * dpi)

    def imgDataToQImageObj(self, imgData) -> qtg.QImage :
        image = qtg.QImage()
        image.loadFromData(imgData)
        return image.scaledToWidth(200)

    def makeDocumentBarkode(self, datas):
        try:
            document = qtg.QTextDocument()
            document.setDocumentMargin(20)
            document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
            cursor = qtg.QTextCursor(document)
            root = document.rootFrame()

            block_fmt = qtg.QTextBlockFormat()
            block_fmt.setTopMargin(10)
            block_fmt.setBackground(qtc.Qt.red)

            std_format = qtg.QTextCharFormat()
            std_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Normal))
            std_format.setVerticalAlignment(qtg.QTextCharFormat.AlignTop)

            page_frame_fmt = qtg.QTextFrameFormat()
            size = root.document().pageSize()
            page_frame_fmt.setWidth(size.width()-50)
            page_frame_fmt.setHeight(size.height()-80)

            img_frame_fmt = qtg.QTextFrameFormat()
            img_frame_fmt.setBorder(2)
            img_frame_fmt.setMargin(10)
            img_frame_fmt.setWidth(200)
            img_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)

            table_format = qtg.QTextTableFormat()
            table_format.setAlignment(qtc.Qt.AlignHCenter)
            table_format.setWidth(qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))
            table_format.setCellPadding(5)
            cols_lenght = [qtg.QTextLength(qtg.QTextLength.PercentageLength, 20)]*5
            table_format.setColumnWidthConstraints( cols_lenght )               # Burda tablo sütun genişliklerini eşit olarak ayarlıyoruz %20

            page_count = math.ceil(len(datas)/40)               # baskının kaç sayfa olacağını belirliyoruz
            for page in range(page_count):
                if page_count-page == 1:
                    data_40 = datas[page*40:]                   # son sayfa ise gerektiği kadar
                else:
                    data_40 = datas[page*40:(page+1)*40]
                row = math.ceil(len(data_40)/5)
                page_frame = cursor.insertFrame(page_frame_fmt)
                cursor.setPosition(page_frame.lastPosition())
                table = cursor.insertTable(row, 5, table_format)

                for i in range(len(data_40)):
                    cursor.insertText(f" {data_40[i][1]:<200}", std_format)
                    cursor.insertBlock()
                    cursor.insertText(f" Bölüm :  {data_40[i][2] if datas[i][2] else '':<200}", std_format)
                    cursor.insertBlock()
                    cursor.insertText(f" Raf No:  {data_40[i][3] if datas[i][3] else '':<200}", std_format)
                    image = self.imgDataToQImageObj(imgData=datas[i][4])
                    cursor.insertImage(image)
                    cursor.movePosition(qtg.QTextCursor.NextCell)
                cursor.setPosition(root.lastPosition())
            return document
        except Exception as E:
            print(f"Fonk: makeDocumentBarkode  \t\t{E}")

    def makeDocumentList(self, data:list[list], kurumAdi:str ="NFO", title:str ="", headings:tuple[str] = tuple(), alignCenterCols:tuple= ()):
        try:
            document = qtg.QTextDocument()
            document.setDocumentMargin(20)
            document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
            cursor = qtg.QTextCursor(document)
            root = document.rootFrame()

            cursor.setPosition(root.lastPosition())

            # Insert top level frames
            logo_frame_fmt = qtg.QTextFrameFormat()
            logo_frame_fmt.setBorder(2)
            logo_frame_fmt.setPadding(5)
            logo_frame_fmt.setTopMargin(-30)
            logo_frame = cursor.insertFrame(logo_frame_fmt)

            cursor.setPosition(root.lastPosition())
            title_frame_fmt = qtg.QTextFrameFormat()
            title_frame_fmt.setTopMargin(20)
            title_frame_fmt.setBottomMargin(20)
            title_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
            title_frame_fmt.setBackground(qtg.QColor("#f0f5f1"))
            title_frame =  cursor.insertFrame(title_frame_fmt)

            cursor.setPosition(root.lastPosition())
            table_frame_fmt = qtg.QTextFrameFormat()
            table_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
            table_frame = cursor.insertFrame(table_frame_fmt)

            # Create the heading
            # create a format for the characters
            std_format = qtg.QTextCharFormat()
            std_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Normal))

            logo_text_format = qtg.QTextCharFormat()
            logo_text_format.setFont(qtg.QFont('Arial', 18, 20, qtg.QFont.DemiBold))

            label_format = qtg.QTextCharFormat()
            label_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Bold))

            # cursor.setPosition(title_frame.lastPosition())
            block_format = qtg.QTextBlockFormat()
            block_format.setLineHeight(100, qtg.QTextBlockFormat.ProportionalHeight)
            block_format.setAlignment(qtc.Qt.AlignCenter)          # texti blok içinde hizalama

            logotext_block_fmt = qtg.QTextBlockFormat()
            logotext_block_fmt.setTopMargin(15)
            logotext_block_fmt.setLineHeight(100, qtg.QTextBlockFormat.ProportionalHeight)
            logotext_block_fmt.setAlignment(qtc.Qt.AlignCenter)


            # create a format for the block
            cursor.setPosition(logo_frame.firstPosition())

            # The easy way
            # cursor.insertImage('logo.png')
            # Better way
            logo_image_fmt = qtg.QTextImageFormat()
            logo_image_fmt.setName("img/logo.jpg")
            logo_image_fmt.setHeight(64)
            logo_image_fmt.setWidth(72)
            cursor.insertImage(logo_image_fmt, qtg.QTextFrameFormat.FloatRight)
            cursor.insertBlock(logotext_block_fmt)
            cursor.insertText(kurumAdi, logo_text_format)

            cursor.setPosition(root.firstPosition())
            cursor.insertBlock()
            cursor.insertText(f"   {datetime.date.today().strftime('%d %b %Y')}", std_format)

            cursor.setPosition(title_frame.firstPosition())
            cursor.insertBlock(block_format)
            cursor.insertText(title, label_format)
            cursor.insertHtml('<html> <body> <hr style="height:5px;border-width:3px;color:green;"></body> </html>')

            # line items
            table_format = qtg.QTextTableFormat()
            table_format.setHeaderRowCount(1)
            table_format.setAlignment(qtc.Qt.AlignHCenter)
            table_format.setCellPadding(2)
            # table_format.setCellSpacing(0)
            table_format.setWidth( qtg.QTextLength( qtg.QTextLength.PercentageLength, 100))             # Tablo sütun genişliği

            num_rows = len(data)+1
            num_cols = len(headings)
            # cursor.insertBlock()
            cursor.setPosition(table_frame.firstPosition())
            table = cursor.insertTable(num_rows, num_cols, table_format)
            # now we are in the first cell of the table
            # write headers
            for heading in headings:
                cursor.insertBlock(block_format)
                cursor.insertText(heading, label_format)
                cursor.movePosition(qtg.QTextCursor.NextCell)

            # write data in table
            for row in data:
                for col, value in enumerate(row):
                    if col in alignCenterCols:
                        block_format.setAlignment(qtc.Qt.AlignCenter)
                        block_format.setLeftMargin(0)
                    else:
                        block_format.setLeftMargin(5)
                        block_format.setAlignment(qtc.Qt.AlignLeft)
                    cursor.insertBlock(block_format)
                    cursor.insertText(str(value), std_format)
                    cursor.movePosition(qtg.QTextCursor.NextCell)
            return document
        except Exception as E:
            print(f"Fonk: makeDocumentList   \t\t{E}")


