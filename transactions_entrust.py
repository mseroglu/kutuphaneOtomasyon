from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, "")

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHBoxLayout, QWidget, QCheckBox, QRadioButton, QPushButton
from PyQt5 import QtGui, QtCore
from ui.emanetVermeUI import Ui_MainWindow
from database import db, curs
from messageBox import msg
import sys, os
class Entrust(QMainWindow):                         # Entrust = Emanet
    def __init__(self):
        super(Entrust, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.numberOfBlankLines = 20
        self.duration           = 20_000
        self.dictBooksInfos     = {}
        self.dictMembersInfos   = {}
        self.barkodList         = []
        self.selectedBooksDict = {'KitapId':None,'KitapAdi':None}

        self.yenile()
        self.ui.radio_isim.clicked.connect(self.filterMembersOnTablewidget)
        self.ui.radio_tc.clicked.connect(self.filterMembersOnTablewidget)
        self.ui.radio_okulNo.clicked.connect(self.filterMembersOnTablewidget)
        self.ui.le_searchMember.textChanged.connect(self.filterMembersOnTablewidget)
        self.ui.le_searchBook.textChanged.connect(self.filterBooksOnTablewidget)
        self.ui.radio_barkod.clicked.connect(self.filterBooksOnTablewidget)
        self.ui.radio_isbn.clicked.connect(self.filterBooksOnTablewidget)
        self.ui.radio_kitapAdi.clicked.connect(self.filterBooksOnTablewidget)

        self.ui.btn_clearSelection.clicked.connect(self.clearSelection)




    def yenile(self):
        self.showMembersInTablewidget()
        self.showBooksOnTablewidget()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.setDateOnLabel()
        self.yenile()

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
            self.ui.label_verilisTarihi.setStyleSheet("QLabel{background-color:green;color:white; padding:10px }")
            self.ui.label_iadeTarihi.setText(iadeTarihi)
            self.ui.label_iadeTarihi.setStyleSheet("QLabel{background-color:red;color:white; padding:10px}")
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: giveBooksToMembers \t\tHata Kodu : {E}", self.duration)

    def createButtonForTablewidget(self, memberData=[]):
        layout = QHBoxLayout()
        btn = QPushButton("Ver")
        tcno = memberData[5]
        btn.setObjectName(tcno)
        btn.setStyleSheet("QPushButton{background-color:pink}")
        btn.setMinimumSize(15, 20)
        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn.clicked.connect( self.giveBooksToMembers )
        btn.setMaximumSize(30,20)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.dictMembersInfos[tcno] = memberData
        return widget

    def clearSelection(self):
        try:
            self.selectedBooksDict = {'KitapId':None,'KitapAdi':None}  # Bu silinmeli, yoksa son seçili kitaplar birden çok üyeye verilir.
            self.showBooksOnTablewidget()
            self.showMembersInTablewidget()
            self.barkodList = []  # Bu liste sıfırlanmalı, yoksa önceki seçilmiş kitaplar gitmez
        except Exception as E:
            print(f"Fonk: clearSelection    \tHata: {E}")

    def giveBooksToMembers(self):
        addedData = 0
        try:
            tcno        = self.sender().objectName()
            memberId    = self.dictMembersInfos[tcno][0]
            verilebilir = self.dictMembersInfos[tcno][1]
            memberName  = " ".join( self.dictMembersInfos[tcno][3:5])
            listBooksId = self.selectedBooksDict["KitapId"]
            listBooksName = self.selectedBooksDict["KitapAdi"]
            print(self.dictMembersInfos[tcno])
            if not listBooksId :
                msg.popup_mesaj('Dikkat', "Hiç eser seçmediniz !  Lütfen önce verilecek eserleri seçiniz.\t\n")
            else:
                if verilebilir < len( listBooksId ):
                    msg.popup_mesaj('Dikkat', f"{memberName} isimli üye en fazla {verilebilir} kitap alabilir. \t\n\nLütfen sadece {verilebilir} kitap seçiniz!\n")
                else:
                    name    = f"{self.dictMembersInfos[tcno][2]}{5*' '}{self.dictMembersInfos[tcno][3]} {self.dictMembersInfos[tcno][4]}"
                    books   = '\n'.join( listBooksName)
                    answer, _ = msg.MesajBox("Dikkat", f"""Verilecek Eserler :\n{ books } \n\nAlan Üye\t:\n{name} \n\neser verme işlemini onaylıyor musunuz?\t\t\n""")
                    if answer:
                        for bookId in listBooksId:
                            db.insertData("EmanetTablosu",
                                          KitapId       = bookId,
                                          UyeId         = memberId,
                                          VerilisTarihi = datetime.today().date(),
                                          MaxKalmaSuresi= db.maxDayBooksStay        )
                            addedData += curs.rowcount
                        db.updateBookTableState( Durum=(0,)*len(listBooksId), kitapId=listBooksId)     # Durum=0 kitap müsait değil demek
                        self.clearSelection()
                        self.ui.le_searchBook.clear()
                        self.ui.le_searchMember.clear()
                        self.ui.statusbar.showMessage(f"{addedData} adet verilen kitap kaydı oluşturuldu", self.duration-10)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: giveBooksToMembers \t\tHata Kodu : {E}", self.duration)

    def addBookIdListOnDataDict(self, state):
        try:
            barcod = self.sender().objectName()
            if state:
                self.barkodList.append(barcod)
            else:
                if barcod in self.barkodList:
                    self.barkodList.remove(barcod)
            print("bookInfo ",self.dictBooksInfos[barcod])
            listBookId   = tuple(self.dictBooksInfos[b][0] for b in self.barkodList)
            listBookName = tuple(self.dictBooksInfos[b][2] for b in self.barkodList)
            self.selectedBooksDict["KitapId"] = listBookId
            self.selectedBooksDict["KitapAdi"] = listBookName
            print('self.selectedBooksDict: ', self.selectedBooksDict)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: addBookIdListOnDataDict \t\tHata Kodu : {E}", self.duration)

    def createCheckboxForTablewidget(self, bookData=[]):
        layout = QHBoxLayout()
        cBox = QCheckBox()
        cBox.setCheckState(False)
        barcodNo = bookData[1]
        self.dictBooksInfos[ barcodNo ] = bookData           # bookData[1] = Barkod number
        cBox.setObjectName( barcodNo )
        cBox.setMinimumSize(15, 15)
        cBox.clicked[bool].connect( self.addBookIdListOnDataDict )
        cBox.setMaximumSize(15, 15)
        cBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        layout.addWidget(cBox)
        widget = QWidget()
        widget.setLayout(layout)
        return widget

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
                        if index==0: item = item[6:]
                        self.ui.table_booksList.setItem(row,col,QTableWidgetItem(str(item)))
                        if col in (1,4):
                            self.ui.table_booksList.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table_booksList.resizeColumnsToContents()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksOnTablewidget     Hata Kodu : {E}", self.duration)

    def filterBooksOnTablewidget(self):
        try:
            ara = self.ui.le_searchBook.text()
            if self.ui.radio_barkod.isChecked()     : col = 1
            elif self.ui.radio_kitapAdi.isChecked() : col = 2
            elif self.ui.radio_isbn.isChecked()     : col = 4
            rows = self.ui.table_booksList.rowCount()
            for row in range(rows-self.numberOfBlankLines):
                item = self.ui.table_booksList.item(row,col)
                if item is not None:
                    if ara.lower() not in item.text().lower():
                        self.ui.table_booksList.hideRow(row)
                    else:
                        self.ui.table_booksList.showRow(row)
        except Exception as E:
            print(E)

    def filterMembersOnTablewidget(self) -> None:
        try:
            ara = self.ui.le_searchMember.text()
            if self.ui.radio_tc.isChecked():
                col = 5
            elif self.ui.radio_isim.isChecked():
                col = 3
            elif self.ui.radio_okulNo.isChecked():
                col = 2
            rows = self.ui.table_membersList.rowCount()
            for row in range(rows-self.numberOfBlankLines):
                item = self.ui.table_membersList.item(row,col)
                if item is not None:
                    if ara.lower() not in item.text().lower():
                        self.ui.table_membersList.hideRow(row)
                    else:
                        self.ui.table_membersList.showRow(row)
        except Exception as E:
            print(E)

    def showMembersInTablewidget(self) -> None:
        try:
            cols = ("uyeId", "OkulNo", f"{'Ad':^30}", f"{'Soyad':^15}", "TCNo", "Sinif", "Sube", "EldekiSayi")
            colLabels = ("Tıkla", 'Verilebilir', "Okul No", f"{'Ad':^35}", f"{'Soyad':^20}", f"{'TC Kimlik No':^20}", "Sınıf", "Şube")
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
            self.ui.table_membersList.resizeColumnsToContents()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showMembersInTablewidget \t\t Hata Kodu : {E}", self.duration)