from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QHBoxLayout
from PyQt5.QtGui import QFont

from gui.buttons import ButtonWidget
from gui.info_screen import infoScreenWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mainWidget = QWidget()

        self.account = ""
        self.buttonsWidget = ButtonWidget(self)
        self.infoScreenWidget = infoScreenWidget()

        self.horLayout = QHBoxLayout()

        self.initUI()

    def initUI(self):
        self.buttonsWidget.__init__(self)
        self.infoScreenWidget.__init__()

        self.setWindowTitle("ATM")
        self.setGeometry(800, 800, 800, 800)
        self.mainWidget.setLayout(self.horLayout)

        self.horLayout.addWidget(self.buttonsWidget)
        self.horLayout.addWidget(self.infoScreenWidget)

        self.setCentralWidget(self.mainWidget)
        self.statusBar().showMessage('Welcome To ATM')

        # self.show()

    def initAll(self):
        self.buttonsWidget.initAll()
        self.infoScreenWidget.initAll()
        self.statusBar().showMessage('Welcome To ATM')
