# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/anasayfa2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 600)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_side = QtWidgets.QFrame(self.centralwidget)
        self.frame_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_side.setObjectName("frame_side")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_side)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_openTransactions = QtWidgets.QPushButton(self.frame_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openTransactions.sizePolicy().hasHeightForWidth())
        self.btn_openTransactions.setSizePolicy(sizePolicy)
        self.btn_openTransactions.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openTransactions.setFont(font)
        self.btn_openTransactions.setObjectName("btn_openTransactions")
        self.verticalLayout_2.addWidget(self.btn_openTransactions)
        self.btn_openMemberSave = QtWidgets.QPushButton(self.frame_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openMemberSave.sizePolicy().hasHeightForWidth())
        self.btn_openMemberSave.setSizePolicy(sizePolicy)
        self.btn_openMemberSave.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openMemberSave.setFont(font)
        self.btn_openMemberSave.setObjectName("btn_openMemberSave")
        self.verticalLayout_2.addWidget(self.btn_openMemberSave)
        self.btn_openSaveBook = QtWidgets.QPushButton(self.frame_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openSaveBook.sizePolicy().hasHeightForWidth())
        self.btn_openSaveBook.setSizePolicy(sizePolicy)
        self.btn_openSaveBook.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openSaveBook.setFont(font)
        self.btn_openSaveBook.setObjectName("btn_openSaveBook")
        self.verticalLayout_2.addWidget(self.btn_openSaveBook)
        self.btn_openReports = QtWidgets.QPushButton(self.frame_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openReports.sizePolicy().hasHeightForWidth())
        self.btn_openReports.setSizePolicy(sizePolicy)
        self.btn_openReports.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openReports.setFont(font)
        self.btn_openReports.setObjectName("btn_openReports")
        self.verticalLayout_2.addWidget(self.btn_openReports)
        self.btn_openSettings = QtWidgets.QPushButton(self.frame_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openSettings.sizePolicy().hasHeightForWidth())
        self.btn_openSettings.setSizePolicy(sizePolicy)
        self.btn_openSettings.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_openSettings.setFont(font)
        self.btn_openSettings.setObjectName("btn_openSettings")
        self.verticalLayout_2.addWidget(self.btn_openSettings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_quit = QtWidgets.QPushButton(self.frame_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy)
        self.btn_quit.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_quit.setFont(font)
        self.btn_quit.setObjectName("btn_quit")
        self.verticalLayout_2.addWidget(self.btn_quit)
        self.horizontalLayout.addWidget(self.frame_side)
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_header = QtWidgets.QGroupBox(self.frame_main)
        self.groupBox_header.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_header.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_header.setTitle("")
        self.groupBox_header.setFlat(False)
        self.groupBox_header.setObjectName("groupBox_header")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_header)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 30, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_searchBarcode = QtWidgets.QLineEdit(self.groupBox_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchBarcode.sizePolicy().hasHeightForWidth())
        self.le_searchBarcode.setSizePolicy(sizePolicy)
        self.le_searchBarcode.setMinimumSize(QtCore.QSize(0, 25))
        self.le_searchBarcode.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchBarcode.setFont(font)
        self.le_searchBarcode.setMaxLength(8)
        self.le_searchBarcode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_searchBarcode.setDragEnabled(True)
        self.le_searchBarcode.setClearButtonEnabled(True)
        self.le_searchBarcode.setObjectName("le_searchBarcode")
        self.horizontalLayout_4.addWidget(self.le_searchBarcode)
        self.label_barcodeRead = QtWidgets.QLabel(self.groupBox_header)
        self.label_barcodeRead.setMaximumSize(QtCore.QSize(40, 30))
        self.label_barcodeRead.setText("")
        self.label_barcodeRead.setPixmap(QtGui.QPixmap("ui\\../img/barcodOkut.png"))
        self.label_barcodeRead.setScaledContents(True)
        self.label_barcodeRead.setObjectName("label_barcodeRead")
        self.horizontalLayout_4.addWidget(self.label_barcodeRead)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.label_logo = QtWidgets.QLabel(self.groupBox_header)
        self.label_logo.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("ui\\../img/logo.jpg"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setIndent(-1)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_6.addWidget(self.label_logo)
        self.verticalLayout.addWidget(self.groupBox_header)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_main)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_books = QtWidgets.QWidget()
        self.tab_books.setObjectName("tab_books")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_books)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_searchBook = QtWidgets.QPushButton(self.tab_books)
        self.btn_searchBook.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../img/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_searchBook.setIcon(icon)
        self.btn_searchBook.setIconSize(QtCore.QSize(24, 24))
        self.btn_searchBook.setCheckable(True)
        self.btn_searchBook.setObjectName("btn_searchBook")
        self.horizontalLayout_5.addWidget(self.btn_searchBook)
        self.le_searchBook = QtWidgets.QLineEdit(self.tab_books)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchBook.sizePolicy().hasHeightForWidth())
        self.le_searchBook.setSizePolicy(sizePolicy)
        self.le_searchBook.setMinimumSize(QtCore.QSize(0, 25))
        self.le_searchBook.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchBook.setFont(font)
        self.le_searchBook.setObjectName("le_searchBook")
        self.horizontalLayout_5.addWidget(self.le_searchBook)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.table_bookList = QtWidgets.QTableWidget(self.tab_books)
        self.table_bookList.setObjectName("table_bookList")
        self.table_bookList.setColumnCount(0)
        self.table_bookList.setRowCount(0)
        self.table_bookList.horizontalHeader().setStretchLastSection(True)
        self.table_bookList.verticalHeader().setDefaultSectionSize(40)
        self.table_bookList.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_4.addWidget(self.table_bookList)
        self.tabWidget.addTab(self.tab_books, "")
        self.tab_members = QtWidgets.QWidget()
        self.tab_members.setObjectName("tab_members")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_members)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_searchMember = QtWidgets.QPushButton(self.tab_members)
        self.btn_searchMember.setText("")
        self.btn_searchMember.setIcon(icon)
        self.btn_searchMember.setIconSize(QtCore.QSize(24, 24))
        self.btn_searchMember.setCheckable(True)
        self.btn_searchMember.setObjectName("btn_searchMember")
        self.horizontalLayout_3.addWidget(self.btn_searchMember)
        self.le_searchMember = QtWidgets.QLineEdit(self.tab_members)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchMember.sizePolicy().hasHeightForWidth())
        self.le_searchMember.setSizePolicy(sizePolicy)
        self.le_searchMember.setMinimumSize(QtCore.QSize(0, 25))
        self.le_searchMember.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchMember.setFont(font)
        self.le_searchMember.setObjectName("le_searchMember")
        self.horizontalLayout_3.addWidget(self.le_searchMember)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.table_memberList = QtWidgets.QTableWidget(self.tab_members)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_memberList.setFont(font)
        self.table_memberList.setAlternatingRowColors(True)
        self.table_memberList.setObjectName("table_memberList")
        self.table_memberList.setColumnCount(0)
        self.table_memberList.setRowCount(0)
        self.table_memberList.horizontalHeader().setStretchLastSection(False)
        self.table_memberList.verticalHeader().setDefaultSectionSize(40)
        self.table_memberList.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_3.addWidget(self.table_memberList)
        self.tabWidget.addTab(self.tab_members, "")
        self.tab_givenToday = QtWidgets.QWidget()
        self.tab_givenToday.setObjectName("tab_givenToday")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_givenToday)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_searchGivenToday = QtWidgets.QPushButton(self.tab_givenToday)
        self.btn_searchGivenToday.setText("")
        self.btn_searchGivenToday.setIcon(icon)
        self.btn_searchGivenToday.setIconSize(QtCore.QSize(24, 24))
        self.btn_searchGivenToday.setCheckable(True)
        self.btn_searchGivenToday.setObjectName("btn_searchGivenToday")
        self.horizontalLayout_2.addWidget(self.btn_searchGivenToday)
        self.le_searchGivenToday = QtWidgets.QLineEdit(self.tab_givenToday)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchGivenToday.sizePolicy().hasHeightForWidth())
        self.le_searchGivenToday.setSizePolicy(sizePolicy)
        self.le_searchGivenToday.setMinimumSize(QtCore.QSize(0, 25))
        self.le_searchGivenToday.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchGivenToday.setFont(font)
        self.le_searchGivenToday.setObjectName("le_searchGivenToday")
        self.horizontalLayout_2.addWidget(self.le_searchGivenToday)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.table_givenToday = QtWidgets.QTableWidget(self.tab_givenToday)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_givenToday.setFont(font)
        self.table_givenToday.setAlternatingRowColors(True)
        self.table_givenToday.setObjectName("table_givenToday")
        self.table_givenToday.setColumnCount(0)
        self.table_givenToday.setRowCount(0)
        self.table_givenToday.horizontalHeader().setStretchLastSection(False)
        self.table_givenToday.verticalHeader().setDefaultSectionSize(40)
        self.table_givenToday.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_5.addWidget(self.table_givenToday)
        self.tabWidget.addTab(self.tab_givenToday, "")
        self.tab_expired = QtWidgets.QWidget()
        self.tab_expired.setObjectName("tab_expired")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_expired)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_searchExpired = QtWidgets.QPushButton(self.tab_expired)
        self.btn_searchExpired.setText("")
        self.btn_searchExpired.setIcon(icon)
        self.btn_searchExpired.setIconSize(QtCore.QSize(24, 24))
        self.btn_searchExpired.setCheckable(True)
        self.btn_searchExpired.setObjectName("btn_searchExpired")
        self.horizontalLayout_7.addWidget(self.btn_searchExpired)
        self.le_searchExpired = QtWidgets.QLineEdit(self.tab_expired)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchExpired.sizePolicy().hasHeightForWidth())
        self.le_searchExpired.setSizePolicy(sizePolicy)
        self.le_searchExpired.setMinimumSize(QtCore.QSize(0, 25))
        self.le_searchExpired.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchExpired.setFont(font)
        self.le_searchExpired.setObjectName("le_searchExpired")
        self.horizontalLayout_7.addWidget(self.le_searchExpired)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.table_expaired = QtWidgets.QTableWidget(self.tab_expired)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_expaired.setFont(font)
        self.table_expaired.setObjectName("table_expaired")
        self.table_expaired.setColumnCount(0)
        self.table_expaired.setRowCount(0)
        self.table_expaired.horizontalHeader().setStretchLastSection(False)
        self.table_expaired.verticalHeader().setDefaultSectionSize(40)
        self.table_expaired.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_10.addWidget(self.table_expaired)
        self.tabWidget.addTab(self.tab_expired, "")
        self.tab_outsides = QtWidgets.QWidget()
        self.tab_outsides.setObjectName("tab_outsides")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_outsides)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_searchOutside = QtWidgets.QPushButton(self.tab_outsides)
        self.btn_searchOutside.setText("")
        self.btn_searchOutside.setIcon(icon)
        self.btn_searchOutside.setIconSize(QtCore.QSize(24, 24))
        self.btn_searchOutside.setCheckable(True)
        self.btn_searchOutside.setChecked(False)
        self.btn_searchOutside.setObjectName("btn_searchOutside")
        self.horizontalLayout_8.addWidget(self.btn_searchOutside)
        self.le_searchOutsides = QtWidgets.QLineEdit(self.tab_outsides)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_searchOutsides.sizePolicy().hasHeightForWidth())
        self.le_searchOutsides.setSizePolicy(sizePolicy)
        self.le_searchOutsides.setMinimumSize(QtCore.QSize(0, 25))
        self.le_searchOutsides.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_searchOutsides.setFont(font)
        self.le_searchOutsides.setObjectName("le_searchOutsides")
        self.horizontalLayout_8.addWidget(self.le_searchOutsides)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.table_outsides = QtWidgets.QTableWidget(self.tab_outsides)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_outsides.setFont(font)
        self.table_outsides.setObjectName("table_outsides")
        self.table_outsides.setColumnCount(13)
        self.table_outsides.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_outsides.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outsides.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outsides.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outsides.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_outsides.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_outsides.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 255))
        self.table_outsides.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 255))
        self.table_outsides.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 255))
        self.table_outsides.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 127))
        self.table_outsides.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 127))
        self.table_outsides.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 127))
        self.table_outsides.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.table_outsides.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.table_outsides.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.table_outsides.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.table_outsides.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.table_outsides.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.table_outsides.setHorizontalHeaderItem(12, item)
        self.table_outsides.horizontalHeader().setMinimumSectionSize(50)
        self.table_outsides.horizontalHeader().setStretchLastSection(False)
        self.table_outsides.verticalHeader().setDefaultSectionSize(40)
        self.table_outsides.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_9.addWidget(self.table_outsides)
        self.tabWidget.addTab(self.tab_outsides, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.groupBox_footer = QtWidgets.QGroupBox(self.frame_main)
        self.groupBox_footer.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_footer.setTitle("")
        self.groupBox_footer.setObjectName("groupBox_footer")
        self.verticalLayout.addWidget(self.groupBox_footer)
        self.horizontalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.btn_searchOutside.clicked['bool'].connect(self.le_searchOutsides.setVisible) # type: ignore
        self.btn_searchBook.clicked['bool'].connect(self.le_searchBook.setVisible) # type: ignore
        self.btn_searchMember.clicked['bool'].connect(self.le_searchMember.setVisible) # type: ignore
        self.btn_searchGivenToday.clicked['bool'].connect(self.le_searchGivenToday.setVisible) # type: ignore
        self.btn_searchExpired.clicked['bool'].connect(self.le_searchExpired.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kütüphane Otomasyonu v1.0"))
        self.btn_openTransactions.setText(_translate("MainWindow", "Ver"))
        self.btn_openMemberSave.setText(_translate("MainWindow", "Üye Kayıt"))
        self.btn_openSaveBook.setText(_translate("MainWindow", "Kitap Kayıt"))
        self.btn_openReports.setText(_translate("MainWindow", "Raporlar"))
        self.btn_openSettings.setText(_translate("MainWindow", "Ayarlar"))
        self.btn_quit.setText(_translate("MainWindow", "Çıkış"))
        self.le_searchBarcode.setPlaceholderText(_translate("MainWindow", "barkod"))
        self.le_searchBook.setPlaceholderText(_translate("MainWindow", "ara"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_books), _translate("MainWindow", "Eser Listesi"))
        self.le_searchMember.setPlaceholderText(_translate("MainWindow", "ara"))
        self.table_memberList.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_members), _translate("MainWindow", "Üye Listesi"))
        self.le_searchGivenToday.setPlaceholderText(_translate("MainWindow", "ara"))
        self.table_givenToday.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_givenToday), _translate("MainWindow", "Bugün Verilenler"))
        self.le_searchExpired.setPlaceholderText(_translate("MainWindow", "ara"))
        self.table_expaired.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_expired), _translate("MainWindow", "Süresi Dolanlar"))
        self.le_searchOutsides.setPlaceholderText(_translate("MainWindow", "ara"))
        self.table_outsides.setSortingEnabled(True)
        item = self.table_outsides.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_outsides.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_outsides.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_outsides.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.table_outsides.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.table_outsides.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tıkla"))
        item = self.table_outsides.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Barkod No"))
        item = self.table_outsides.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Eser Adı"))
        item = self.table_outsides.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Yazarı"))
        item = self.table_outsides.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Veriliş Tarihi"))
        item = self.table_outsides.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Kalan Gün"))
        item = self.table_outsides.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "İade Tarihi"))
        item = self.table_outsides.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TC Kimlik No"))
        item = self.table_outsides.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Okul No"))
        item = self.table_outsides.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Ad"))
        item = self.table_outsides.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Soyad"))
        item = self.table_outsides.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Sınıf"))
        item = self.table_outsides.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Şube"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_outsides), _translate("MainWindow", "Dışardakiler"))
