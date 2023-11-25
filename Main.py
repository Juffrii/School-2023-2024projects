import sys

from DataBase import *
from ReactionModel import *

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QListWidget
from PyQt6.QtWidgets import QTextEdit, QScrollArea, QScrollBar, QTextBrowser
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QCheckBox, QRadioButton
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('User Interface\\MainWindow.ui', self)
        self.data = list()
        self.addReaction.clicked.connect(self.create_new_b)
        self.SearchButton.clicked.connect(self.search_b)

    def search_b(self):
        self.listWidget_2.clear()
        try:
            if self.atomNorStuff.checkState():
                biba = search(mode="not_initial", compound=self.reactionCompoundsLIne.text(),
                              result=self.reactionResultLine.text(), ion="False", charct="True")

            for i in biba:
                self.listWidget_2.insertItem(1, i.compound + " -> " + i.result)
        except:
            self.listWidget_2.insertItem(0, "Error")

    def create_new_b(self):
        try:
            create_new(compound=str(self.reactionCompoundsInput.text()), result=str(self.reactionResultInput.text()),
                       ion="False", charct="True")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
