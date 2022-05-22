import locale
locale.setlocale(locale.LC_ALL, "")                                             # Yerel ayarları uygular
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5 import Qt, QtCore, QtGui
from ui.ayarlarUI import Ui_Form

from database import conn, curs, db
from messageBox import msg

class Settings_page(QWidget):
    def __init__(self):
        super(Settings_page, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)     # pencereyi en üstte tutuyor

        self.setWindowIcon(QtGui.QIcon("img/ayar.jpg"))
        self.duration = 15_000
        self.selectedUserId = None


        self.listAuthors()
        self.listCategories()
        self.listSections()
        self.listBookshelfs()
        self.showUserInfoInTablewidget()

        self.ui.btn_saveInstutionInfo.clicked.connect(self.saveSchoolInfos)

        self.ui.btn_userSave.clicked.connect(self.createNewUser )
        self.ui.btn_updateUser.clicked.connect(self.updateUser )
        self.ui.btn_delUser.clicked.connect(self.delUser)

        self.ui.btn_clear.clicked.connect(self.clearForm)


        self.ui.btn_addAuthor.clicked.connect(self.addNewAuthor)
        self.ui.btn_addCategori.clicked.connect(self.addNewCategory)
        self.ui.btn_addBookshelf.clicked.connect(self.addNewBookshelf)
        self.ui.btn_addSection.clicked.connect(self.addNewSection)
        self.ui.le_author.returnPressed.connect(self.addNewAuthor)
        self.ui.le_kategori.returnPressed.connect(self.addNewCategory)
        self.ui.le_bookshelf.returnPressed.connect(self.addNewBookshelf)
        self.ui.le_section.returnPressed.connect(self.addNewSection)

        self.ui.btn_delAuthor.clicked.connect(self.delAuthor)
        self.ui.btn_delCategori.clicked.connect(self.delCategory)
        self.ui.btn_delBookshelf.clicked.connect(self.delBookshelf)
        self.ui.btn_delSection.clicked.connect(self.delSection)

        self.ui.btn_levelup.clicked.connect(self.takeEveryoneToNextLevel)

        self.showInstitutionInfo()
        db.maxNumberOfBooksGiven = self.ui.spinBox_maxNumberOfBooksGiven.value()
        db.maxDayBooksStay = self.ui.spinBox_maxDayBooksStay.value()
        self.ui.spinBox_maxDayBooksStay.valueChanged.connect(self.whenMaxChanged)
        self.ui.spinBox_maxNumberOfBooksGiven.valueChanged.connect(self.whenMaxChanged)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        pass


    def whenMaxChanged(self):
        db.maxDayBooksStay  = self.ui.spinBox_maxDayBooksStay.value()
        db.maxNumberOfBooksGiven = self.ui.spinBox_maxNumberOfBooksGiven.value()
        db.updateSchoolInfo(maxCount= db.maxNumberOfBooksGiven, maxDay  = db.maxDayBooksStay)

    def takeEveryoneToNextLevel(self):
        try:
            mezunSinif = self.ui.combo_chooseGrade.currentIndex()
            if not mezunSinif:
                msg.popup_mesaj("Mezun sınıf seçimi yapılmadı",
                                "\nMezun olacak bir sınıf seçmelisiniz ! ! !    \n\nMezun öğrenciler pasif duruma gelir.\n\n")
            else:
                cevap = msg.MesajBox("Dikkat", f"{mezunSinif}. sınıflar mezun olacak ve pasif duruma düşecektir.    \n\n"
                                     "Diğer sınıflar bir üst sınıfa geçirilecektir.\n\n"
                                     "Bu işlem geri alınamaz. Yapmak istediğinize emin misiniz?        \n" )
                if cevap[0]:
                    sql = f"""UPDATE UyeTablosu SET Sinif=Sinif+1, Durum=(CASE WHEN Sinif={mezunSinif} THEN 0 ELSE 1 END) WHERE UyeTipi=0 AND Durum=1"""
                    curs.execute( sql )
                    conn.commit()
                    if curs.rowcount:
                        msg.popup_mesaj("İşlem tamamdır", f"{curs.rowcount} öğrenci bir üst sınıfa geçirildi    ")
                    else:
                        msg.popup_mesaj("İşlem başarısız !", f"Sınıf atlatma işlemi başarısız oldu ! ! !    ")
        except Exception as E:
            print(E)

    def showUserInfoInForm(self):
        try:
            row      = self.ui.tableWidget.currentItem().row()
            userData = self.ui.tableWidget.item(row, 2).data(QtCore.Qt.UserRole)[3:]
            self.selectedUserId = userData[0]
            self.ui.combo_userType.setCurrentIndex(userData[1])
            self.ui.le_tcno.setText(userData[2])
            self.ui.le_studentNumber.setText(userData[3])
            self.ui.le_name.setText(userData[4])
            self.ui.le_lastname.setText(userData[5])
            self.ui.le_sinif.setText(userData[6])
            self.ui.le_sube.setText(userData[7])
            self.ui.le_username.setText(userData[8])
            self.ui.le_password.setText(userData[9])
            self.ui.combo_userState.setCurrentIndex(userData[10])
        except Exception as E:
            print(f"Fonk: showUserInfoInForm \tHata Kodu : {E}")

    def showUserInfoInTablewidget(self) -> None :
        try:
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.itemDoubleClicked.connect(self.clickedTablewidgetItemForChangeUserState)
            self.ui.tableWidget.itemClicked.connect(self.showUserInfoInForm)
            data = db.getUserInfoWithCase()
            for row, rowData in enumerate(data):
                for col, colData in enumerate(rowData[:3]):
                    self.ui.tableWidget.setItem(row, col,QTableWidgetItem(colData))
                    if col==2:
                        self.ui.tableWidget.item(row,col).setData(QtCore.Qt.UserRole, rowData)
        except Exception as E:
            print(f"Fonk: showUserInfoInTablewidget \tHata Kodu : {E}")

    def clickedTablewidgetItemForChangeUserState(self, item):
        try:
            userInfo = item.data(QtCore.Qt.UserRole)
            if userInfo is not None:
                db.updateUserState(Durum=userInfo[2], Username=userInfo[0])
                self.showUserInfoInTablewidget()
        except Exception as E:
            print(f"Fonk: clickedTablewidgetItemForChangeUserState \tHata Kodu : {E}")

    def showInstitutionInfo(self) -> None:
        try:
            cameInfo = db.getData("OkulBilgiTablosu", "*")[0]
            self.ui.le_institutionCode.setText(cameInfo[1])
            self.ui.le_institutionCode.setEnabled(False)
            self.ui.le_institutionName.setText(cameInfo[2])
            self.ui.le_institutionName.setEnabled(False)
            self.ui.btn_saveInstutionInfo.setEnabled(False)
            self.ui.spinBox_maxNumberOfBooksGiven.setValue(cameInfo[3])
            self.ui.spinBox_maxDayBooksStay.setValue(cameInfo[4])
        except Exception as E:
            mesaj = msg.MesajBox("Dikkat", "Kurum bilgilerini kaydetmeniz gerekmektedir")
            if mesaj[0]:
                self.show()

    def saveSchoolInfos(self) -> None:
        try:
            curs.execute(F"SELECT COUNT(*) FROM OkulBilgiTablosu")
            if not curs.fetchone()[0]:
                infoDict = self.getSchoolInfo()
                if infoDict["KurumKodu"] and infoDict["OkulAdi"]:
                    cevap = msg.MesajBox("Dikkat",
                                          "Kurum bilgileri kaydedildikten sonra değiştirilemez. \n\n" 
                                          "Kaydetmek istediğinizden emin misiniz? \n")
                    if cevap[0]:
                        db.insertData(TableName="OkulBilgiTablosu", **infoDict)
                else:
                    msg.popup_mesaj("Dikkat", "Kurum bilgileri boş olamaz !!!")
        except Exception as E:
            print(E)

    def getSchoolInfo(self) -> dict:
        return {"KurumKodu"         : self.ui.le_institutionCode.text().strip(),
                "OkulAdi"           : self.ui.le_institutionName.text().strip().title(),
                "MaxCount"          : self.ui.spinBox_maxNumberOfBooksGiven.value(),
                "MaxDay"            : self.ui.spinBox_maxDayBooksStay.value()}

    def getUserInfo(self) -> dict:
        return {"GorevliTipi":self.ui.combo_userType.currentIndex(),
                "TCNo"      : self.ui.le_tcno.text().strip(),
                "OkulNo"    : self.ui.le_studentNumber.text().strip(),
                "Ad"        : self.ui.le_name.text().strip().title(),
                "Soyad"     : self.ui.le_lastname.text().strip().title(),
                "Sinif"     : self.ui.le_sinif.text().strip(),
                "Sube"      : self.ui.le_sube.text().strip().upper(),
                "Username"  : self.ui.le_username.text().strip(),
                "Password"  : self.ui.le_password.text().strip(),
                "Durum"     : self.ui.combo_userState.currentIndex()}

    def updateUser(self) -> None :
        try:
            if self.selectedUserId:
                cols_datas = self.getUserInfo()
                cols_datas['gorevliId'] = self.selectedUserId
                db.updateData(TableName="GorevliTablosu", **cols_datas)
                self.showUserInfoInTablewidget()
                self.clearForm()
            else:
                msg.popup_mesaj("Dikkat", "Güncellenecek kullanıcı verisi yok !\t")
        except Exception as E:
            print(E)

    def delUser(self):
        try:
            if self.selectedUserId:
                result, _ = msg.MesajBox("DİKKAT : Kullanıcı silinecek",
                                         f"Seçili kullanıcıyı silmek istediğinizden emin misiniz?\t\t\n")
                if result:
                    db.delData("GorevliTablosu", gorevliId=self.selectedUserId)
                    if curs.rowcount > 0:
                        msg.popup_mesaj('Silindi', "Kullanıcı silindi. Hadi hayırlı olsun. ;-)\t\n")
                    self.showUserInfoInTablewidget()
                    self.clearForm()
            else:
                msg.popup_mesaj('Seçim yapılmadı', f'Silinecek kullanıcıyı seçmediniz. \t\t\n')
        except Exception as E:
            print(f"Fonk: delUser \t\t Hata Kodu : {E}")

    def createNewUser(self) -> None :
        try:
            cols_datas = self.getUserInfo()
            db.insertData(TableName="GorevliTablosu", **cols_datas)
            if curs.rowcount>0:
                title,mesaj = ("Yeni kullanıcı", "Yeni kullanıcı oluşturma işlemi başarılı...\t\t\n")
                self.showUserInfoInTablewidget()
                self.clearForm()
            else:
                title, mesaj = ("Dikkat : İşlem başarısız", "İşlem başarısız. Yeni kullanıcı oluşturulamadı !\n\n"
                                                            "Kullanıcı adı veya TC Kimlik No daha önce kullanılmış.\t\n")
            msg.popup_mesaj(title, mesaj)
        except Exception as E:
            print(E)

    def addNewAuthor(self) -> None:
        try:
            cols_datas = {"YazarAdi": self.ui.le_author.text().strip().title()}
            db.insertData("YazarTablosu", **cols_datas)
            self.ui.le_author.clear()
            self.listAuthors()
        except Exception as E:
            print(f"Fonk: addNewAuthor  \t\tHata Kodu : {E}", self.duration)

    def addNewCategory(self) -> None:
        cols_datas = {"Kategori": self.ui.le_kategori.text().strip().capitalize()}
        db.insertData("KategoriTablosu", **cols_datas)
        self.ui.le_kategori.clear()
        self.listCategories()

    def addNewSection(self) -> None:
        cols_datas = {"Bolum": self.ui.le_section.text().strip().capitalize()}
        db.insertData("BolumTablosu", **cols_datas)
        self.ui.le_section.clear()
        self.listSections()

    def addNewBookshelf(self) -> None:
        cols_datas = {"RafNo": self.ui.le_bookshelf.text().strip().capitalize()}
        db.insertData("RafTablosu", **cols_datas)
        self.ui.le_bookshelf.clear()
        self.listBookshelfs()

    def delAuthor(self):
        cols_datas = {"YazarAdi": self.ui.list_author.currentItem().text()}
        db.delData("YazarTablosu", **cols_datas)
        self.listAuthors()

    def delCategory(self):
        cols_datas = {"Kategori": self.ui.list_categories.currentItem().text()}
        db.delData("KategoriTablosu", **cols_datas)
        self.listCategories()

    def delSection(self) -> None:
        cols_datas = {"Bolum": self.ui.list_section.currentItem().text()}
        db.delData("BolumTablosu", **cols_datas)
        self.listSections()

    def delBookshelf(self) -> None:
        cols_datas = {"RafNo": self.ui.list_bookshelf.currentItem().text()}
        db.delData("RafTablosu", **cols_datas)
        self.listBookshelfs()

    def listAuthors(self) -> None:
        self.ui.list_author.clear()
        try:
            authors = db.getDataWithOrderBy("YazarTablosu", "YazarAdi")
            for item in authors:
                self.ui.list_author.addItem( item[0] )
        except Exception as E:
            print(E)

    def listCategories(self) -> None:
        self.ui.list_categories.clear()
        try:
            categories = db.getDataWithOrderBy("KategoriTablosu", "Kategori")
            for item in categories:
                self.ui.list_categories.addItem( item[0] )
        except Exception as E:
            print(E)

    def listSections(self) -> None:
        self.ui.list_section.clear()
        try:
            sections = db.getDataWithOrderBy("BolumTablosu", "Bolum")
            for item in sections:
                self.ui.list_section.addItem( item[0] )
        except Exception as E:
            print(E)

    def listBookshelfs(self) -> None:
        self.ui.list_bookshelf.clear()
        try:
            bookshelfs = db.getDataWithOrderBy("RafTablosu", "RafNo")
            for item in bookshelfs:
                self.ui.list_bookshelf.addItem( item[0] )
        except Exception as E:
            print(E)

    def clearForm(self) -> None:
        try:
            self.ui.combo_userType.setCurrentIndex(0)
            self.ui.le_tcno.clear()
            self.ui.le_studentNumber.clear()
            self.ui.le_name.clear()
            self.ui.le_lastname.clear()
            self.ui.le_sinif.clear()
            self.ui.le_sube.clear()
            self.ui.le_username.clear()
            self.ui.le_password.clear()
            self.selectedUserId = None
        except Exception as E:
            print(E)





