# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/uyeKayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(976, 593)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        Form.setFont(font)
        Form.setToolTip("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("QFrame { background-color: #5dcc7f;  border-radius: 5px }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_16 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.combo_memberType = QtWidgets.QComboBox(self.frame)
        self.combo_memberType.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_memberType.setFont(font)
        self.combo_memberType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combo_memberType.setObjectName("combo_memberType")
        self.combo_memberType.addItem("")
        self.combo_memberType.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_memberType)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_tcNo = QtWidgets.QLineEdit(self.frame)
        self.le_tcNo.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_tcNo.setFont(font)
        self.le_tcNo.setInputMask("")
        self.le_tcNo.setMaxLength(11)
        self.le_tcNo.setCursorPosition(0)
        self.le_tcNo.setClearButtonEnabled(True)
        self.le_tcNo.setObjectName("le_tcNo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_tcNo)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_studentNumber = QtWidgets.QLineEdit(self.frame)
        self.le_studentNumber.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_studentNumber.setFont(font)
        self.le_studentNumber.setInputMask("")
        self.le_studentNumber.setMaxLength(11)
        self.le_studentNumber.setObjectName("le_studentNumber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_studentNumber)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.le_name = QtWidgets.QLineEdit(self.frame)
        self.le_name.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setMaxLength(100)
        self.le_name.setObjectName("le_name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.le_lastname = QtWidgets.QLineEdit(self.frame)
        self.le_lastname.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_lastname.setFont(font)
        self.le_lastname.setMaxLength(100)
        self.le_lastname.setObjectName("le_lastname")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_lastname)
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.combo_sex = QtWidgets.QComboBox(self.frame)
        self.combo_sex.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_sex.setFont(font)
        self.combo_sex.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combo_sex.setObjectName("combo_sex")
        self.combo_sex.addItem("")
        self.combo_sex.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.combo_sex)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.dateEdit_birthDate = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_birthDate.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_birthDate.setFont(font)
        self.dateEdit_birthDate.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_birthDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 4, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_birthDate.setCalendarPopup(True)
        self.dateEdit_birthDate.setObjectName("dateEdit_birthDate")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dateEdit_birthDate)
        self.label_13 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.le_beMemberDate = QtWidgets.QLineEdit(self.frame)
        self.le_beMemberDate.setEnabled(False)
        self.le_beMemberDate.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_beMemberDate.setFont(font)
        self.le_beMemberDate.setAlignment(QtCore.Qt.AlignCenter)
        self.le_beMemberDate.setObjectName("le_beMemberDate")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.le_beMemberDate)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.le_phoneNumber = QtWidgets.QLineEdit(self.frame)
        self.le_phoneNumber.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_phoneNumber.setFont(font)
        self.le_phoneNumber.setInputMask("")
        self.le_phoneNumber.setText("")
        self.le_phoneNumber.setMaxLength(11)
        self.le_phoneNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_phoneNumber.setClearButtonEnabled(True)
        self.le_phoneNumber.setObjectName("le_phoneNumber")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.le_phoneNumber)
        self.label_15 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_sinif = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_sinif.sizePolicy().hasHeightForWidth())
        self.le_sinif.setSizePolicy(sizePolicy)
        self.le_sinif.setMinimumSize(QtCore.QSize(70, 0))
        self.le_sinif.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_sinif.setFont(font)
        self.le_sinif.setInputMask("")
        self.le_sinif.setMaxLength(2)
        self.le_sinif.setAlignment(QtCore.Qt.AlignCenter)
        self.le_sinif.setObjectName("le_sinif")
        self.horizontalLayout.addWidget(self.le_sinif)
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setMinimumSize(QtCore.QSize(30, 0))
        self.label_17.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.le_sube = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_sube.sizePolicy().hasHeightForWidth())
        self.le_sube.setSizePolicy(sizePolicy)
        self.le_sube.setMinimumSize(QtCore.QSize(70, 0))
        self.le_sube.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_sube.setFont(font)
        self.le_sube.setInputMask("")
        self.le_sube.setMaxLength(2)
        self.le_sube.setAlignment(QtCore.Qt.AlignCenter)
        self.le_sube.setObjectName("le_sube")
        self.horizontalLayout.addWidget(self.le_sube)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_18 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.combo_memberStatus = QtWidgets.QComboBox(self.frame)
        self.combo_memberStatus.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_memberStatus.setFont(font)
        self.combo_memberStatus.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combo_memberStatus.setObjectName("combo_memberStatus")
        self.combo_memberStatus.addItem("")
        self.combo_memberStatus.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.combo_memberStatus)
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.checkBox_uyeKartiYazdirma = QtWidgets.QCheckBox(self.frame)
        self.checkBox_uyeKartiYazdirma.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkBox_uyeKartiYazdirma.setChecked(True)
        self.checkBox_uyeKartiYazdirma.setObjectName("checkBox_uyeKartiYazdirma")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.checkBox_uyeKartiYazdirma)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_addImg = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addImg.sizePolicy().hasHeightForWidth())
        self.btn_addImg.setSizePolicy(sizePolicy)
        self.btn_addImg.setMinimumSize(QtCore.QSize(150, 200))
        self.btn_addImg.setMaximumSize(QtCore.QSize(150, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_addImg.setFont(font)
        self.btn_addImg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_addImg.setAutoFillBackground(False)
        self.btn_addImg.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../img/member.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addImg.setIcon(icon)
        self.btn_addImg.setIconSize(QtCore.QSize(150, 200))
        self.btn_addImg.setObjectName("btn_addImg")
        self.verticalLayout_2.addWidget(self.btn_addImg)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.table_members = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_members.sizePolicy().hasHeightForWidth())
        self.table_members.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_members.setFont(font)
        self.table_members.setStyleSheet("QTableWidget {border: 5px solid #5dcc7f; border-radius: 5px }")
        self.table_members.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table_members.setAlternatingRowColors(True)
        self.table_members.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_members.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_members.setObjectName("table_members")
        self.table_members.setColumnCount(6)
        self.table_members.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(5, item)
        self.table_members.horizontalHeader().setCascadingSectionResizes(True)
        self.table_members.horizontalHeader().setDefaultSectionSize(80)
        self.table_members.horizontalHeader().setMinimumSectionSize(30)
        self.table_members.horizontalHeader().setStretchLastSection(True)
        self.table_members.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.table_members)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout_2.addWidget(self.btn_del)
        self.btn_update = QtWidgets.QPushButton(Form)
        self.btn_update.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_2.addWidget(self.btn_update)
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.btn_getFromExcel = QtWidgets.QPushButton(Form)
        self.btn_getFromExcel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_getFromExcel.setFont(font)
        self.btn_getFromExcel.setObjectName("btn_getFromExcel")
        self.horizontalLayout_2.addWidget(self.btn_getFromExcel)
        self.btn_openSampleExcel = QtWidgets.QPushButton(Form)
        self.btn_openSampleExcel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openSampleExcel.setFont(font)
        self.btn_openSampleExcel.setObjectName("btn_openSampleExcel")
        self.horizontalLayout_2.addWidget(self.btn_openSampleExcel)
        self.btn_memberCard = QtWidgets.QPushButton(Form)
        self.btn_memberCard.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_memberCard.setFont(font)
        self.btn_memberCard.setObjectName("btn_memberCard")
        self.horizontalLayout_2.addWidget(self.btn_memberCard)
        self.btn_memberList = QtWidgets.QPushButton(Form)
        self.btn_memberList.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_memberList.setFont(font)
        self.btn_memberList.setObjectName("btn_memberList")
        self.horizontalLayout_2.addWidget(self.btn_memberList)
        self.btn_clear = QtWidgets.QPushButton(Form)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.combo_memberStatus.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Üye Kayıt"))
        self.label_16.setText(_translate("Form", "Üyelik Tipi"))
        self.combo_memberType.setItemText(0, _translate("Form", "Öğrenci"))
        self.combo_memberType.setItemText(1, _translate("Form", "Personel"))
        self.label_7.setText(_translate("Form", "TC Kimlik No"))
        self.label_8.setText(_translate("Form", "Okul No"))
        self.label_9.setText(_translate("Form", "Adı"))
        self.label_10.setText(_translate("Form", "Soyadı"))
        self.label_11.setText(_translate("Form", "Cinsiyet"))
        self.combo_sex.setItemText(0, _translate("Form", "Kadın"))
        self.combo_sex.setItemText(1, _translate("Form", "Erkek"))
        self.label_12.setText(_translate("Form", "Doğum Tarihi"))
        self.dateEdit_birthDate.setDisplayFormat(_translate("Form", "dd.MM.yyyy"))
        self.label_13.setText(_translate("Form", "Üyelik Tarihi"))
        self.label_14.setText(_translate("Form", "Telefon No"))
        self.label_15.setText(_translate("Form", "Sınıf / Şube"))
        self.label_17.setText(_translate("Form", " / "))
        self.label_18.setText(_translate("Form", "Üye Durumu"))
        self.combo_memberStatus.setItemText(0, _translate("Form", "Pasif"))
        self.combo_memberStatus.setItemText(1, _translate("Form", "Aktif"))
        self.label_19.setText(_translate("Form", "Üye Kartı"))
        self.checkBox_uyeKartiYazdirma.setText(_translate("Form", "Yazdırma kuyruğuna ekle"))
        self.btn_addImg.setToolTip(_translate("Form", "Resim Ekle"))
        self.table_members.setSortingEnabled(True)
        item = self.table_members.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.table_members.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.table_members.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.table_members.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.table_members.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.table_members.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Tc Kimlik No"))
        item = self.table_members.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Okul No"))
        item = self.table_members.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ad"))
        item = self.table_members.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Soyad"))
        item = self.table_members.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sınıfı"))
        item = self.table_members.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Şube"))
        self.btn_del.setText(_translate("Form", "Sil"))
        self.btn_update.setText(_translate("Form", "Güncelle"))
        self.btn_save.setText(_translate("Form", "Kaydet"))
        self.btn_getFromExcel.setText(_translate("Form", "Excel\'den Üye Kaydet"))
        self.btn_openSampleExcel.setText(_translate("Form", "Örnek Excel Sayfası"))
        self.btn_memberCard.setText(_translate("Form", "Üye Kartı"))
        self.btn_memberList.setText(_translate("Form", "Üye Listesi"))
        self.btn_clear.setText(_translate("Form", "Temizle"))
