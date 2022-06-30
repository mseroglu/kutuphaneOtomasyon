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
            self.kurumAdi = "Kurum bilgileri bulunamıyor"

        self.doc = MakeDocument()

        self.ui.btn_due.clicked.connect(self.handlePreviewDue)
        self.ui.btn_printAllBarkodes.clicked.connect(self.handlePreviewBarkodes)
        self.ui.btn_printQueuedUpBarkodes.clicked.connect(self.handlePreviewBarkodes)
        self.ui.btn_printMemberList.clicked.connect(self.handlePreviewMemberList)
        self.ui.btn_printBookList_sortBarkodNumber.clicked.connect(self.handlePreviewBookList)
        self.ui.btn_printBookList_sortBookName.clicked.connect(self.handlePreviewBookList)

    def handlePreviewBookList(self):
        secenekler = {"btn_printBookList_sortBarkodNumber":0,  "btn_printBookList_sortBookName":1}
        tercih = secenekler[self.sender().objectName()]

        try:
            data        = db.getBooksForReport(tercih= tercih)
            headings = ("Barkod", "Kitap Adı", "Yazarı", "Kategori", "Raf No")
            # document    = self.doc.makeDocumentList(
            #     data            = data,
            #     kurumAdi        = self.kurumAdi,
            #     title           = "Kütüphane Kitap Listesi",
            #     headings        = headings,
            #     alignCenterCols = (0,)     )
            document = self.doc.makeDocumentListWithoutHeader(data=data, headings=headings, alignCenterCols=(0,))
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreviewBookList   \t\t{E}")

    def handlePreviewMemberList(self):
        try:
            data        = db.getMemberDataForReport()
            headings = ('Üye No','Okul No',"Ad","Soyad",'Sınıf','Şube', "Doğum Tarihi", "Üyelik Tarihi")
            # document    = self.doc.makeDocumentList(
            #     data            = data,
            #     kurumAdi        = self.kurumAdi,
            #     title           = "Aktif Üye Listesi",
            #     headings        = headings,
            #     alignCenterCols = (0,1,4,5,6,7)     )
            document    = self.doc.makeDocumentListWithoutHeader(data=data, headings=headings, alignCenterCols=(0,1,4,5,6,7))
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreviewMemberList   \t\t{E}")

    def handlePreviewDue(self):
        try:
            data        = db.getEscrowBooksReturnToday_orderBySinif()
            headings = ('Barkod',"Eser Adı","Yazarı","Alma Tarihi","Süre","İade Tarihi",'Üye No','Okul No',"Ad","Soyad",'Sınıf','Şube')
            #document = self.doc.makeDocumentList(
                # data            = data,
                # kurumAdi        = self.kurumAdi,
                # title           = "İade Zamanı Gelen/Geçen Eserler",
                # headings        = headings,
                # alignCenterCols = (0,3,4,5,6,7,10,11)       )
            document = self.doc.makeDocumentListWithoutHeader(data=data, headings=headings, alignCenterCols=(0,3,4,5,6,7,10,11))
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
                if sonuc:
                    db.updateState("KitapTablosu", BarkodPrint=(0,), kitapId=tuple(i[0] for i in data))
        except Exception as E:
            print(f"Fonk: handlePreviewBarkodes   \t\t{E}")

    def handlePreviewMemberCards(self):
        secenekler = {"Tüm Barkodlar":0, "Kuyruktaki Barkodlar":1}
        secim = secenekler[self.sender().text()]
        try:
            data        = db.getBookDataForPrintBarkode(secim)               # data [Kitap Adı, Section, Raf, ImgData]
            document    = self.doc.makeDocumentMemberCards( datas=data )
            dialog      = qtps.QPrintPreviewDialog()
            dialog.paintRequested.connect( document.print_ )
            result = dialog.exec_()
            if result:
                sonuc,_ = msg.MesajBox("Dikkat", "Üye kartlarını başarı ile yazdırdıysanız kuyruk temizlensin mi?")
                if sonuc:
                    db.updateState("UyeTablosu", UyeKartiPrint=(0,), TCNo=tuple(i[0] for i in data))
        except Exception as E:
            print(f"Fonk: handlePreviewMemberCards   \t\t{E}")




