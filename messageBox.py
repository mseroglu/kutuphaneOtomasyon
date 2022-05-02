from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

class MessageBox():

    def popup_mesaj(self, baslik="", mesaj="") -> None:
        try:
            mBox = QMessageBox()
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            mBox.setFont(font)
            mBox.setText(mesaj)
            mBox.setIcon(QMessageBox.Information)
            mBox.setWindowTitle(baslik)
            mBox.setWindowIcon(QtGui.QIcon("img/ayar.jpg"))
            mBox.setContentsMargins(10,5,10,5)
            mBox.setStandardButtons(QMessageBox.Ok)
            mBox.setEscapeButton(QMessageBox.Ok)         # x ile çıkıca hangi işlemi yapsın
            self.butonOk = mBox.button(QMessageBox.Ok)
            self.butonOk.setText("Tamam")
            mBox.setDefaultButton(self.butonOk)
            result = mBox.exec_()
        except Exception as E:
            print(f"mesaj fonk hatası  {E}")

    def MesajBox(self, baslik="BAŞLIK", mesaj="MESAJ", defaultButton=QMessageBox.No, icon=QMessageBox.Critical,
                   buttons=(QMessageBox.Yes | QMessageBox.No), textButtons={"b1":"Evet", "b2":"Hayır", "b3":"Evet (Formu Temizle)"}) -> tuple:
        mBox = QMessageBox()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        mBox.setFont(font)
        mBox.setIcon(icon)
        mBox.setWindowIcon(QtGui.QIcon("img/ayar.jpg"))
        mBox.setText(mesaj)
        mBox.setWindowTitle(baslik)
        mBox.setStandardButtons(buttons)
        mBox.setEscapeButton(QMessageBox.No)  # x ile çıkıca hangi işlemi yapsın
        mBox.setContentsMargins(10, 10, 10, 10)
        mBox.setDefaultButton(defaultButton)
        butonEvet = mBox.button(QMessageBox.Yes)
        butonEvet.setText(textButtons["b1"])
        butonHayir = mBox.button(QMessageBox.No)
        butonHayir.setText(textButtons["b2"])
        if len(mBox.buttons()) == 3:
            butonOk = mBox.button(QMessageBox.Ok)
            butonOk.setText(textButtons["b3"])

        result = mBox.exec_()
        if result == QMessageBox.Yes:
            return (True, False)
        elif result == QMessageBox.Ok:
            return (True, True)                       # ikinci True mesajBox kapandıktan sonra formun temizlenmesi için
        return (False, False)

msg = MessageBox()