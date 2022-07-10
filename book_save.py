import locale, os, io
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')

from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidgetItem, QFileDialog, QCompleter
from PyQt5 import QtGui, QtCore
from ui.kitapKayitUI import Ui_MainWindow
from database import db, curs
from datetime import datetime
from messageBox import msg
from PIL import Image
import json


class SaveBook(QMainWindow):
    def __init__(self):
        super(SaveBook, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.duration = 20_000
        self.bookPhotoData = None
        self.ui.le_isbn.setFocus()

        self.showAuthorsOnCombo()
        self.showCategoriesOnCombo()
        self.showSectionsOnCombo()
        self.showBookshelfsOnCombo()
        self.showBooksOnTablewidget()

        self.ui.btn_update.setVisible(False)
        self.ui.btn_del.setVisible(False)



        self.ui.btn_save.clicked.connect(self.saveNewBook)
        self.ui.btn_clear.clicked.connect(self.clearForm)
        self.ui.btn_addAuthor.clicked.connect(self.saveNewAuthorName)
        self.ui.btn_addCategori.clicked.connect(self.saveNewCategory)
        self.ui.btn_addSection.clicked.connect(self.saveNewSection)
        self.ui.btn_addBookshelf.clicked.connect(self.saveNewBookshelf)

        self.ui.btn_getDataFromExcel.clicked.connect(db.insertBookDatasFromExcel)
        self.ui.btn_getDataFromExcel.clicked.connect(self.showEvent)
        self.ui.btn_showExcelFile.clicked.connect(self.openSampleExcelPage)
        self.ui.table_bookList.itemClicked.connect(self.showBookInfoInForm)
        self.ui.btn_update.clicked.connect(self.updateBookInfo)
        self.ui.btn_del.clicked.connect(self.delBook)

        self.ui.btn_addImg.clicked.connect(self.addBookPhoto)

        self.ui.le_isbn.installEventFilter(self)
        self.veriSetiAktar()


    def eventFilter(self, obj: 'QObject', event: 'QEvent') -> bool:
        try:
            if event.type() == QtCore.QEvent.FocusOut and obj.objectName()== "le_isbn":
                listBookData = self.completerBookInfoDict.get( self.ui.le_isbn.text())
                if listBookData:
                    self.ui.le_bookName.setText(listBookData[0])
                    self.ui.combo_authorName.setCurrentText(listBookData[1])
                    self.ui.le_publisher.setText(listBookData[2])
                    self.ui.le_pageCount.setText(listBookData[3])
            return super(SaveBook, self).eventFilter(obj, event)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: eventFilter\t\tHata Kodu : {E}", self.duration)

    def veriSetiAktar(self):
        try:
            completerList = []
            self.completerBookInfoDict = {}
            with open("./auxiliary_files/books.json", encoding="utf-8") as file:
                books = json.loads(file.read())
                for book in books:
                    completerList.append(book["isbn"])
                    self.completerBookInfoDict[book["isbn"]] = list(book.values())[1:]
                self.ui.le_isbn.setCompleter(QCompleter(completerList))
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: veriSetiAktar\t\tHata Kodu : {E}", self.duration)

    def addBookPhoto(self):
        try:
            filePath, _ = QFileDialog.getOpenFileName(self, caption= "Fotoğraf Seçimi", filter= "Görsel (*.png *.jpeg *.jpg)")
            if filePath.endswith(".png") or filePath.endswith(".jpg") or filePath.endswith(".jpeg"):
                with Image.open(filePath) as resim:
                    resim = resim.resize( (150,200), Image.ANTIALIAS)
                    IO_Object = io.BytesIO()
                    resim.save(IO_Object, "png")
                    self.bookPhotoData = IO_Object.getvalue()
                self.showBookPhoto(self.bookPhotoData)
        except Exception as E:
            print(f"Fonk: addMemberPhoto    Hata: {E}")

    def showBookPhoto(self, data):
        try:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData( data )
            if not data:
                pixmap = "img/book_cover.png"
            self.ui.btn_addImg.setIcon( QtGui.QIcon(pixmap) )
            self.ui.btn_addImg.setStyleSheet("QPushButton {border-radius: 20px}")
        except Exception as E:
            print(f"Fonk: showBookPhoto   \tHata: {E} ")

    def openSampleExcelPage(self):
        try:
            os.startfile("excel_pages")
        except Exception as E:
            print(f"Fonk: openSampleExcelPage   \tHata: {E} ")

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        try:
            self.showAuthorsOnCombo()
            self.showCategoriesOnCombo()
            self.showSectionsOnCombo()
            self.showBookshelfsOnCombo()
            self.showBooksOnTablewidget()
            self.setBarkodeNumber()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: enterEvent\t\tHata Kodu : {E}", self.duration)

    def showBooksOnTablewidget(self):
        books = db.getData("KitapTablosu", "kitapId", "Barkod", "KitapAdi")
        try:
            if books:
                self.ui.table_bookList.clearContents()
                self.ui.table_bookList.setRowCount(len(books)+20)
                for row, book in enumerate(books):
                    for col, item in enumerate(book[1:]):
                        self.ui.table_bookList.setItem(row,col,QTableWidgetItem(str(item)))
                        if col==1:
                            self.ui.table_bookList.item(row,col).setData(QtCore.Qt.UserRole,book)
                            self.ui.table_bookList.item(row,col).setToolTip("click")
                    self.ui.table_bookList.item(row, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBooksOnTablewidget     Hata Kodu : {E}", self.duration)

    def setBarkodeNumber(self) -> None:
        try:
            newBarkodeNumber7   = db.createBarkodeNumber()
            newBarkodeNumber7 = f"{int(newBarkodeNumber7) + 1:0>7}"
            self.newBarkodeNumber8, self.imgByte   = db.createBarkodeImg( newBarkodeNumber7 )
            self.ui.le_barkode.setText( self.newBarkodeNumber8 )
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(self.imgByte, "png")
            self.ui.label_barcodeImg.setPixmap(pixmap)
        except Exception as E:
            print(E)
            self.ui.statusbar.showMessage(f"Fonk: setBarkodeNumber     Hata Kodu : {E}", self.duration)

    def getBookInfo(self) -> dict:
        return {
                "ISBN"      : self.ui.le_isbn.text().strip(),
                "KitapAdi"  : self.ui.le_bookName.text().strip().title(),
                "YazarId"   : self.ui.combo_authorName.currentData(QtCore.Qt.UserRole), #yazarId,
                "KategoriId": self.ui.combo_category.currentData(QtCore.Qt.UserRole),   #kategoriId,
                "BolumId"   : self.ui.combo_section.currentData(QtCore.Qt.UserRole),    #bolumId,
                "RafId"     : self.ui.combo_bookshelf.currentData(QtCore.Qt.UserRole),  #rafId,
                "Yayinevi"  : self.ui.le_publisher.text().strip().title(),
                "SayfaSayisi": self.ui.le_pageCount.text().strip(),
                "BasimYili" : self.ui.le_publicationYear.text(),
                "Aciklama"  : self.ui.plain_description.toPlainText(),
                "DisariVerme": self.ui.combo_exportability.currentIndex(),
                "KayitTarihi": datetime.now().date(),
                "ImgBook"   : self.bookPhotoData,
                "BarkodPrint": self.ui.checkBox_barkodYazdirma.checkState()}


    def showBookInfoInForm(self):
        try:
            self.ui.btn_save.setVisible(False)
            self.ui.btn_update.setVisible(True)
            self.ui.btn_del.setVisible(True)
            Id, Barkod, bookName = self.ui.table_bookList.currentItem().data(QtCore.Qt.UserRole)
            cameData = db.getBookDataWithId(Id=Id)
            self.selectedIdForUpdate = Id
            self.selectedISBN        = cameData[2]
            self.ui.le_barkode.setText( cameData[1] )
            self.ui.le_isbn.setText( cameData[2] )
            self.ui.le_bookName.setText( cameData[3] )
            self.ui.combo_authorName.setCurrentIndex(self.ui.combo_authorName.findData( cameData[4] ) )
            self.ui.combo_category.setCurrentIndex(self.ui.combo_category.findData( cameData[5] ) )
            self.ui.combo_section.setCurrentIndex(self.ui.combo_section.findData( cameData[6] ) )
            self.ui.combo_bookshelf.setCurrentIndex(self.ui.combo_bookshelf.findData( cameData[7] ) )
            self.ui.le_publisher.setText( cameData[8] )
            self.ui.le_pageCount.setText( cameData[9] )
            self.ui.le_publicationYear.setText( cameData[10] )
            self.ui.plain_description.setPlainText(cameData[11])
            self.ui.combo_exportability.setCurrentIndex(cameData[12])
            self.ui.label_barcodeImg.clear()
            if cameData[15] is not None:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(cameData[15], "png")
                self.ui.label_barcodeImg.setPixmap(pixmap)
            self.showBookPhoto(cameData[16])
            self.bookPhotoData = cameData[16]
            self.ui.checkBox_barkodYazdirma.setChecked(bool(cameData[17]))
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBookInfoInForm \t\t Hata Kodu : {E}", self.duration)

    def delBook(self):
        try:
            if self.selectedIdForUpdate:
                bookId, barkod, bookName = self.ui.table_bookList.currentItem().data(QtCore.Qt.UserRole)
                bookData = db.checkBookEntrustState(Id=bookId)
                if bookData:
                    msg.popup_mesaj("Silme işlemi başarısız", f"Barkod\t:  {bookData[0]}\n"
                                                              f"Kitap Adı\t:  {bookData[1]}\n"  
                                                              f"Uye No\t:  {bookData[2]}\n"
                                                              f"Uye Adı\t:  {bookData[3]} {bookData[4]}\n\n"
                                                              f"Kitap üye ile eşleşiyor. Kitabı silmek için önce üyeden geri almalısınız")
                    self.clearForm()
                    return
                result, _ = msg.MesajBox("DİKKAT : Eser Silinecek", f"Barkod No :  {barkod}\nEser Adı\t :  {bookName} \n\neseri silmek istediğinizden emin misiniz?\t\t\n")
                if result:
                    db.delData("KitapTablosu", kitapId=bookId)
                    if curs.rowcount>0:
                        msg.popup_mesaj('Silindi', "Kitap kaydı silindi. Hadi hayırlı olsun. ;-)\t\n")
                    self.showBooksOnTablewidget()
                    self.clearForm()
            else:
                msg.popup_mesaj('Seçim yapılmadı', f'Silmek için bir kitap seçmediniz. \t\t\n')
        except AttributeError as E:
            msg.popup_mesaj('Seçim yapılmadı', f'Silmek için bir kitap seçmediniz. \t\t\n')
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: delBook \t\t Hata Kodu : {E}", self.duration)

    def updateBookInfo(self):
        try:
            cols_datas = self.getBookInfo()
            if self.selectedISBN != cols_datas['ISBN']:
                db.updateISBN(oldISBN=self.selectedISBN, newISBN=cols_datas['ISBN'])
            imageData  = cols_datas["ImgBook"]
            del cols_datas["ImgBook"]
            if bool(cols_datas["KitapAdi"]):
                cols_datas["kitapId"] = self.selectedIdForUpdate
                db.updateData(TableName="KitapTablosu", **cols_datas)
                if curs.rowcount>0:
                    self.saveBookImage(isbn=cols_datas["ISBN"], imgData= imageData)
                    self.clearForm()
                    self.showBooksOnTablewidget()
            else:
                msg.popup_mesaj("Dikkat", "Eser adı boş olmamalı ! ! !\t\t")
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: updateBookInfo \t\t Hata Kodu : {E}", self.duration)

    def saveBookImage(self, isbn, imgData=None):
        try:
            if imgData is not None and len(isbn)==13:
                result = db.getImageData("KitapFotoTablosu", "COUNT(*)", ISBN=isbn)
                if result:
                    db.updateImage(ISBN=isbn, ImgBook=imgData)
                else:
                    db.insertData("KitapFotoTablosu", ISBN=isbn, ImgBook=imgData)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: saveBookImage \t\t Hata Kodu : {E}", self.duration)

    def saveNewBook(self) -> None:
        try:
            def saveBooks(quantityBooks, cols_datas) -> int :
                saved = 0
                for i in range(quantityBooks):                              # kaç adet kaydetmek istiyoruz
                    db.insertData(TableName="KitapTablosu", **cols_datas)
                    saved += curs.rowcount
                    if curs.rowcount > 0:
                        db.saveBarkod(curs.lastrowid)
                return saved

            kacKitap = self.ui.spinBox_bookCount.value()
            cols_datas = self.getBookInfo()
            imageData = cols_datas["ImgBook"]
            del cols_datas["ImgBook"]
            if not cols_datas["KitapAdi"]:
                msg.popup_mesaj("Boş alan uyarısı", "Eser adı boş olmamalı ! ! !\t\t")
            else:
                count = db.checkBook( cols_datas['ISBN'] )        # aynı isbn no ile kayıtlı kitap sayısını döndürür int
                saved = 0
                if count:
                    result, _ = msg.MesajBox("Kayıt kontrol",
                                             f"'{cols_datas['ISBN']}'  ISBN numarası ile kayıtlı {count} adet eser mevcut. \t\n\n"
                                             f"Aynı eserden ekleme yapmak istiyor musunuz?\n")
                    if result:
                        saved = saveBooks(quantityBooks=kacKitap, cols_datas=cols_datas)
                else:
                    saved = saveBooks(quantityBooks=kacKitap, cols_datas=cols_datas)

                if saved > 0 :
                    self.saveBookImage(isbn=cols_datas["ISBN"], imgData= imageData)
                    mesaj = f"{saved} kitap başarı ile kayıt edildi"
                    saved = 0
                    self.showBooksOnTablewidget()
                    self.clearForm()
                else:
                    mesaj = "Kayıt işlemi yapılmadı ! ! !"
                msg.popup_mesaj("Kayıt", mesaj=mesaj)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: saveNewBook      Hata Kodu : {E}", self.duration)

    def showAuthorsOnCombo(self):
        try:
            self.ui.combo_authorName.clear()
            self.ui.combo_authorName.insertItem(0, "")
            authors = db.getDataWithOrderBy("YazarTablosu", "YazarAdi", "yazarId")
            row = 1
            for Name, ID in authors:
                self.ui.combo_authorName.addItem(Name,userData=ID)
                self.ui.combo_authorName.setIconSize(QtCore.QSize(24,24))
                self.ui.combo_authorName.setItemIcon(row, QtGui.QIcon( "./img/author.png" if row % 2 else "./img/author1.png" ))
                row +=1
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showAuthorsOnCombo        Hata Kodu : {E}", self.duration)

    def showCategoriesOnCombo(self):
        try:
            self.ui.combo_category.clear()
            self.ui.combo_category.insertItem(0, "")
            categories = db.getDataWithOrderBy("KategoriTablosu", "Kategori", "kategoriId")
            for category, ID in categories:
                self.ui.combo_category.addItem(category, userData=ID)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showCategoriesOnCombo        Hata Kodu : {E}", self.duration)

    def showSectionsOnCombo(self):
        try:
            self.ui.combo_section.clear()
            self.ui.combo_section.insertItem(0, "")
            sections = db.getDataWithOrderBy("BolumTablosu", "Bolum", "bolumId")
            for section, ID in sections:
                self.ui.combo_section.addItem(section, userData=ID)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showSectionsOnCombo        Hata Kodu : {E}", self.duration)

    def showBookshelfsOnCombo(self)->None:
        try:
            self.ui.combo_bookshelf.clear()
            self.ui.combo_bookshelf.insertItem(0, "")
            bookshelfs  = db.getDataWithOrderBy("RafTablosu", "RafNo", "rafId")
            for bookshelf, ID in bookshelfs:
                self.ui.combo_bookshelf.addItem(bookshelf, userData=ID)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: showBookshelfsOnCombo        Hata Kodu : {E}", self.duration)

    def saveNewAuthorName(self):
        try:
            text, result = QInputDialog.getText(self, "Yazar Adı kayıt", "Kaydetmek istediğiniz YAZARIN ADINI Giriniz :")
            text = text.strip().title()
            if result and bool(text):
                db.insertData(TableName = "YazarTablosu", YazarAdi= text.title())
                self.showAuthorsOnCombo()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: saveNewAuthorName     Hata Kodu : {E}", self.duration)

    def saveNewCategory(self):
        try:
            text, result = QInputDialog.getText(self, "Kategori kayıt", "Kategori Adı Giriniz :")
            text = text.strip().capitalize()
            if result and bool(text):
                db.insertData(TableName = "KategoriTablosu", Kategori=text.title())
                self.showCategoriesOnCombo()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: saveNewCategory     Hata Kodu : {E}", self.duration)

    def saveNewSection(self):
        try:
            text, result = QInputDialog.getText(self, "Bölüm-Dolap kayıt", "Bölüm-Dolap Adı Giriniz :")
            text = text.strip().capitalize()
            if result and bool(text):
                db.insertData(TableName = "BolumTablosu", Bolum=text)
                self.showSectionsOnCombo()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: saveNewSection     Hata Kodu : {E}", self.duration)

    def saveNewBookshelf(self):
        try:
            text, result = QInputDialog.getText(self, "Raf No kayıt", "Raf No Giriniz :")
            text = text.strip().capitalize()
            if result and bool(text):
                db.insertData(TableName = "RafTablosu", RafNo=text)
                self.showBookshelfsOnCombo()
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: saveNewBookshelf     Hata Kodu : {E}", self.duration)

    def clearForm(self):
        try:
            self.ui.table_bookList.clearSelection()
            self.ui.le_isbn.clear()
            self.ui.le_bookName.clear()
            self.ui.combo_authorName.setCurrentIndex(-1)
            self.ui.combo_category.setCurrentIndex(-1)
            self.ui.combo_section.setCurrentIndex(-1)
            self.ui.combo_bookshelf.setCurrentIndex(-1)
            self.ui.le_publisher.clear()
            self.ui.le_pageCount.clear()
            self.ui.le_publicationYear.clear()
            self.ui.plain_description.clear()
            self.ui.spinBox_bookCount.setValue(1)
            self.setBarkodeNumber()
            self.selectedIdForUpdate = None
            self.ui.btn_addImg.setIcon(QtGui.QIcon("img/book_cover.png"))
            self.bookPhotoData = None
            self.ui.btn_save.setVisible(True)
            self.ui.btn_update.setVisible(False)
            self.ui.btn_del.setVisible(False)
        except Exception as E:
            self.ui.statusbar.showMessage(f"Fonk: clearForm        Hata Kodu : {E}", self.duration)


