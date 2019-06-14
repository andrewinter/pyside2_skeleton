import os
import sys
from PySide2.QtGui import QKeySequence
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QFileDialog, QMainWindow, QAction, QDesktopWidget, QWidget, QApplication, QPushButton, QGridLayout, QListWidget, QComboBox

PROGRAM_WIDTH = 500
PROGRAM_HEIGHT = 300

class MainWindow(QMainWindow):
    resized = Signal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.setWindowOptions()
        self.content = WindowContent(parent=self)
        self.setCentralWidget(self.content)

    def initUI(self):
        menu = self.menuBar()
        files = menu.addMenu("Datei")
        open_action = QAction("Öffnen", self)
        save_action = QAction("Speichern", self)
        exit_action = QAction("Schließen", self)
        open_action.triggered.connect(self.open)
        save_action.triggered.connect(self.save)
        exit_action.triggered.connect(self.close)
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        exit_action.setShortcut(QKeySequence("Ctrl+X"))
        files.addAction(open_action)
        files.addAction(save_action)
        files.addAction(exit_action)

    def setWindowOptions(self):
        self.setGeometry(0, 0, PROGRAM_WIDTH, PROGRAM_HEIGHT)
        self.centerApplication()
        self.setWindowTitle("Application Title")

    def centerApplication(self):
        resolution = QDesktopWidget().screenGeometry()
        w = ((resolution.width() / 2) - (self.frameSize().width() / 2))
        h = ((resolution.height() / 2) - (self.frameSize().height() / 2))
        self.move(w, h)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)

    def currentDimensions(self):
        print(f"W: {self.frameGeometry().width()}\nH: {self.frameGeometry().height()}")

    def open(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", os.path.abspath(os.sep), "All files (*.*)")
        try:
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read())
        except OSError as err:
            print(err)

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", os.path.abspath(os.sep), "All files (*.*)")
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("Testfile created by application.py")
        except OSError as err:
            print(err)


class WindowContent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Widgets
        self.list_widget = QListWidget(self)
        self.btn_widget = QPushButton("Push me", self)

        # Widget Options go here

        # Functionality
        self.btn_widget.clicked.connect(self.do_something)

        # Layout
        layout = QGridLayout(self)
        layout.addWidget(self.list_widget, 0, 0)
        layout.addWidget(self.btn_widget, 1, 0)

        # Further Options go here

    def do_something(self):
        print("did something")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
