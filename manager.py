import sys

import os
import json

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QWidget, QFileDialog


class OpenFolder(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/open_folder.ui', self)
        self.OpenFolder.clicked.connect(self.open_folder)
        self.StartEditor.clicked.connect(self.start_editor)

    def start_editor(self):
        print(self.plainTextEdit.toPlainText())
        sys.exit()

    def open_folder(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Choose folder", ".")
        self.plainTextEdit.setPlainText(dirlist)


class NewFolder(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/new_project.ui', self)
        self.OpenFolder.clicked.connect(self.open_folder)
        self.StartEditor.clicked.connect(self.start_editor)

    def start_editor(self):
        directory = str(self.Directory.toPlainText() + "/" + self.ProjectName.toPlainText())
        os.mkdir(directory)
        os.mkdir(directory + "/src")
        os.mkdir(directory + "/code")

        data = {
            "name": self.ProjectName.toPlainText(),
            "libraries": ["None"],
            "date": "None",
            "dir": str(self.Directory.toPlainText() + "/" + self.ProjectName.toPlainText()),
            "settings": ["None"]
        }

        with open(directory + "/data_file.json", "w") as write_file:
            json.dump(data, write_file)
        sys.exit()

    def open_folder(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Choose folder", ".")
        self.Directory.setPlainText(dirlist)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/manager.ui', self)
        self.OpenFolder.clicked.connect(self.open_folder)
        self.NewProjects.clicked.connect(self.new_project)

    def open_folder(self):
        self.app = QApplication(sys.argv)
        self.ex = OpenFolder()
        self.ex.show()

    def new_project(self):
        self.app1 = QApplication(sys.argv)
        self.ex1 = NewFolder()
        self.ex1.show()


#   def settings(self):
#       self.app = QApplication(sys.argv)
#       self.ex = OpenFolder()
#       self.ex.show()
#
#   def open_recent(self):
#       self.app = QApplication(sys.argv)
#       self.ex = OpenFolder()
#       self.ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
