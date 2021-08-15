from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont


class infoScreenWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.infoLayout = QVBoxLayout()
        self.mainInfoLabel = QLabel("Welcome To ATM \n"
                                    "This ATM provides limited service now \n"
                                    "Insert Your Card and Select your account")
        self.balance = 0
        self.accountType = ""

        self.initUI()

    def initUI(self):

        self.setLayout(self.infoLayout)

        self.infoLayout.addWidget(self.mainInfoLabel)
        self.mainInfoLabel.setWordWrap(True)

    def initAll(self):
        self.mainInfoLabel.setText("Welcome To ATM \n"
                                    "This ATM provides limited service now \n"
                                    "Insert Your Card and Select your account")

    def insertCard(self):
        self.mainInfoLabel.setText("You Selected " + self.accountType + "\n"
                                   "Select options below \n\n"
                                   "1. Withdraw \n"
                                   "2. Balance \n"
                                   "3. Deposit")
    def showMessage(self, text):
        self.mainInfoLabel.setText(text)