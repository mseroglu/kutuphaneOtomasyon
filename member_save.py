from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtGui, QtCore
from ui.uyeKayitUI import Ui_Form
from datetime import datetime
from messageBox import msg
from database import conn, curs, db

class SaveMember(QWidget):
    def __init__(self):
        super(SaveMember, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)      # hep üstte kalması için



        self.ui.btn_saveMembers.clicked.connect(db.insertMembersDataFromExcel)
        self.ui.btn_saveMembers.clicked.connect(self.showMembersInTablewidget)
        self.ui.btn_save.clicked.connect(self.createNewMember)
        self.ui.btn_update.clicked.connect(self.updateMemberInfo)
        self.ui.table_members.itemDoubleClicked.connect(self.showMemberInfoInForm)
        self.ui.btn_del.clicked.connect(self.delMember)


        self.ui.btn_clear.clicked.connect(self.clearForm)


    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.showMembersInTablewidget()

    def dosyadan_aktar(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Dosyadan al", self.filePath, "Excel Belgesi (*.xls *.xlsx)")
            self.filePath = "/".join(file_path.split("/")[:(len(file_path.split("/"))-1)])   # son açılan dosya konumu hatırlamak için
            if file_path.endswith("xls") or file_path.endswith("xlsx"):
                # todo
                pass
        except Exception as E:
            self.ui.statusbar.showMessage(f"FONK: dosyadan_aktar HATA KODU : {E}")

    def delMember(self):
        try:
            row     = self.ui.table_members.currentRow()
            tcno    = self.ui.table_members.item(row, 0).text()
            name    = self.ui.table_members.item(row,2).text()
            lastname = self.ui.table_members.item(row,3).text()
            result, _ = msg.MesajBox("DİKKAT : Üye kaydı silinecek", f"{name+' '+lastname} isimli üyeyi silmek istiyor musunuz?")
            if result:
                db.delData("UyeTablosu", TCNo=tcno)
                if curs.rowcount>0:
                    msg.popup_mesaj('Silindi', "Üyenin kaydı silindi. Hadi hayırlı olsun. ;-)       ")
                self.showMembersInTablewidget()
        except Exception as E:
            print(E)

    def showMemberInfoInForm(self):
        try:
            row     = self.ui.table_members.currentRow()
            tcno    = self.ui.table_members.item(row, 0).text()
            cameData = db.getMemberDataWithTcno(tcno)
            print(cameData)
            self.selectedIdForUpdate = cameData[0][0]
            self.ui.combo_memberType.setCurrentIndex( cameData[0][1] )
            self.ui.combo_memberStatus.setCurrentIndex( cameData[0][2] )
            self.ui.le_tcNo.setText( cameData[0][3] )
            self.ui.le_studentNumber.setText( cameData[0][4] )
            self.ui.le_name.setText( cameData[0][5] )
            self.ui.le_lastname.setText( cameData[0][6] )
            self.ui.combo_sex.setCurrentIndex( 0 if cameData[0][7] in (0,"0","Kız","Kadın","KIZ","KADIN") else 1 )
            self.ui.le_sinif.setText( str(cameData[0][8]) )
            self.ui.le_sube.setText( cameData[0][9] )
            y,m,d = cameData[0][11][:10].split("-")
            self.ui.dateEdit_birthDate.setDate(QtCore.QDate(int(y),int(m),int(d)))
            self.ui.le_beMemberDate.setText(datetime.strftime( datetime.strptime(cameData[0][12], "%Y-%m-%d"), '%d.%m.%Y'))
        except Exception as E:
            print(E)

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
            print(E)

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
                "DogumTarihi": self.ui.dateEdit_birthDate.date().toPyDate()
                }

    def updateMemberInfo(self):
        try:
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
            self.ui.le_phoneNumber.setText("0")
            self.ui.le_beMemberDate.clear()
        except Exception as E:
            print(E)

    def today(self) -> datetime :                # dateEdit nesnesine vermek için
        bugun = datetime.now()
        print(bugun)
        date_ = QtCore.QDate(bugun.year, bugun.month, bugun.day)
        print(date_)
        return date_

