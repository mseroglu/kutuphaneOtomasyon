# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/raporlar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 666)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_110 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_110.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_110.setObjectName("groupBox_110")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_110)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_due = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_due.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_due.setObjectName("btn_due")
        self.verticalLayout.addWidget(self.btn_due)
        self.btn_memberCards = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_memberCards.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_memberCards.setObjectName("btn_memberCards")
        self.verticalLayout.addWidget(self.btn_memberCards)
        self.btn_printAllBarkodes = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_printAllBarkodes.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_printAllBarkodes.setObjectName("btn_printAllBarkodes")
        self.verticalLayout.addWidget(self.btn_printAllBarkodes)
        self.btn_printQueuedUpBarkodes = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_printQueuedUpBarkodes.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_printQueuedUpBarkodes.setObjectName("btn_printQueuedUpBarkodes")
        self.verticalLayout.addWidget(self.btn_printQueuedUpBarkodes)
        self.btn_printMemberList = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_printMemberList.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_printMemberList.setObjectName("btn_printMemberList")
        self.verticalLayout.addWidget(self.btn_printMemberList)
        self.btn_printBookList_sortBarkodNumber = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_printBookList_sortBarkodNumber.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_printBookList_sortBarkodNumber.setObjectName("btn_printBookList_sortBarkodNumber")
        self.verticalLayout.addWidget(self.btn_printBookList_sortBarkodNumber)
        self.btn_printBookList_sortBookName = QtWidgets.QPushButton(self.groupBox_110)
        self.btn_printBookList_sortBookName.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_printBookList_sortBookName.setObjectName("btn_printBookList_sortBookName")
        self.verticalLayout.addWidget(self.btn_printBookList_sortBookName)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_110)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_110)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.horizontalLayout_3.addWidget(self.groupBox_110)
        self.groupBox_111 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_111.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_111.setObjectName("groupBox_111")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_111)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 345, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_111)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_111)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_111)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_111)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        spacerItem1 = QtWidgets.QSpacerItem(20, 345, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.groupBox_111)
        self.groupBox_112 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_112.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_112.setObjectName("groupBox_112")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_112)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 345, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_firstDate = QtWidgets.QDateEdit(self.groupBox_112)
        self.dateEdit_firstDate.setWrapping(True)
        self.dateEdit_firstDate.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_firstDate.setCalendarPopup(True)
        self.dateEdit_firstDate.setObjectName("dateEdit_firstDate")
        self.horizontalLayout.addWidget(self.dateEdit_firstDate)
        self.dateEdit_secondDate = QtWidgets.QDateEdit(self.groupBox_112)
        self.dateEdit_secondDate.setWrapping(True)
        self.dateEdit_secondDate.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_secondDate.setCalendarPopup(True)
        self.dateEdit_secondDate.setObjectName("dateEdit_secondDate")
        self.horizontalLayout.addWidget(self.dateEdit_secondDate)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_112)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_112)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_2.addWidget(self.pushButton_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 444, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.addWidget(self.groupBox_112)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Raporlar"))
        self.groupBox_110.setTitle(_translate("MainWindow", "Yazd??rma Se??enekleri"))
        self.btn_due.setText(_translate("MainWindow", "Teslim Zaman?? Gelenler"))
        self.btn_memberCards.setText(_translate("MainWindow", "??ye Kimlik Kartlar??"))
        self.btn_printAllBarkodes.setText(_translate("MainWindow", "T??m Barkodlar"))
        self.btn_printQueuedUpBarkodes.setText(_translate("MainWindow", "Kuyruktaki Barkodlar"))
        self.btn_printMemberList.setText(_translate("MainWindow", "??ye Listesi"))
        self.btn_printBookList_sortBarkodNumber.setText(_translate("MainWindow", "Eser Listesi (Barkod No S??ral??)"))
        self.btn_printBookList_sortBookName.setText(_translate("MainWindow", "Eser Listesi (Eser Ad?? S??ral??)"))
        self.pushButton_6.setText(_translate("MainWindow", "Elinde Eser Olan ??yeler"))
        self.pushButton_7.setText(_translate("MainWindow", "Eser Almayan ??yeler"))
        self.groupBox_111.setTitle(_translate("MainWindow", "Okuma ??statistikleri"))
        self.pushButton_9.setText(_translate("MainWindow", "En ??ok Okunan Eserler"))
        self.pushButton_10.setText(_translate("MainWindow", "En Az Okunan Eserler"))
        self.pushButton_11.setText(_translate("MainWindow", "En Az Okunan Yazarlar"))
        self.pushButton_12.setText(_translate("MainWindow", "En ??ok Okunan Yazarlar"))
        self.groupBox_112.setTitle(_translate("MainWindow", "Tarihleri aras??nda"))
        self.dateEdit_firstDate.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.dateEdit_secondDate.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.pushButton_14.setText(_translate("MainWindow", "Eser Alanlar"))
        self.pushButton_15.setText(_translate("MainWindow", "Geri Getirenler"))
