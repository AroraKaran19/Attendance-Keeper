#Attendance Keeper
#Karan Arora

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys

def main_window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 500)
    win.setWindowTitle('Attendance Keeper')
    win.setFixedSize(500, 500)
    win.setStyleSheet("background-color: yellow;")

    heading = QtWidgets.QLabel(win)
    heading.setText("Attendance Keeper")
    heading.setFont(QFont('helvetica', 20))
    heading.adjustSize()
    heading.move(140, 20)

    win.show()
    sys.exit(app.exec())

main_window()