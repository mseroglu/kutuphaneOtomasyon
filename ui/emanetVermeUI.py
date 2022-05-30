# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/emanetVerme.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 600)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{background-color: #6fb4b8; color:white; padding:10px; border-radius: 5px; font-size: 11pt }")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_iadeTarihi = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_iadeTarihi.sizePolicy().hasHeightForWidth())
        self.label_iadeTarihi.setSizePolicy(sizePolicy)
        self.label_iadeTarihi.setMinimumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_iadeTarihi.setFont(font)
        self.label_iadeTarihi.setStyleSheet("QLabel{background-color: rgba(66,146,157,255); color:white; padding:10px; border-radius: 5px; font-size: 12pt}")
        self.label_iadeTarihi.setScaledContents(False)
        self.label_iadeTarihi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_iadeTarihi.setOpenExternalLinks(False)
        self.label_iadeTarihi.setObjectName("label_iadeTarihi")
        self.verticalLayout_4.addWidget(self.label_iadeTarihi)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(233, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_okulNo = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_okulNo.setFont(font)
        self.radio_okulNo.setChecked(True)
        self.radio_okulNo.setObjectName("radio_okulNo")
        self.horizontalLayout.addWidget(self.radio_okulNo)
        self.radio_tc = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_tc.setFont(font)
        self.radio_tc.setObjectName("radio_tc")
        self.horizontalLayout.addWidget(self.radio_tc)
        self.radio_isim = QtWidgets.QRadioButton(self.groupBox)
        self.radio_isim.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_isim.setFont(font)
        self.radio_isim.setObjectName("radio_isim")
        self.horizontalLayout.addWidget(self.radio_isim)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.le_searchMember = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchMember.sizePolicy().hasHeightForWidth())
        self.le_searchMember.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchMember.setFont(font)
        self.le_searchMember.setClearButtonEnabled(True)
        self.le_searchMember.setObjectName("le_searchMember")
        self.horizontalLayout_5.addWidget(self.le_searchMember)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(40, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui\\../img/kisiler3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.table_membersList = QtWidgets.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_membersList.setFont(font)
        self.table_membersList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.table_membersList.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table_membersList.setAlternatingRowColors(True)
        self.table_membersList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_membersList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_membersList.setObjectName("table_membersList")
        self.table_membersList.setColumnCount(0)
        self.table_membersList.setRowCount(0)
        self.table_membersList.horizontalHeader().setDefaultSectionSize(50)
        self.table_membersList.horizontalHeader().setMinimumSectionSize(20)
        self.table_membersList.horizontalHeader().setStretchLastSection(True)
        self.table_membersList.verticalHeader().setVisible(False)
        self.table_membersList.verticalHeader().setDefaultSectionSize(40)
        self.table_membersList.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.table_membersList)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio_kitapAdi = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_kitapAdi.setFont(font)
        self.radio_kitapAdi.setObjectName("radio_kitapAdi")
        self.horizontalLayout_2.addWidget(self.radio_kitapAdi)
        self.radio_isbn = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_isbn.setFont(font)
        self.radio_isbn.setObjectName("radio_isbn")
        self.horizontalLayout_2.addWidget(self.radio_isbn)
        self.radio_barkod = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_barkod.setFont(font)
        self.radio_barkod.setChecked(True)
        self.radio_barkod.setObjectName("radio_barkod")
        self.horizontalLayout_2.addWidget(self.radio_barkod)
        self.btn_clearSelection = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_clearSelection.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_clearSelection.setObjectName("btn_clearSelection")
        self.horizontalLayout_2.addWidget(self.btn_clearSelection)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.le_searchBook = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchBook.sizePolicy().hasHeightForWidth())
        self.le_searchBook.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchBook.setFont(font)
        self.le_searchBook.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.le_searchBook.setClearButtonEnabled(True)
        self.le_searchBook.setObjectName("le_searchBook")
        self.horizontalLayout_6.addWidget(self.le_searchBook)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMaximumSize(QtCore.QSize(50, 30))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui\\../img/barcodOkut.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.table_booksList = QtWidgets.QTableWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_booksList.setFont(font)
        self.table_booksList.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table_booksList.setAlternatingRowColors(True)
        self.table_booksList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_booksList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_booksList.setObjectName("table_booksList")
        self.table_booksList.setColumnCount(0)
        self.table_booksList.setRowCount(0)
        self.table_booksList.horizontalHeader().setDefaultSectionSize(50)
        self.table_booksList.horizontalHeader().setMinimumSectionSize(20)
        self.table_booksList.horizontalHeader().setStretchLastSection(True)
        self.table_booksList.verticalHeader().setVisible(False)
        self.table_booksList.verticalHeader().setDefaultSectionSize(40)
        self.table_booksList.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_2.addWidget(self.table_booksList)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("QLabel{background-color: #6fb4b8 ;color:white; padding:10px; border-radius: 5px; font-size: 11pt }")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_verilisTarihi = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_verilisTarihi.sizePolicy().hasHeightForWidth())
        self.label_verilisTarihi.setSizePolicy(sizePolicy)
        self.label_verilisTarihi.setMinimumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_verilisTarihi.setFont(font)
        self.label_verilisTarihi.setStyleSheet("QLabel{background-color: rgba(66,146,157,255); color:white; padding:10px; border-radius: 5px; font-size: 12pt}")
        self.label_verilisTarihi.setScaledContents(False)
        self.label_verilisTarihi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_verilisTarihi.setOpenExternalLinks(False)
        self.label_verilisTarihi.setObjectName("label_verilisTarihi")
        self.verticalLayout_3.addWidget(self.label_verilisTarihi)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ver"))
        self.label_4.setText(_translate("MainWindow", "İade Tarihi"))
        self.label_iadeTarihi.setText(_translate("MainWindow", "20 Nisan 2022"))
        self.radio_okulNo.setText(_translate("MainWindow", "Okul No"))
        self.radio_tc.setText(_translate("MainWindow", "TC Kimlik No"))
        self.radio_isim.setText(_translate("MainWindow", "İsim"))
        self.radio_kitapAdi.setText(_translate("MainWindow", "Kitap Adı"))
        self.radio_isbn.setText(_translate("MainWindow", "ISBN"))
        self.radio_barkod.setText(_translate("MainWindow", "Barkod"))
        self.btn_clearSelection.setText(_translate("MainWindow", "Seçimi Temizle"))
        self.label_2.setText(_translate("MainWindow", "Veriliş Tarihi "))
        self.label_verilisTarihi.setText(_translate("MainWindow", "06 Nisan 2022"))