class MakeDocument:
    doc_width   = 1240                          # A4 150 DPI ölçüleri
    doc_height  = 1754
    def createDocument(self):
        self.document = qtg.QTextDocument()
        self.document.setDocumentMargin(0)
        self.document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
        self.cursor = qtg.QTextCursor(self.document)
        self.root = self.document.rootFrame()
        self.cursor.setPosition(self.root.lastPosition())

    def imgDataToQImageObj(self, imgData) -> qtg.QImage :
        image = qtg.QImage()
        image.loadFromData(imgData)
        return image.scaledToWidth(200)

    def makeDocumentMemberCards(self, datas):
        try:
            self.createDocument()

            block_fmt = qtg.QTextBlockFormat()
            block_fmt.setTopMargin(0)
            block_fmt.setBackground(qtc.Qt.red)

            std_format = qtg.QTextCharFormat()
            std_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Normal))
            std_format.setVerticalAlignment(qtg.QTextCharFormat.AlignTop)

            page_frame_fmt = qtg.QTextFrameFormat()
            page_frame_fmt.setWidth(self.doc_width-20)
            page_frame_fmt.setHeight(self.doc_height-40)
            page_frame_fmt.setBottomMargin(20)
            # page_frame_fmt.setBackground(qtc.Qt.red)

            img_frame_fmt = qtg.QTextFrameFormat()
            img_frame_fmt.setBorder(2)
            img_frame_fmt.setMargin(10)
            img_frame_fmt.setWidth(200)
            img_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)

            table_format = qtg.QTextTableFormat()
            table_format.setAlignment(qtc.Qt.AlignHCenter)
            table_format.setWidth(qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))
            table_format.setCellPadding(5)
            table_format.setCellSpacing(10)
            cols_lenght = [qtg.QTextLength(qtg.QTextLength.PercentageLength, 20)]*5
            table_format.setColumnWidthConstraints( cols_lenght )               # Burda tablo sütun genişliklerini eşit olarak ayarlıyoruz %20

            page_count = math.ceil(len(datas)/40)                   # baskının kaç sayfa olacağını belirliyoruz
            for page in range(page_count):
                if page_count-page == 1:
                    data_40 = datas[page*40:]                       # son sayfa ise 40 değil, gerektiği kadar kutu çizsin
                else:
                    data_40 = datas[page*40:(page+1)*40]            # her sayfanın verisini data_40 a atıp parça parça veriyoruz
                row = math.ceil(len(data_40)/5)                     # satır sayısını yukarı yuvarlayarak buluyoruz
                page_frame = self.cursor.insertFrame(page_frame_fmt)
                self.cursor.setPosition(page_frame.lastPosition())
                table = self.cursor.insertTable(row, 5, table_format)

                for i in range(len(data_40)):
                    self.cursor.insertText(f"{data_40[i][1][:25]:<100}", std_format)
                    self.cursor.insertBlock()
                    self.cursor.insertText(f"Bölüm  :  {data_40[i][2][:16] if datas[i][2] else '':<100}", std_format)
                    self.cursor.insertBlock()
                    self.cursor.insertText(f"Raf No :  {data_40[i][3][:16] if datas[i][3] else '':<100}", std_format)
                    image = self.imgDataToQImageObj(imgData=data_40[i][4])
                    self.cursor.insertImage(image)
                    self.cursor.movePosition(qtg.QTextCursor.NextCell)
                self.cursor.setPosition(self.root.lastPosition())
            return self.document
        except Exception as E:
            print(f"Fonk: makeDocumentMemberCards  \t\t{E}")

    def makeDocumentBarkode(self, datas):
        try:
            self.createDocument()

            block_fmt = qtg.QTextBlockFormat()
            block_fmt.setTopMargin(0)
            block_fmt.setBackground(qtc.Qt.red)

            std_format = qtg.QTextCharFormat()
            std_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Normal))
            std_format.setVerticalAlignment(qtg.QTextCharFormat.AlignTop)

            page_frame_fmt = qtg.QTextFrameFormat()
            page_frame_fmt.setWidth(self.doc_width-20)
            page_frame_fmt.setHeight(self.doc_height-40)
            page_frame_fmt.setBottomMargin(20)
            page_frame_fmt.setTopMargin(30)
            # page_frame_fmt.setBackground(qtc.Qt.red)

            img_frame_fmt = qtg.QTextFrameFormat()
            img_frame_fmt.setBorder(2)
            img_frame_fmt.setMargin(10)
            img_frame_fmt.setWidth(200)
            img_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)

            table_format = qtg.QTextTableFormat()
            table_format.setAlignment(qtc.Qt.AlignHCenter)
            table_format.setWidth(qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))
            table_format.setCellPadding(5)
            table_format.setCellSpacing(10)
            cols_lenght = [qtg.QTextLength(qtg.QTextLength.PercentageLength, 20)]*5
            table_format.setColumnWidthConstraints( cols_lenght )               # Burda tablo sütun genişliklerini eşit olarak ayarlıyoruz %20

            page_count = math.ceil(len(datas)/40)                   # baskının kaç sayfa olacağını belirliyoruz
            for page in range(page_count):
                if page_count-page == 1:
                    data_40 = datas[page*40:]                       # son sayfa ise 40 değil, gerektiği kadar kutu çizsin
                else:
                    data_40 = datas[page*40:(page+1)*40]            # her sayfanın verisini data_40 a atıp parça parça veriyoruz
                row = math.ceil(len(data_40)/5)                     # satır sayısını yukarı yuvarlayarak buluyoruz
                page_frame = self.cursor.insertFrame(page_frame_fmt)
                self.cursor.setPosition(page_frame.lastPosition())
                table = self.cursor.insertTable(row, 5, table_format)

                for i in range(len(data_40)):
                    self.cursor.insertText(f"{data_40[i][1][:25]:<100}", std_format)
                    self.cursor.insertBlock()
                    self.cursor.insertText(f"Bölüm  :  {data_40[i][2][:16] if datas[i][2] else '':<100}", std_format)
                    self.cursor.insertBlock()
                    self.cursor.insertText(f"Raf No :  {data_40[i][3][:16] if datas[i][3] else '':<100}", std_format)
                    image = self.imgDataToQImageObj(imgData=data_40[i][4])
                    self.cursor.insertImage(image)
                    self.cursor.movePosition(qtg.QTextCursor.NextCell)
                self.cursor.setPosition(self.root.lastPosition())
            return self.document
        except Exception as E:
            print(f"Fonk: makeDocumentBarkode  \t\t{E}")

    def makeDocumentList(self, data:list[list], kurumAdi:str ="NFO", title:str ="", headings:tuple[str] = tuple(), alignCenterCols:tuple= ()):
        try:
            self.createDocument()
            # Insert top level frames
            logo_frame_fmt = qtg.QTextFrameFormat()
            logo_frame_fmt.setBorder(2)
            logo_frame_fmt.setPadding(5)
            logo_frame_fmt.setTopMargin(-30)

            logo_frame = self.cursor.insertFrame(logo_frame_fmt)

            self.cursor.setPosition(self.root.lastPosition())
            title_frame_fmt = qtg.QTextFrameFormat()
            title_frame_fmt.setTopMargin(10)
            title_frame_fmt.setBottomMargin(20)
            title_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
            title_frame_fmt.setBackground(qtg.QColor("#f0f5f1"))
            title_frame =  self.cursor.insertFrame(title_frame_fmt)

            self.cursor.setPosition(self.root.lastPosition())
            table_frame_fmt = qtg.QTextFrameFormat()
            table_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
            table_frame = self.cursor.insertFrame(table_frame_fmt)

            std_format = qtg.QTextCharFormat()
            std_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Normal))

            logo_text_format = qtg.QTextCharFormat()
            logo_text_format.setFont(qtg.QFont('Arial', 18, 20, qtg.QFont.DemiBold))

            label_format = qtg.QTextCharFormat()
            label_format.setFont(qtg.QFont("Sans", 10, qtg.QFont.Bold))

            # cursor.setPosition(title_frame.lastPosition())
            block_format = qtg.QTextBlockFormat()
            block_format.setLineHeight(100, qtg.QTextBlockFormat.ProportionalHeight)
            block_format.setAlignment(qtc.Qt.AlignCenter)          # texti blok içinde hizalama

            logotext_block_fmt = qtg.QTextBlockFormat()
            logotext_block_fmt.setTopMargin(15)
            logotext_block_fmt.setLineHeight(100, qtg.QTextBlockFormat.ProportionalHeight)
            logotext_block_fmt.setAlignment(qtc.Qt.AlignCenter)

            # create a format for the block
            self.cursor.setPosition(logo_frame.firstPosition())

            # The easy way
            # cursor.insertImage('img/logo.png')
            # Better way
            logo_image_fmt = qtg.QTextImageFormat()
            logo_image_fmt.setName("img/logo.jpg")
            logo_image_fmt.setHeight(64)
            logo_image_fmt.setWidth(72)
            self.cursor.insertImage(logo_image_fmt, qtg.QTextFrameFormat.FloatRight)
            self.cursor.insertBlock(logotext_block_fmt)
            self.cursor.insertText(kurumAdi, logo_text_format)

            self.cursor.setPosition(self.root.firstPosition())
            self.cursor.insertBlock()
            self.cursor.insertText(f"   {datetime.date.today().strftime('%d %b %Y')}", std_format)

            self.cursor.setPosition(title_frame.firstPosition())
            self.cursor.insertBlock(block_format)
            self.cursor.insertText(title, label_format)
            self.cursor.insertHtml('<html> <body> <hr style="height:5px;border-width:3px;color:green;"></body> </html>')

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
            self.cursor.setPosition(table_frame.firstPosition())
            table = self.cursor.insertTable(num_rows, num_cols, table_format)
            # now we are in the first cell of the table
            # write headers
            for heading in headings:
                self.cursor.insertBlock(block_format)
                self.cursor.insertText(heading, label_format)
                self.cursor.movePosition(qtg.QTextCursor.NextCell)

            # write data in table
            for row in data:
                for col, value in enumerate(row):
                    if col in alignCenterCols:
                        block_format.setAlignment(qtc.Qt.AlignCenter)
                        block_format.setLeftMargin(0)
                    else:
                        block_format.setLeftMargin(5)
                        block_format.setAlignment(qtc.Qt.AlignLeft)
                    self.cursor.insertBlock(block_format)
                    self.cursor.insertText(str(value) if value else "", std_format)
                    self.cursor.movePosition(qtg.QTextCursor.NextCell)
            return self.document
        except Exception as E:
            print(f"Fonk: makeDocumentList   \t\t{E}")

    def makeDocumentListWithoutHeader(self, data:list[list], headings:tuple[str], alignCenterCols:tuple[int]):
        try:
            self.createDocument()
            table_frame_fmt = qtg.QTextFrameFormat()
            table_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
            table_frame = self.cursor.insertFrame(table_frame_fmt)

            std_format = qtg.QTextCharFormat()
            std_format.setFont(qtg.QFont("Sans", 9, qtg.QFont.Normal))

            label_format = qtg.QTextCharFormat()
            label_format.setFont(qtg.QFont("Sans", 10, qtg.QFont.Bold))

            # cursor.setPosition(title_frame.lastPosition())
            block_format = qtg.QTextBlockFormat()
            block_format.setLineHeight(100, qtg.QTextBlockFormat.ProportionalHeight)
            block_format.setAlignment(qtc.Qt.AlignCenter)          # texti blok içinde hizalama

            # line items
            table_format = qtg.QTextTableFormat()
            table_format.setHeaderRowCount(1)
            table_format.setBorderStyle(qtg.QTextFrameFormat.BorderStyle_Inset)
            table_format.setAlignment(qtc.Qt.AlignHCenter)
            table_format.setCellPadding(2)
            table_format.setWidth(self.doc_width-50)
            table_format.setBottomMargin(50)
            # table_format.setHeight(self.doc_height-100)
            table_format.setWidth( qtg.QTextLength( qtg.QTextLength.PercentageLength, 95))             # Tablo sütun genişliği

            num_rows = len(data)+1
            num_cols = len(headings)
            self.cursor.setPosition(table_frame.firstPosition())
            table = self.cursor.insertTable(num_rows, num_cols, table_format)

            for heading in headings:
                self.cursor.insertBlock(block_format)
                self.cursor.insertText(heading, label_format)
                self.cursor.movePosition(qtg.QTextCursor.NextCell)

            # write data in table
            for row in data:
                for col, value in enumerate(row):
                    if col in alignCenterCols:
                        block_format.setAlignment(qtc.Qt.AlignCenter)
                        block_format.setLeftMargin(0)
                    else:
                        block_format.setLeftMargin(5)
                        block_format.setAlignment(qtc.Qt.AlignLeft)
                    self.cursor.insertBlock(block_format)
                    self.cursor.insertText(str(value) if value else "", std_format)
                    self.cursor.movePosition(qtg.QTextCursor.NextCell)
            return self.document
        except Exception as E:
            print(f"Fonk: makeDocumentListWithoutHeader   \t\t{E}")


