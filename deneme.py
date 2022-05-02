import sys
from PyQt5.QtWidgets import *

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

import sys
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

class MyCombo(QWidget):
    def __init__(self, *args):
        super(MyCombo, self).__init__(*args)
        #super.__init__(self, *args)
        vLayout=QVBoxLayout(self)
        self.setLayout(vLayout)

        self.combo=QComboBox(self)
        self.combo.currentIndexChanged.connect(self.currentIndexChanged)
        comboModel=self.combo.model()


        for i, book in (((11,12,13,14,15),"Book1"),((12,21,22,23,45),"Book2"),((13,30,31,32,33,34),"Book3"),((14,"a","b"),"Book4"),(15,"Book5")):
            item = QtGui.QStandardItem(str(i))
            item.setData(i, QtCore.Qt.UserRole)
            item.setText(book)

            comboModel.appendRow(item)
        vLayout.addWidget(self.combo)

    def currentIndexChanged(self, index):
        modelIndex = self.combo.model().index(index, 0)
        print(self.combo.model().data(modelIndex, QtCore.Qt.UserRole))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyCombo()
    w.show()
    sys.exit(app.exec_())