from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QTextImageFormat
from PIL import Image

def resizeImg(imgName):
    ab = Image.open("imgBarkode/"+imgName)
    ab.thumbnail([200,200*257//441])
    ab.save("imgBarkode/_"+imgName)

resizeImg("7661130000242.png")


class Reports:
    def handlePrint(self):
        try:
            dialog = QtGui.QPrintDialog()
            if dialog.exec_() == QtGui.QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())
        except Exception as E:
            print(f"Fonk: handlePrint   \t\t{E}")

    def handlePreview(self):
        try:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec_()
        except Exception as E:
            print(f"Fonk: handlePreview   \t\t{E}")


    # ve son olarak belgeyi oluşturmak ve yazdırmak için bazı yöntemler:

    def handlePaintRequest(self, printer):
        try:
            document = self.makeTableDocument()
            document.print_(printer)
        except Exception as E:
            print(f"Fonk: handlePaintRequest   \t\t{E}")

    def makeTableDocument(self):
        try:
            document = QtGui.QTextDocument()
            cursor = QtGui.QTextCursor(document)
            imgFormat = QTextImageFormat()
            cursor.insertImage(QImage("./imgBarkode/_7661130000204.png"),imgFormat)
            cursor.insertImage("./imgBarkode/_7661130000204.png")

            rows = 10
            columns = 3
            table = cursor.insertTable(rows + 1, columns)
            format = table.format()
            format.setHeaderRowCount(1)
            table.setFormat(format)
            format = cursor.blockCharFormat()
            format.setFontWeight(QtGui.QFont.Bold)
            for column in range(columns):
                cursor.setCharFormat(format)
                cursor.insertText("title")
                cursor.movePosition(QtGui.QTextCursor.NextCell)
            for row in range(rows):
                for column in range(columns):
                    cursor.insertText("text")
                    # cursor.insertImage("./imgBarkode/_7661130000204.png")
                    cursor.movePosition(QtGui.QTextCursor.NextCell)
            return document
        except Exception as E:
            print(f"Fonk: makeTableDocument   \t\t{E}")
