import datetime
import sys, os, locale
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QCheckBox, QComboBox
from PyQt5 import QtGui, QtCore
from ui.anasayfaUI import Ui_MainWindow

from member_save import SaveMember
from book_save import SaveBook
from transactions_entrust import Entrust
from settings_page import Settings_page

from database import db, curs
from messageBox import msg



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Kütüphanem")
        self.setGeometry(200,50,800,600)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.duration = 20_000
        self.dictEscrowBookInfos    = {}

        self.ui.tabWidget.currentChanged.connect(self.showEvent)



        self.ui.btn_openSaveBook.clicked.connect(winSaveBook.show)
        self.ui.btn_openSaveBook.clicked.connect(self.openWindowControl)
        self.ui.btn_openMemberSave.clicked.connect(winSaveMember.show)
        self.ui.btn_openMemberSave.clicked.connect(self.openWindowControl)
        self.ui.btn_openTransactions.clicked.connect(winEntrust.show)
        self.ui.btn_openTransactions.clicked.connect(self.openWindowControl)
        self.ui.btn_openSettings.clicked.connect(winSettings.show)
        self.ui.btn_openSettings.clicked.connect(self.openWindowControl)
        self.ui.btn_quit.clicked.connect(sys.exit)




    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        try:
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
        elif winSaveMember.isActiveWindow():
            winSaveBook.close()
            winEntrust.close()
            winSettings.close()
        elif winEntrust.isActiveWindow():
            winSaveBook.close()
            winSaveMember.close()
            winSettings.close()
        elif winSettings.isActiveWindow():
            winSaveBook.close()
            winSaveMember.close()
            winEntrust.close()


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
            print("Geri alınan kitap : ", bookInfo)
            bookId, escrowId, bookName, name, lastname = bookInfo[0], bookInfo[1], bookInfo[3], bookInfo[10], bookInfo[11]
            cevap,_     = msg.MesajBox("Geri alma işlemi", f"BARKOD NO\t:  {barkod[7:]} \nKİTAP ADI\t:  {bookName} \n\n"
                                                           f"'{name+' '+lastname}' isimli üyeden yukardaki kitabı teslim alıyorsunuz.\t\n\n"
                                                           "Emin misiniz?\n")
            if cevap:
                returnDate  = datetime.date.today()
                db.updateBookTableState( Durum=(1,), kitapId=(bookId,) )            # Durum=1 'Rafta', Durum=0 "Okunuyor"
                kitapDurum = curs.rowcount
                db.updateEntrustTableEscrowState( "EmanetTablosu", DonusTarihi=returnDate, emanetId=escrowId )
                emanetDurum= curs.rowcount
                if kitapDurum==1 and emanetDurum==1:
                    title,mesaj = "Başarılı","Geri alma işlemi başarılı. Kitabı rafına koyunuz !\t\t\n"
                    self.showOutsidesOnTablewidget()
                elif kitapDurum<1 and emanetDurum==1:
                    title,mesaj = "Dikkat Problem", "Kitap geri alımı gerçekleşti.\n" \
                                                    "Ancak kitap durumu 'Okunuyor' dan 'Rafta' haline gelmedi !\n" \
                                                    "Kitap 'Rafta' gözükmezse onu listede göremez ve artık veremezsiniz\n"
                else:
                    title, mesaj = "DİKKAT : Başarısız ! ! !", "Kitap geri alımı başarısız, lütfen tekrar deneyiniz !\t\t\n"
                msg.popup_mesaj(title,mesaj )
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: returnTheBook \t\tHata Kodu : {E}", self.duration)

    def showMembersInTablewidget(self):
        try:
            colLabels   = ("Üye Tipi", "Durum", "TC Kimlik No", "Okul No", "Ad", "Soyad", "Cinsiyet", "Sınıf", "Şube",
                           "Telefon", "Doğum Tarihi", "Üyelik Tarihi", "Foto")
            self.ui.table_memberList.clear()
            self.ui.table_memberList.setColumnCount(len(colLabels))
            self.ui.table_memberList.setHorizontalHeaderLabels(colLabels)
            cameData = db.getMemberDataWithWhere()
            self.ui.table_memberList.setRowCount(len(cameData) + 10)
            for row, uye in enumerate(cameData):
                for col, info in enumerate(uye):
                    self.ui.table_memberList.setItem(row, col, QTableWidgetItem(str(info if info else '')))
                    if uye[0] == "Personel":
                        self.ui.table_memberList.item(row, col).setBackground(QtGui.QColor("#d9ead3"))
                    if col in (2,3,7,8,10,11):
                        self.ui.table_memberList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.table_memberList.resizeColumnsToContents()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showMembersInTablewidget \t\t Hata Kodu : {E}", self.duration)

    def showBooksOnTablewidget(self):
        try:
            colLabels = ('Barkod', "ISBN", "Eser Adı", 'Yazarı','Kategori','Bölüm','Raf No','Yayınevi','Sayfa Sayısı',
                        'Basım Yılı','Açıklama', 'Kayıt Tarihi', 'Durum')
            self.ui.table_bookList.clear()
            self.ui.table_bookList.setColumnCount(len(colLabels))
            self.ui.table_bookList.setHorizontalHeaderLabels(colLabels)
            books = db.getBookDataWithJoinTables()
            if books:
                self.ui.table_bookList.setRowCount(len(books)+20)
                for row, book in enumerate(books):
                    for col, item in enumerate(book):
                        if col == 0: item = item[7:]
                        self.ui.table_bookList.setItem(row,col,QTableWidgetItem(str(item if item else "")))
                        if book[12] == "Okunuyor":
                            self.ui.table_bookList.item(row, col).setBackground(QtGui.QColor("#d9ead3"))
                        if col in (0,1,8,9,11):
                            self.ui.table_bookList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table_bookList.resizeColumnsToContents()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksOnTablewidget     Hata Kodu : {E}", self.duration)

    def showTodayEntrustOnTablewidget(self):
        try:
            colLabels = ('Barkod','Eser Adı','Yazarı','Üye No','Okul No','Ad','Soyad','Sınıf','Şube', 'Alma Tarihi', 'İade Tarihi', 'Kalan Gün')
            self.ui.table_givenToday.clear()
            self.ui.table_givenToday.setColumnCount(len(colLabels))
            self.ui.table_givenToday.setHorizontalHeaderLabels(colLabels)
            todayEntrusted = db.getEntrustToday()
            if todayEntrusted:
                self.ui.table_givenToday.setRowCount(len(todayEntrusted)+20)
                for row, book in enumerate(todayEntrusted):
                    for col, item in enumerate(book):
                        if col == 0: item = item[7:]
                        self.ui.table_givenToday.setItem(row,col,QTableWidgetItem(str(item if item else '')))
                        if col in (0,3,4,7,8,9,10,11):
                            self.ui.table_givenToday.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table_givenToday.resizeColumnsToContents()
                self.ui.table_givenToday.horizontalHeader().setStretchLastSection(True)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showTodayEntrustOnTablewidget\t\t Hata Kodu : {E}", self.duration)

    def showOutsidesOnTablewidget(self):
        try:
            colLabels = ('Tıkla','Barkod','Eser Adı','Yazarı',"Verildiği Tarih","Kalan Gün","Son İade Tarihi",
                         'Üye No','Okul No','Ad','Soyad','Sınıf','Şube')
            self.ui.table_outsides.clear()
            self.ui.table_outsides.setColumnCount(len(colLabels))
            self.ui.table_outsides.setHorizontalHeaderLabels(colLabels)
            outsides = db.getOutsides()
            if outsides:
                self.ui.table_outsides.setRowCount(len(outsides)+20)
                for row, book in enumerate(outsides):
                    self.ui.table_outsides.setCellWidget(row,0, self.createButtonForTablewidget( book ))        # Tablewidgwta buton yerleştirme
                    for col, item in enumerate(book[2:]):
                        if col == 0: item = item[7:]
                        self.ui.table_outsides.setItem(row,col+1,QTableWidgetItem(str(item if item!=None else '')))
                        if col in (1,4,5,6,7,8,11,12):
                            self.ui.table_outsides.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table_outsides.resizeColumnsToContents()
                self.ui.table_outsides.setContentsMargins(0, 0, 0, 0)
                self.ui.table_outsides.setViewportMargins(0,0,0,0)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showTodayEntrustOnTablewidget\t\t Hata Kodu : {E}", self.duration)

    def showBooksReturnTodayOnTablewidget(self):
        try:
            colLabels = ('Tıkla', 'Barkod', 'Eser Adı', 'Yazarı', "Verildiği Tarih", "Kalan Gün", "Son İade Tarihi",
                         'Üye No', 'Okul No', 'Ad', 'Soyad', 'Sınıf', 'Şube')
            self.ui.table_expaired.clear()
            self.ui.table_expaired.setColumnCount(len(colLabels))
            self.ui.table_expaired.setHorizontalHeaderLabels(colLabels)
            booksReturnToday = db.getEscrowBooksReturnToday()
            if booksReturnToday:
                self.ui.table_expaired.setRowCount(len(booksReturnToday) + 20)
                for row, book in enumerate(booksReturnToday):
                    self.ui.table_expaired.setCellWidget(row, 0, self.createButtonForTablewidget(book))
                    for col, item in enumerate(book[2:]):
                        if col==0: item = item[7:]
                        self.ui.table_expaired.setItem(row, col+1, QTableWidgetItem(str(item)))
                        if col in (1,4,5,6,7,8,11,12):
                            self.ui.table_expaired.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksReturnTodayOnTablewidget\t\t Hata Kodu : {E}", self.duration)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    winSaveBook = SaveBook()
    winSaveMember = SaveMember()
    winEntrust = Entrust()
    winSettings = Settings_page()

    winMain = MainWindow()

    winMain.show()


    app.setStyle("Fusion")
    sys.exit(app.exec_())
