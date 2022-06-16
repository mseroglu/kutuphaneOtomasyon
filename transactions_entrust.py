from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "")

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHBoxLayout, QWidget, QCheckBox, QPushButton
from PyQt5 import QtGui, QtCore
from ui.emanetVermeUI import Ui_MainWindow
from database import db, curs, tableWidgetResize
from messageBox import msg
from ui.confirmationUI import Ui_Form


class ConfirmationUI(QWidget):
    def __init__(self):
        super(ConfirmationUI, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag( QtCore.Qt.WindowStaysOnTopHint )          # pencereyi en üstte tutar
        self.setStyleSheet("""QGroupBox{padding: 20px 10px 0px 10px; font: italic bold 12px; }
                    QGroupBox::title {                                       
                    border-top-right-radius: 15px;
                    border-top-left-radius: 15px;
                    subcontrol-origin: margin;
                    subcontrol-position: top center;
                    padding: 4px 40px 4px 40px;
                    background-color: green;
                    color: rgb(250, 250, 250)  }""")

        self.result = None
        self.ui.btn_ok.clicked.connect(self.returnResult)
        self.ui.btn_escape.clicked.connect(self.close)
        # self.ui.btn_escape.clicked.connect(Entrust().show())

    def returnResult(self):
        try:
            self.close()
            Entrust().giveBooksToMembers()
            Entrust().refreshTableWidgetItems()             # tablewidget ları yenile çalışmıyor
        except Exception as E:
            print(f"Fonk: returnResult      Hata: {E} ")

    def showConfirmationPage_B(self, memberData, booksData):
        try:
            labelBarkods = (self.ui.label_barkod1, self.ui.label_barkod2, self.ui.label_barkod3, self.ui.label_barkod4, self.ui.label_barkod5)
            labelBooks   = (self.ui.label_eserAdi1, self.ui.label_eserAdi2, self.ui.label_eserAdi3, self.ui.label_eserAdi4, self.ui.label_eserAdi5)
            groupBoxes   = (self.ui.groupBox_1, self.ui.groupBox_2, self.ui.groupBox_3, self.ui.groupBox_4, self.ui.groupBox_5)
            self.ui.label_name.setText(memberData[3]+" "+memberData[4])
            self.ui.label_tcno.setText(memberData[5])
            self.ui.label_schoolNumber.setText(memberData[2])
            self.ui.label_class.setText(str(memberData[6])+" / "+memberData[7])
            dataImg = db.getImageData(TableName="UyeTablosu", Col="Photo", uyeId= memberData[0])
            pixmap = QtGui.QPixmap("img/kitap-kurdu.jpg")
            if dataImg:
                pixmap.loadFromData(dataImg)
            self.ui.label_memberImg.setPixmap(pixmap)
            for i in range(5):                  # önce temizlik
                labelBarkods[i].setText("")
                labelBooks[i].setText("")
                groupBoxes[i].hide()

            i = 0
            for barkod, bookName in list(zip(booksData["Barkod"], booksData["KitapAdi"])):
                labelBarkods[i].setText(barkod)
                labelBooks[i].setText(bookName)
                groupBoxes[i].show()
                groupBoxes[i].setStyleSheet("QGroupBox {background-color: #d9ead3; border-radius:10px}")
                i += 1
            self.show()
        except Exception as E:
            print(f"Fonk: showConfirmationPage_B      Hata: {E} ")



class Entrust(QMainWindow):                         # Entrust = Emanet
    givenBookMemberId   = None
    selectedBooksDict   = {'KitapId': None, 'KitapAdi': None}
    dictBooksInfos      = {}
    dictMembersInfos    = {}
    selectedBarkodList  = []

    bookCheckboxObjectsForSelection = dict()

    def __init__(self):
        super(Entrust, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1000,600)

        self.winConfirmation = ConfirmationUI()

        self.numberOfBlankLines = 20
        self.duration           = 20_000


        self.refreshTableWidgetItems()
        self.ui.radio_isim.clicked.connect(self.filterMembersOnTablewidget)
        self.ui.radio_tc.clicked.connect(self.filterMembersOnTablewidget)
        self.ui.radio_okulNo.clicked.connect(self.filterMembersOnTablewidget)
        self.ui.le_searchMember.textChanged.connect(self.filterMembersOnTablewidget)
        self.ui.le_searchBook.textChanged.connect(self.filterBooksOnTablewidget)
        self.ui.le_searchBook.textChanged.connect(self.editBarkodNumberOnLineedit)
        self.ui.radio_barkod.clicked.connect(self.filterBooksOnTablewidget)
        self.ui.radio_isbn.clicked.connect(self.filterBooksOnTablewidget)
        self.ui.radio_kitapAdi.clicked.connect(self.filterBooksOnTablewidget)

        self.ui.btn_clearSelection.clicked.connect(self.clearSelection)

    def editBarkodNumberOnLineedit(self, text):
        try:
            if self.ui.radio_barkod.isChecked():
                sonEklenen = text.split()[-1]
                if len(sonEklenen) == 8 :
                    try:
                        Entrust.bookCheckboxObjectsForSelection[sonEklenen].click()
                        text += ", "
                        self.ui.le_searchBook.setText(text)
                    except Exception as E:
                        print("Bu kitap rafta bulunamadı")
                        msg.popup_mesaj("Barkod bulunamadı", "Okuttuğunuz barkoda ait kitap rafta bulunamadı. Olası sebepler:\n\n"
                                                             "   1- Üyedeki bir kitap barkodunu okuttunuz ise önce geri almalısınız.\t\n"
                                                             "   2- Ya da kayıtlı olmayan bir barkod okuttunuz.\n")
        except Exception as E:
            print(f"Fonk: editBarkodNumberOnLineedit    \tHata: {E}")


    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        tableWidgetResize(self.ui.table_membersList, (3, 2, 2, 6, 3, 4, 1, 1))
        tableWidgetResize(self.ui.table_booksList, (2, 3, 6, 4, 4))

    def refreshTableWidgetItems(self):
        self.showMembersInTablewidget()
        self.showBooksOnTablewidget()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.ui.le_searchBook.setFocus()
        self.setDateOnLabel()
        self.resizeEvent(QtGui.QResizeEvent)
        self.ui.btn_clearSelection.click()          # bu da iş yapmıyor

    def returnDateXDayLater(self, xDay=7):
        try:
            bugun = datetime.now()
            date_ = QtCore.QDate(bugun.year, bugun.month, bugun.day)
            date_ = date_.addDays(xDay)
            return date_.toPyDate().strftime("%d %b %Y")
        except Exception as E:
            print(f"Fonk: returndate \t\t{E}")

    def setDateOnLabel(self):
        try:
            bugun = datetime.today()
            iadeTarihi = self.returnDateXDayLater( db.maxDayBooksStay )
            self.ui.label_verilisTarihi.setText(bugun.strftime("%d %b %Y"))
            # self.ui.label_verilisTarihi.setStyleSheet("QLabel{background-color:rgba(133,194,38,255);color:white; padding:10px; border-radius: 5px; font-size: 14pt }")
            self.ui.label_iadeTarihi.setText(iadeTarihi)
            # self.ui.label_iadeTarihi.setStyleSheet("QLabel{background-color: rgba(66,146,157,255); color:white; padding:10px; border-radius: 5px; font-size: 14pt}")
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: setDateOnLabel \t\tHata Kodu : {E}", self.duration)

    def createButtonForTablewidget(self, memberData=[]):
        try:
            layout = QHBoxLayout()
            btn = QPushButton("Ver")
            tcno = memberData[5]
            btn.setObjectName(tcno)
            btn.setStyleSheet("QPushButton{background-color:pink}")
            btn.setMinimumSize(15, 20)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect( self.showConfirmationPage_A )
            btn.setMaximumSize(30,20)
            layout.addWidget(btn)
            widget = QWidget()
            widget.setLayout(layout)
            Entrust.dictMembersInfos[tcno] = memberData
            return widget
        except Exception as E:
            print(f"Fonk: createButtonForTablewidget    \tHata: {E}")

    def clearSelection(self):
        try:
            Entrust.selectedBooksDict = {'KitapId':None,'KitapAdi':None}  # Bu silinmeli, yoksa son seçili kitaplar birden çok üyeye verilir.
            self.refreshTableWidgetItems()
            Entrust.selectedBarkodList = []  # Bu liste sıfırlanmalı, yoksa önceki seçilmiş kitaplar gitmez
        except Exception as E:
            print(f"Fonk: clearSelection    \tHata: {E}")

    def showConfirmationPage_A(self):                                             # Verme onay sayfası
        try:
            tcno        : str   = self.sender().objectName()
            memberId    : int   = Entrust.dictMembersInfos[tcno][0]
            Entrust.givenBookMemberId = memberId
            verilebilir : int   = Entrust.dictMembersInfos[tcno][1]
            memberName  : str   = " ".join( Entrust.dictMembersInfos[tcno][3:5])
            listBooksId : list  = Entrust.selectedBooksDict["KitapId"]
            if not listBooksId :
                msg.popup_mesaj('Dikkat', "Hiç eser seçmediniz !  Lütfen önce verilecek eserleri seçiniz.\t\n")
            else:
                if verilebilir < len( listBooksId ):
                    msg.popup_mesaj('Dikkat', f"{memberName} isimli üye en fazla {verilebilir} kitap alabilir. \t\n\nLütfen sadece {verilebilir} kitap seçiniz!\n")
                else:
                    self.winConfirmation.showConfirmationPage_B(memberData=Entrust.dictMembersInfos[tcno], booksData=Entrust.selectedBooksDict)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showConfirmationPage_A \t\tHata Kodu : {E}", self.duration)

    def giveBooksToMembers(self):                                           # Verme onaylanırsa yapılacaklar
        addedData = 0
        try:
            memberId    : int   = Entrust.givenBookMemberId
            listBooksId : list  = Entrust.selectedBooksDict["KitapId"]
            for bookId in listBooksId:
                db.insertData("EmanetTablosu", KitapId =bookId, UyeId =memberId, VerilisTarihi =datetime.today().date(), MaxKalmaSuresi=db.maxDayBooksStay)
                addedData += curs.rowcount
            if not addedData == -1:
                db.updateNumberOfBookAtMember(AldigiEserSayisi=addedData, uyeId=memberId)
                db.updateBookState(Durum=(0,) * len(listBooksId), kitapId=listBooksId)  # Durum=0 kitap müsait değil demek
                self.clearSelection()           # Burası neden çalışmıyor
                self.ui.le_searchBook.clear()
                self.ui.le_searchMember.clear()
                self.ui.statusbar.showMessage(f"{addedData} adet verilen kitap kaydı oluşturuldu")
        except Exception as E:
            print(f"Fonk: giveBooksToMembers \t\tHata Kodu : {E}")

    def addBookIdListOnDataDict(self, state):
        try:
            barcod = self.sender().objectName()
            if state:
                Entrust.selectedBarkodList.append(barcod)
            else:
                if barcod in Entrust.selectedBarkodList:
                    Entrust.selectedBarkodList.remove(barcod)
            listBookId   = tuple(Entrust.dictBooksInfos[b][0] for b in Entrust.selectedBarkodList)
            listBarkod   = tuple(Entrust.dictBooksInfos[b][1] for b in Entrust.selectedBarkodList)
            listBookName = tuple(Entrust.dictBooksInfos[b][2] for b in Entrust.selectedBarkodList)
            Entrust.selectedBooksDict["KitapId"]   = listBookId
            Entrust.selectedBooksDict["KitapAdi"]  = listBookName
            Entrust.selectedBooksDict["Barkod"]    = listBarkod

            # print("bookInfo ", Entrust.dictBooksInfos[barcod])
            # print('self.selectedBooksDict: ', Entrust.selectedBooksDict)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: addBookIdListOnDataDict \t\tHata Kodu : {E}", self.duration)

    def createCheckboxForTablewidget(self, bookData=[]):
        try:
            layout = QHBoxLayout()
            cBox = QCheckBox()
            cBox.setCheckState(False)
            barcodNo = bookData[1]
            Entrust.bookCheckboxObjectsForSelection[barcodNo] = cBox
            Entrust.dictBooksInfos[ barcodNo ] = bookData           # bookData[1] = Barkod number
            cBox.setObjectName( barcodNo )
            cBox.setMinimumSize(15, 15)
            cBox.clicked[bool].connect( self.addBookIdListOnDataDict )
            cBox.setMaximumSize(15, 15)
            cBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            layout.addWidget(cBox)
            widget = QWidget()
            widget.setLayout(layout)
            return widget
        except Exception as E:
            print(f"Fonk: createCheckboxForTablewidget  Hata: {E} ")

    def showBooksOnTablewidget(self):
        cols = ("kitapId", "Barkod", "KitapAdi", "YazarId", 'ISBN')
        colLabels = ("Seç", "Barkod No", f"{'Eser Adı':^40}", f"{'Eserin Yazarı':^30}", 'ISBN')
        try:
            self.ui.table_booksList.clear()
            books = db.getFreeBooks()
            if books:
                self.ui.table_booksList.setRowCount(len(books)+self.numberOfBlankLines)
                self.ui.table_booksList.setColumnCount(len(colLabels))
                self.ui.table_booksList.setHorizontalHeaderLabels(colLabels)
                for row, book in enumerate(books):
                    self.ui.table_booksList.setCellWidget(row, 0, self.createCheckboxForTablewidget(book))
                    for index, item in enumerate(book[1:]):
                        col = index+1
                        self.ui.table_booksList.setItem(row,col,QTableWidgetItem(str(item if item else "")))
                        if col in (1,4):
                            self.ui.table_booksList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                self.resizeEvent(QtGui.QResizeEvent)
                # self.ui.table_booksList.resizeColumnsToContents()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksOnTablewidget     Hata Kodu : {E}", self.duration)

    def filterBooksOnTablewidget(self) -> None:
        try:
            aranan = self.ui.le_searchBook.text()
            if self.ui.radio_barkod.isChecked()     : col = 1
            elif self.ui.radio_kitapAdi.isChecked() : col = 2
            elif self.ui.radio_isbn.isChecked()     : col = 4
            rows = self.ui.table_booksList.rowCount()
            for row in range(rows-self.numberOfBlankLines):
                item = self.ui.table_booksList.item(row,col)
                if item is not None:
                    if aranan.lower() in item.text().lower() or item.text().lower() in aranan.lower():
                        self.ui.table_booksList.showRow(row)
                    else:
                        self.ui.table_booksList.hideRow(row)
        except Exception as E:
            print(E)

    def filterMembersOnTablewidget(self) -> None:
        try:
            aranan = self.ui.le_searchMember.text()
            if self.ui.radio_tc.isChecked()         :  col = 5
            elif self.ui.radio_isim.isChecked()     :  col = 3
            elif self.ui.radio_okulNo.isChecked()   :  col = 2
            rows = self.ui.table_membersList.rowCount() - self.numberOfBlankLines
            for row in range(rows):
                item = self.ui.table_membersList.item(row,col)
                if item is not None:
                    if aranan.lower() not in item.text().lower():
                        self.ui.table_membersList.hideRow(row)
                    else:
                        self.ui.table_membersList.showRow(row)
        except Exception as E:
            print(E)

    def showMembersInTablewidget(self) -> None:
        try:
            cols = ("uyeId", "OkulNo", f"{'Ad':^30}", f"{'Soyad':^15}", "TCNo", "Sinif", "Sube", "EldekiSayi")
            colLabels = ("Tıkla", 'Alabilir', "Okul No", f"{'Ad':^35}", f"{'Soyad':^20}", f"{'TC Kimlik No':^20}", "Sınıf", "Şube")
            self.ui.table_membersList.clear()
            self.ui.table_membersList.setColumnCount(len(cols))
            self.ui.table_membersList.setHorizontalHeaderLabels(colLabels)
            self.ui.table_membersList.setColumnCount(len(colLabels))
            memberData = db.getMemberDataNumberOfRead()
            self.ui.table_membersList.setRowCount(len(memberData) + self.numberOfBlankLines)
            for row, uye in enumerate(memberData):
                if uye[1] > 0:
                    self.ui.table_membersList.setCellWidget(row, 0, self.createButtonForTablewidget(uye))        # butonu burda Tablewidgeta uerleştiriyoruz
                for index, info in enumerate( uye[1:8] ):
                    col = index+1
                    self.ui.table_membersList.setItem(row, col, QTableWidgetItem(str(info)))
                    if col in (1,2,5,6,7):
                        self.ui.table_membersList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
            # self.ui.table_membersList.resizeColumnsToContents()
            self.resizeEvent(QtGui.QResizeEvent)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showMembersInTablewidget \t\t Hata Kodu : {E}", self.duration)