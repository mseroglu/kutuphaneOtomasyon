import datetime
import sys, locale

locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')


from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget

from PyQt5 import QtGui, QtCore
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog, QPrinter

from ui.anasayfaUI import Ui_MainWindow
from member_save import SaveMember
from book_save import SaveBook
from transactions_entrust import Entrust
from settings_page import Settings_page
from reports import ReportsPage

from database import db, curs, tableWidgetResize
from messageBox import msg




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Kütüphanem")
        self.setGeometry(200,50,800,600)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.le_searchOutsides.setVisible(False)
        self.ui.le_searchExpired.setVisible(False)
        self.ui.le_searchGivenToday.setVisible(False)
        self.ui.le_searchMember.setVisible(False)
        self.ui.le_searchBook.setVisible(False)
        self.ui.combo_searchCriteriaOutside.setVisible(False)
        self.ui.combo_searchCriteriaExpired.setVisible(False)
        self.ui.combo_searchCriteriaTodayGiven.setVisible(False)
        self.ui.combo_searchCriteriaMember.setVisible(False)
        self.ui.combo_searchCriteriaBook.setVisible(False)
        self.numberOfBlankLines = 20
        self.duration           = 20_000
        self.dictEscrowBookInfos= {}

        self.addItemsInCombos()

        self.ui.btn_searchOutside.clicked['bool'].connect(self.clearSearching)
        self.ui.btn_searchBook.clicked['bool'].connect(self.clearSearching)
        self.ui.btn_searchMember.clicked['bool'].connect(self.clearSearching)
        self.ui.btn_searchExpired.clicked['bool'].connect(self.clearSearching)
        self.ui.btn_searchGivenToday.clicked['bool'].connect(self.clearSearching)

        self.ui.tabWidget.currentChanged.connect(self.showEvent)
        self.ui.le_searchBarcode.cursorPositionChanged.connect(self.bookStateControl)

        self.ui.le_searchMember.textChanged.connect(self.genelfilter)
        self.ui.le_searchBook.textChanged.connect(self.genelfilter)
        self.ui.le_searchGivenToday.textChanged.connect(self.genelfilter)
        self.ui.le_searchExpired.textChanged.connect(self.genelfilter)
        self.ui.le_searchOutsides.textChanged.connect(self.genelfilter)



        self.ui.btn_openSaveBook.clicked.connect(winSaveBook.show)
        self.ui.btn_openSaveBook.clicked.connect(self.openWindowControl)
        self.ui.btn_openMemberSave.clicked.connect(winSaveMember.show)
        self.ui.btn_openMemberSave.clicked.connect(self.openWindowControl)
        self.ui.btn_openTransactions.clicked.connect(winEntrust.show)
        self.ui.btn_openTransactions.clicked.connect(self.openWindowControl)
        self.ui.btn_openSettings.clicked.connect(winSettings.show)
        self.ui.btn_openSettings.clicked.connect(self.openWindowControl)
        self.ui.btn_openReports.clicked.connect(winReports.show)
        self.ui.btn_openReports.clicked.connect(self.openWindowControl)
        self.ui.btn_quit.clicked.connect(sys.exit)

        # self.ui.btn_searchOutside.clicked.connect(self.handlePreview)

    def tusaBasYaziYazdir(self):
        key_press = QtGui.QKeyEvent(QtGui.QKeyEvent.KeyPress, QtCore.Qt.Key_X, QtCore.Qt.NoModifier, "X")
        QApplication.sendEvent(self.ui.le_searchBarcode, key_press)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.ui.le_searchBarcode.setFocus()


    def handlePreview(self):
        try:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreview   \t\t{E}")


    # ve son olarak belgeyi oluşturmak ve yazdırmak için bazı yöntemler:

    def handlePaintRequest(self, printer):
        try:
            document = self.makeTableDocument()
            document.print_(printer)
        except Exception as E:
            print(f"Fonk: handlePaintRequest   \t\t{E}")

    def imgDataToQImageObj(self, imgData) -> QtGui.QImage :
        imgDataToQImageObj = open("./imgBarkode/00000246.png", "rb").read()
        image = QtGui.QImage()
        image.loadFromData(imgDataToQImageObj)
        return image.scaledToWidth(150)

    def makeTableDocument(self):
        try:
            # setPixmap(pixmap.scaled(width, width, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
            document    = QtGui.QTextDocument()
            cursor      = QtGui.QTextCursor(document)
            # math.ceil(rows/6)
            rows    = 16
            columns = 4

            table   = cursor.insertTable(rows, columns)
            formatT = table.format()
            formatT.setAlignment( QtCore.Qt.AlignCenter )
            table.setFormat(formatT)
            formatC = cursor.blockCharFormat()
            formatC.setFontWeight(QtGui.QFont.Normal)
            for row in range(rows):
                for column in range(columns):
                    if not row % 2:
                        cursor.setCharFormat(formatC)
                        cursor.insertText(f"   Bölüm\t: {'A12'}\n   Raf No\t: {'A123'}\n   ISBN\t: {9876543210123}\n   {3*'Kitap Adı'}")
                    else:
                        image = self.imgDataToQImageObj(imgData="")
                        cursor.insertImage(image)
                    cursor.movePosition(QtGui.QTextCursor.NextCell)

            return document
        except Exception as E:
            print(f"Fonk: makeTableDocument   \t\t{E}")



    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        tableWidgetResize(self.ui.table_memberList, (2, 2, 3, 2, 6, 4, 2, 1, 1, 3, 3, 3, 3), blank=50)
        tableWidgetResize(self.ui.table_bookList, (2, 3, 6, 4, 2, 2, 2, 3, 2, 2, 3, 2, 2), blank=50)
        tableWidgetResize(self.ui.table_givenToday, (3, 6, 4, 3, 2, 5, 3, 1, 1, 3, 2, 3), blank=50)
        tableWidgetResize(self.ui.table_expaired, (3, 3, 6, 4, 3, 2, 3, 4, 2, 5, 3, 1, 1), blank=50)
        tableWidgetResize(self.ui.table_outsides, (3, 3, 6, 4, 3, 3, 3, 4, 2, 5, 3, 1, 1), blank=50)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        try:
            self.ui.le_searchBarcode.setFocus()
            self.openWindowControl()
            self.showBooksOnTablewidget()
            self.showMembersInTablewidget()
            self.showOutsidesOnTablewidget()
            self.showTodayEntrustOnTablewidget()
            self.showBooksReturnTodayOnTablewidget()
        except Exception as E:
            print(f"Fonk: showEvent  \tHata : {E}")

    def openWindowControl(self):
        if winSaveBook.isActiveWindow():
            winSaveMember.close()
            winEntrust.close()
            winSettings.close()
            winReports.close()
        elif winSaveMember.isActiveWindow():
            winSaveBook.close()
            winEntrust.close()
            winSettings.close()
            winReports.close()
        elif winEntrust.isActiveWindow():
            winSaveBook.close()
            winSaveMember.close()
            winSettings.close()
            winReports.close()
        elif winSettings.isActiveWindow():
            winSaveBook.close()
            winSaveMember.close()
            winEntrust.close()
            winReports.close()
        elif winReports.isActiveWindow():
            winSaveBook.close()
            winSaveMember.close()
            winEntrust.close()
            winSettings.close()

    def clearSearching(self, state):
        if not state:
            self.ui.le_searchBook.clear()
            self.ui.le_searchMember.clear()
            self.ui.le_searchExpired.clear()
            self.ui.le_searchOutsides.clear()
            self.ui.le_searchGivenToday.clear()

    def bookStateControl(self, old, new):
        try:
            self.ui.le_searchOutsides.clear()
            if new==8:
                barkod = self.ui.le_searchBarcode.text()
                bookStateData = db.getBookState(Barkod=barkod)
                if bookStateData:
                    if bookStateData[0]:
                        winEntrust.show()
                        winEntrust.ui.le_searchBook.setText(barkod)
                        self.ui.le_searchBarcode.clear()
                    else:
                        self.genelfilter()
            else:
                self.genelfilter()
        except Exception as E:
            print(E)

    def addItemsInCombos(self):                 #       *item  Bu kullanım tuple olan itemı parçalara böler. Burada 2 parçaya bölünecek
        try:
            for item in (("Barkod", 1), ("Eser Adı", 2), ("Yazar Adı", 3), ("TC Kimlik No", 7), ("Okul No", 8), ("Üye Adı", 9), ("Üye Soyadı", 10)):
                self.ui.combo_searchCriteriaOutside.addItem(*item)
            for item in (("Eser Adı", 2), ("Yazar Adı", 3), ("Barkod", 1), ("TC Kimlik No", 7), ("Okul No", 8), ("Üye Adı", 9),("Üye Soyadı", 10)):
                self.ui.combo_searchCriteriaExpired.addItem(*item)
            for item in (("Eser Adı", 1), ("Yazar Adı", 2), ("Barkod", 0), ("TC Kimlik No", 3), ("Okul No", 4), ("Üye Adı", 5),("Üye Soyadı", 6)):
                self.ui.combo_searchCriteriaTodayGiven.addItem(*item)
            for item in (("Okul No", 3), ("Üye Adı", 4), ("Üye Soyadı", 5), ("TC Kimlik No", 2)):
                self.ui.combo_searchCriteriaMember.addItem(*item)
            for item in (("Eser Adı", 2), ("Yazar Adı", 3), ("Barkod", 0), ("ISBN", 1)):
                self.ui.combo_searchCriteriaBook.addItem(*item)
        except Exception as E:
            print(f"Fonk: addItemsInCombos  \tHata: {E}")

    def genelfilter(self):
        filtreKaynagiObj = {"le_searchMember"       : (self.ui.le_searchMember,     self.ui.table_memberList,   self.ui.combo_searchCriteriaMember),
                            "le_searchBook"         : (self.ui.le_searchBook,       self.ui.table_bookList,     self.ui.combo_searchCriteriaBook),
                            "le_searchOutsides"     : (self.ui.le_searchOutsides,   self.ui.table_outsides,     self.ui.combo_searchCriteriaOutside),
                            "le_searchExpired"      : (self.ui.le_searchExpired,    self.ui.table_expaired,     self.ui.combo_searchCriteriaExpired),
                            "le_searchGivenToday"   : (self.ui.le_searchGivenToday, self.ui.table_givenToday,   self.ui.combo_searchCriteriaTodayGiven),
                            "le_searchBarcode"      : (self.ui.le_searchBarcode,    self.ui.table_outsides,     self.ui.combo_searchCriteriaOutside)}
        sinyalObj       = self.sender().objectName()
        filtreKaynagi   = filtreKaynagiObj[ sinyalObj ]
        if sinyalObj == "le_searchBarcode":
            self.ui.combo_searchCriteriaOutside.setCurrentIndex(0)
            self.ui.tabWidget.setCurrentWidget(self.ui.tab_outsides)
        try:
            ara     = filtreKaynagi[0].text()
            rows    = filtreKaynagi[1].rowCount() - self.numberOfBlankLines
            combo   = filtreKaynagi[2]
            col     = combo.currentData(QtCore.Qt.UserRole)
            for row in range(rows):
                item = filtreKaynagi[1].item(row, col)
                if item is not None:
                    if ara.lower() in item.text().lower():
                        filtreKaynagi[1].showRow(row)
                    else:
                        filtreKaynagi[1].hideRow(row)
        except Exception as E:
            print(f"Fonk: genelFiltre Hata: {E}")

    def createButtonForTablewidget(self, data: list ) -> QWidget :
        try:
            layout = QHBoxLayout()
            btn = QPushButton("Geri Al")
            barkod = data[2]
            btn.setObjectName(barkod)
            if data[6] < 1: btn.setStyleSheet('QPushButton{background-color:pink}')
            btn.setMinimumSize(15, 20)
            btn.clicked.connect( self.returnTheBook )
            btn.setMaximumSize(60,20)
            layout.addWidget(btn)
            widget = QWidget()
            widget.setLayout(layout)
            self.dictEscrowBookInfos[barkod] = data
            return widget
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: createButtonForTablewidget \t\tHata Kodu : {E}", self.duration)

    def returnTheBook(self) -> None:
        try:
            barkod      = self.sender().objectName()
            bookInfo    = self.dictEscrowBookInfos[barkod]
            print(bookInfo)
            bookId, escrowId, bookName, tcno, name, lastname = bookInfo[0], bookInfo[1], bookInfo[3], bookInfo[8], bookInfo[10], bookInfo[11]
            cevap, _    = msg.MesajBox("Geri alma işlemi", f"BARKOD NO\t:  {barkod} \nKİTAP ADI\t:  {bookName} \n\n"
                                                           f"'{name+' '+lastname}' isimli üyeden yukardaki kitabı teslim alıyorsunuz.\t\n\n"
                                                           "Emin misiniz?\n")
            if cevap:
                returnDate  = datetime.date.today()
                db.updateNumberOfBookAtMember(AldigiEserSayisi=-1, TCNo=tcno)
                db.updateBookState( Durum=(1,), kitapId=(bookId,) )            # Durum=1 'Rafta', Durum=0 "Okunuyor"
                kitapDurum = curs.rowcount
                db.updateEntrustTableEscrowState( "EmanetTablosu", DonusTarihi=returnDate, emanetId=escrowId )
                emanetDurum= curs.rowcount
                if kitapDurum == 1 and emanetDurum == 1 :
                    title,mesaj = "Başarılı","Geri alma işlemi başarılı. Kitabı rafına koyunuz !\t\t\n"
                    self.showOutsidesOnTablewidget()
                elif kitapDurum < 1 and emanetDurum == 1:
                    title, mesaj = "Dikkat Problem", "Kitap geri alımı gerçekleşti.\n" \
                                                    "Ancak kitap durumu 'Okunuyor' dan 'Rafta' haline gelmedi !\n" \
                                                    "Kitap 'Rafta' gözükmezse onu listede göremez ve artık veremezsiniz\n"
                else:
                    title, mesaj = "DİKKAT : Başarısız ! ! !", "Kitap geri alımı başarısız, lütfen tekrar deneyiniz !\t\t\n"
                msg.popup_mesaj(title,mesaj )
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: returnTheBook \t\tHata Kodu : {E}", self.duration)

    def showMembersInTablewidget(self):
        try:
            colLabels   = ("Üye Tipi", "Durum", f"{'TC Kimlik No':^20}", "Okul No", f"{'Ad':^35}", f"{'Soyad':^15}",
                "Cinsiyet", "Sınıf", "Şube", f"{'Telefon':^20}", "Doğum Tarihi", "Üyelik Tarihi", f"{'Foto':^20}")
            self.ui.table_memberList.clear()
            self.ui.table_memberList.setColumnCount(len(colLabels))
            self.ui.table_memberList.setHorizontalHeaderLabels(colLabels)
            cameData = db.getMemberDataWithWhere()
            self.ui.table_memberList.setRowCount(len(cameData) + self.numberOfBlankLines)
            for row, uye in enumerate(cameData):
                for col, info in enumerate(uye):
                    self.ui.table_memberList.setItem(row, col, QTableWidgetItem(str(info if info else '')))
                    if uye[0] == "Personel":
                        self.ui.table_memberList.item(row, col).setBackground(QtGui.QColor("#d9ead3"))
                    if col in (2,3,7,8,10,11):
                        self.ui.table_memberList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
            self.resizeEvent(QtGui.QResizeEvent)
            # self.ui.table_memberList.resizeColumnsToContents()
            self.ui.table_memberList.horizontalHeader().setStretchLastSection(True)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showMembersInTablewidget \t\t Hata Kodu : {E}", self.duration)

    def showBooksOnTablewidget(self):
        try:
            colLabels = ('Barkod ', f"{'ISBN':^20}", f"{'Eser Adı':^30}", f'{"Yazarı":^20}', 'Kategori', 'Bölüm',
                         'Raf No', 'Yayınevi', 'Sayfa Sayısı', 'Basım Yılı', 'Kayıt Tarihi', 'Durum', 'Açıklama')
            self.ui.table_bookList.clear()
            self.ui.table_bookList.setColumnCount(len(colLabels))
            self.ui.table_bookList.setHorizontalHeaderLabels(colLabels)
            books = db.getBookDataWithJoinTables()
            if books:
                self.ui.table_bookList.setRowCount(len(books)+self.numberOfBlankLines)
                for row, book in enumerate(books):
                    for col, item in enumerate(book):
                        self.ui.table_bookList.setItem(row,col,QTableWidgetItem(str(item if item else "")))
                        if book[11] == "Okunuyor":
                            self.ui.table_bookList.item(row, col).setBackground(QtGui.QColor("#d9ead3"))
                        if col in (0,1,8,9,10):
                            self.ui.table_bookList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                self.resizeEvent(QtGui.QResizeEvent)
                # self.ui.table_bookList.resizeColumnsToContents()
                self.ui.table_bookList.horizontalHeader().setStretchLastSection(True)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksOnTablewidget     Hata Kodu : {E}", self.duration)

    def showTodayEntrustOnTablewidget(self):
        try:
            colLabels = ('Barkod', f'{"Eser Adı":^40}', f'{"Yazarı":^25}', 'TC Kimlik Nosu', 'Okul No', f'{"Ad":^25}',
                         f'{"Soyad":^15}', 'Sınıf','Şube', 'Veriliş Tarihi', 'Kalan Gün', 'İade Tarihi')
            self.ui.table_givenToday.clear()
            self.ui.table_givenToday.setColumnCount(len(colLabels))
            self.ui.table_givenToday.setHorizontalHeaderLabels(colLabels)
            todayEntrusted = db.getEntrustToday()
            if todayEntrusted:
                self.ui.table_givenToday.setRowCount(len(todayEntrusted)+self.numberOfBlankLines)
                for row, book in enumerate(todayEntrusted):
                    for col, item in enumerate(book):
                        self.ui.table_givenToday.setItem(row,col,QTableWidgetItem(str(item if item else '')))
                        if col in (0,3,4,7,8,9,10,11):
                            self.ui.table_givenToday.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                # self.ui.table_givenToday.resizeColumnsToContents()
                self.resizeEvent(QtGui.QResizeEvent)
                self.ui.table_givenToday.horizontalHeader().setStretchLastSection(True)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showTodayEntrustOnTablewidget\t\t Hata Kodu : {E}", self.duration)

    def showOutsidesOnTablewidget(self):
        try:
            colLabels = ('Tıkla','Barkod No', f'{"Eser Adı":^35}', f'{"Yazarı":^30}',"Veriliş Tarihi","Kalan Gün","İade Tarihi",
                         'TC Kimlik No','Okul No',f'{"Ad":^25}',f'{"Soyad":^15}','Sınıf','Şube')
            self.ui.table_outsides.clearContents()
            self.ui.table_outsides.setColumnCount(len(colLabels))
            # self.ui.table_outsides.setHorizontalHeaderLabels(colLabels)
            outsides = db.getOutsides()
            if outsides:
                self.ui.table_outsides.setRowCount(len(outsides)+self.numberOfBlankLines)
                for row, book in enumerate(outsides):
                    self.ui.table_outsides.setCellWidget(row,0, self.createButtonForTablewidget( book ))        # Tablewidgwta buton yerleştirme
                    for index, item in enumerate(book[2:]):
                        col = index+1
                        self.ui.table_outsides.setItem(row,col,QTableWidgetItem(str(item if item!=None else '')))
                        if col in (1,4,5,6,7,8,11,12):
                            self.ui.table_outsides.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                # self.ui.table_outsides.resizeColumnsToContents()
                self.resizeEvent(QtGui.QResizeEvent)
                self.ui.table_outsides.horizontalHeader().setStretchLastSection(True)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showTodayEntrustOnTablewidget\t\t Hata Kodu : {E}", self.duration)

    def showBooksReturnTodayOnTablewidget(self):
        try:
            colLabels = ('Tıkla', 'Barkod', f'{"Eser Adı":^30}', f'{"Yazarı":^20}', "Veriliş Tarih", "Kalan Gün", "İade Tarihi",
                         'TC Kimlik No', 'Okul No', f'{"Ad":^30}', f'{"Soyad":^15}', 'Sınıf', 'Şube')
            self.ui.table_expaired.clear()
            self.ui.table_expaired.setColumnCount(len(colLabels))
            self.ui.table_expaired.setHorizontalHeaderLabels(colLabels)
            booksReturnToday = db.getEscrowBooksReturnToday()
            if booksReturnToday:
                self.ui.table_expaired.setRowCount(len(booksReturnToday) + self.numberOfBlankLines)
                for row, book in enumerate(booksReturnToday):
                    self.ui.table_expaired.setCellWidget(row, 0, self.createButtonForTablewidget(book))
                    for index, item in enumerate(book[2:]):
                        col = index+1
                        self.ui.table_expaired.setItem(row, col, QTableWidgetItem(str(item)))
                        if col in (1,4,5,6,7,8,11,12):
                            self.ui.table_expaired.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                # self.ui.table_expaired.resizeColumnsToContents()
                self.resizeEvent(QtGui.QResizeEvent)
                self.ui.table_expaired.horizontalHeader().setStretchLastSection(True)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksReturnTodayOnTablewidget\t\t Hata Kodu : {E}", self.duration)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    winSaveBook     = SaveBook()
    winSaveMember   = SaveMember()
    winEntrust      = Entrust()
    winSettings     = Settings_page()
    winReports      = ReportsPage()

    winMain         = MainWindow()

    winMain.show()


    app.setStyle("Fusion")
    sys.exit(app.exec_())


# .\pyrcc5 C:\PythonProje\kitaplik\icons.qrc -o C:\PythonProje\kitaplik\icons_rc.py

#------------------- pyinstaller --noconsole --onefile -i "img/kitaplik.ico" main.py ------------------#
#------------------------ pyinstaller --noconsole -i "img/kitaplik.ico" main.py -----------------------#