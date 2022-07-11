import os, io

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5 import QtGui, QtCore
from ui.uyeKayitUI import Ui_MainWindow
from datetime import datetime
from messageBox import msg
from database import curs, db, tableWidgetResize
from PIL import Image


class SaveMember(QMainWindow):
    def __init__(self):
        super(SaveMember, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_addImg.setStyleSheet("QPushButton {border: None; background: transparent; border-radius: 20px }")
        self.memberPhotoData = None
        self.selectedIdForUpdate = None
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)      # hep üstte kalması için

        self.ui.btn_del.setVisible(False)
        self.ui.btn_update.setVisible(False)

        self.ui.le_beMemberDate.setText(datetime.now().strftime("%d.%m.%Y"))



        self.ui.btn_getFromExcel.clicked.connect(db.insertMembersDataFromExcel)
        self.ui.btn_getFromExcel.clicked.connect(self.showMembersInTablewidget)
        self.ui.btn_openSampleExcel.clicked.connect(self.openSampleExcelPage)
        self.ui.btn_save.clicked.connect(self.createNewMember)
        self.ui.btn_update.clicked.connect(self.updateMemberInfo)
        self.ui.table_members.currentItemChanged.connect(self.showMemberInfoInForm)
        self.ui.btn_del.clicked.connect(self.delMember)



        self.ui.btn_clear.clicked.connect(self.clearForm)
        self.ui.btn_addImg.clicked.connect(self.addMemberPhoto)



    def openSampleExcelPage(self):
        try:
            os.startfile("excel_pages")
        except Exception as E:
            print(f"Fonk: openSampleExcelPage   \tHata: {E} ")

    def showMemberPhoto(self, data):
        try:
            pixmap = "img/member.jpg"
            if data:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(data)
            self.ui.btn_addImg.setIcon( QtGui.QIcon(pixmap) )
            self.ui.btn_addImg.setStyleSheet("QPushButton {border-radius: 20px}")
            self.memberPhotoData = data
        except Exception as E:
            print(f"Fonk: showMemberPhoto   \tHata: {E} ")

    def addMemberPhoto(self):
        try:
            filePath, _ = QFileDialog.getOpenFileName(self, caption= "Fotoğraf Seçimi", filter= "Görsel (*.png *.jpeg *.jpg)")
            if filePath.endswith(".png") or filePath.endswith(".jpg") or filePath.endswith(".jpeg"):
                with Image.open(filePath) as resim:
                    resim = resim.resize( (150,200), Image.ANTIALIAS)
                    IO_Object = io.BytesIO()
                    resim.save(IO_Object, "png")
                    self.memberPhotoData = IO_Object.getvalue()
                self.showMemberPhoto(self.memberPhotoData)
        except Exception as E:
            print(f"Fonk: addMemberPhoto    Hata: {E}")

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        tableWidgetResize(self.ui.table_members, (3,2,4,2,1,1), blank=3)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.showMembersInTablewidget()
        self.resizeEvent(QtGui.QResizeEvent)

    def delMember(self):
        try:
            row     = self.ui.table_members.currentRow()
            tcno    = self.ui.table_members.item(row, 0).text()
            name    = self.ui.table_members.item(row,2).text()
            lastname = self.ui.table_members.item(row,3).text()
            bookData = db.checkBookEntrustState(TCNo=tcno)
            if bookData:
                msg.popup_mesaj("Silme işlemi başarısız", f"Barkod\t:  {bookData[0]}\n"
                                                          f"Kitap Adı\t:  {bookData[1]}\n"                                                          
                                                          f"Uye No\t:  {bookData[2]}\n"
                                                          f"Uye Adı\t:  {bookData[3]} {bookData[4]}\n\n"
                                                          f"Üye kitap ile eşleşiyor. Üyeyi silmek için önce üyedeki kitabı geri almalısınız")
                self.clearForm()
                return
            result, _ = msg.MesajBox("DİKKAT : Üye kaydı silinecek", f"{name+' '+lastname} isimli üyeyi silmek istiyor musunuz?")
            if result:
                db.delData("UyeTablosu", TCNo=tcno)
                if curs.rowcount>0:
                    msg.popup_mesaj('Silindi', "Üyenin kaydı silindi. Hadi hayırlı olsun. ;-)       ")
                self.showMembersInTablewidget()
                self.clearForm()
        except Exception as E:
            print(f"Fonk: delMember    Hata: {E}")

    def showMemberInfoInForm(self):
        try:
            self.ui.btn_del.setVisible(True)
            self.ui.btn_update.setVisible(True)
            self.ui.btn_save.setVisible(False)
            row     = self.ui.table_members.currentRow()
            tcno    = self.ui.table_members.item(row, 0).text()
            cameData = db.getMemberDataWithTcno(tcno)
            self.selectedIdForUpdate = cameData[0]
            self.ui.combo_memberType.setCurrentIndex( cameData[1] )
            self.ui.combo_memberStatus.setCurrentIndex( cameData[2] )
            self.ui.le_tcNo.setText( cameData[3] )
            self.ui.le_studentNumber.setText( cameData[4] )
            self.ui.le_name.setText( cameData[5] )
            self.ui.le_lastname.setText( cameData[6] )
            self.ui.combo_sex.setCurrentIndex( 0 if cameData[7] in (0,"0","Kız","Kadın","KIZ","KADIN") else 1 )
            self.ui.le_sinif.setText( str(cameData[8]) )
            self.ui.le_sube.setText( cameData[9] )
            y,m,d = cameData[11][:10].split("-")
            self.ui.dateEdit_birthDate.setDate(QtCore.QDate(int(y),int(m),int(d)))
            self.ui.le_beMemberDate.setText(datetime.strftime( datetime.strptime(cameData[12], "%Y-%m-%d"), '%d.%m.%Y'))
            self.showMemberPhoto( cameData[13] )
            self.ui.checkBox_uyeKartiYazdirma.setCheckState( cameData[14])
        except Exception as E:
            print(f"Fonk: showMemberInfoInForm    Hata: {E}")

    def showMembersInTablewidget(self):
        try:
            cols = ("TCNo", "OkulNo", "Ad", "Soyad", "Sinif", "Sube")
            self.ui.table_members.clearContents()
            cameData = db.getData("UyeTablosu", *cols)
            self.ui.table_members.setRowCount(len(cameData)+10)
            labels = ("TC Kimlik No", "Okul No", "Ad", "Soyad", "Sınıf", "Şube")
            self.ui.table_members.setColumnCount(len(labels))
            self.ui.table_members.setHorizontalHeaderLabels(labels)
            for row, uye in enumerate(cameData):
                for col, info in enumerate(uye):
                    self.ui.table_members.setItem(row,col,QTableWidgetItem(str(info)))
                    if col in (0,1,4,5):
                        self.ui.table_members.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.table_members.resizeColumnsToContents()
        except Exception as E:
            print(f"Fonk: showMembersInTablewidget    Hata: {E}")

    def getMemberInfo(self) -> dict:
        return {"UyeTipi"   : self.ui.combo_memberType.currentIndex(),
                "Durum"     : self.ui.combo_memberStatus.currentIndex(),
                "TCNo"      : self.ui.le_tcNo.text().strip(),
                "OkulNo"    : self.ui.le_studentNumber.text().strip(),
                "Ad"        : self.ui.le_name.text().strip().title(),
                "Soyad"     : self.ui.le_lastname.text().strip().title(),
                "Cinsiyet"  : self.ui.combo_sex.currentIndex(),
                "Sinif"     : self.ui.le_sinif.text().strip(),
                "Sube"      : self.ui.le_sube.text().strip().upper(),
                "Tel"       : self.ui.le_phoneNumber.text().strip(),
                "DogumTarihi": self.ui.dateEdit_birthDate.date().toPyDate(),
                "UyeKartiPrint": self.ui.checkBox_uyeKartiYazdirma.checkState(),
                "Photo"     : self.memberPhotoData
                }

    def updateMemberInfo(self):
        try:
            if not self.selectedIdForUpdate:
                msg.popup_mesaj("Dikkat", "Seçili bir üye yok, güncelleme yapmak için bir üyeyi çift tıklayınız ! ! !")
            else:
                cols_datas = self.getMemberInfo()
                if bool(cols_datas["TCNo"]) and bool(cols_datas['Ad']) and bool(cols_datas['Soyad']):
                    cols_datas["uyeId"] = self.selectedIdForUpdate
                    db.updateData(TableName="UyeTablosu", **cols_datas)
                    if curs.rowcount>0:
                        self.clearForm()
                        self.showMembersInTablewidget()
                else:
                    msg.popup_mesaj("Dikkat", "TC kimlik no, isim ve soyadı alanı boş olmamalıdır ! ! !")
        except Exception as E:
            print(E)

    def createNewMember(self) -> None:
        try:
            cols_datas = self.getMemberInfo()
            if bool(cols_datas["TCNo"]) and bool(cols_datas["Ad"]) and bool(cols_datas["Soyad"]):
                result, _ = msg.MesajBox("Yeni üye kaydı", f"{cols_datas['Ad']+' '+cols_datas['Soyad']} isimli üyeyi kaydetmek istiyor musunuz?")
                if result:
                    cols_datas["UyelikTarihi"] = datetime.now().date()
                    db.insertData(TableName="UyeTablosu", **cols_datas)
                    if curs.rowcount>0:
                        msg.popup_mesaj("Yeni üye kaydı", f"Yeni üye kaydı başarı ile yapılmıştır")
                        self.showMembersInTablewidget()
                    else:
                        msg.popup_mesaj("Başarısız ! ! !",
                                        "Kayıt yapılamadı ! Zaten kayıtlı bir 'TC Kimlik No' kullandınız !\n\n"
                                        "Güncelleme yapmayı deneyiniz... Yada farklı bir kimlik no giriniz.\n")
            else:
                msg.popup_mesaj("Dikkat", "TC kimlik no, isim ve soyadı alanı boş olmamalıdır ! ! !")
        except Exception as E:
            print(E)

    def clearForm(self):
        try:
            self.ui.combo_memberType.setCurrentIndex(0)
            self.ui.le_tcNo.clear()
            self.ui.le_studentNumber.clear()
            self.ui.le_name.clear()
            self.ui.le_lastname.clear()
            self.ui.combo_sex.setCurrentIndex(0)
            self.ui.le_sinif.clear()
            self.ui.le_sube.clear()
            self.ui.le_phoneNumber.clear()
            self.ui.le_beMemberDate.setText(datetime.now().strftime("%d.%m.%Y"))
            self.ui.checkBox_uyeKartiYazdirma.setCheckState(True)
            self.ui.btn_addImg.setIcon(QtGui.QIcon("img/member.jpg"))
            self.memberPhotoData = None
            self.selectedIdForUpdate = 0
            self.ui.btn_del.setVisible(False)
            self.ui.btn_update.setVisible(False)
            self.ui.btn_save.setVisible(True)
        except Exception as E:
            print(E)

    def today(self) -> datetime :                # dateEdit nesnesine vermek için
        bugun = datetime.now()
        print(bugun)
        date_ = QtCore.QDate(bugun.year, bugun.month, bugun.day)
        print(date_)
        return date_

