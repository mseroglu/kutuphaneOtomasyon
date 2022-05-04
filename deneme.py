
from PyQt5 import QtCore, QtWidgets, QtGui
import numpy as np

# generate np array of (r, g, b) triplets with dtype uint8
height = width = 255
RGBarray = np.array([[r % 256, c % 256, -c % 256] for r in range(height) for c in range(width)], dtype=np.uint8)

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel()
# create QImage from numpy array
image = QtGui.QImage(bytes(RGBarray), width, height, 3*width, QtGui.QImage.Format_RGB888)
print(bytes(RGBarray))
pixmap = QtGui.QPixmap(image)
label.setPixmap(pixmap)
label.show()
app.exec()