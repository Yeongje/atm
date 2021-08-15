from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel, QVBoxLayout


class VerifyPIN(QDialog):
    def __init__(self, ButtonWidget):
        super().__init__()

        self.buttonsWidget = ButtonWidget;

        self.vertLayout = QVBoxLayout()
        self.pinEditLabel = QLineEdit()
        self.pinLabel = QLabel("Enter your Pin number")
        self.enterBtn = QPushButton("ENTER")

        self.enterBtn.clicked.connect(self.checkPin)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Enter Pin Number")
        self.setLayout(self.vertLayout)

        self.vertLayout.addWidget(self.pinEditLabel)
        self.vertLayout.addWidget(self.pinLabel)
        self.vertLayout.addWidget(self.enterBtn)


    def checkPin(self):
        try:
            if self.pinEditLabel.text() != "":
                temp = int(self.pinEditLabel.text())
                self.close()

                selectAccountDiag = SelectAccount(self)
                selectAccountDiag.exec_()
                # selectAccountDiag.show()

                self.buttonsWidget.withdrawBtn.setDisabled(False)
                self.buttonsWidget.balanceBtn.setDisabled(False)
                self.buttonsWidget.depositBtn.setDisabled(False)
                self.buttonsWidget.insertCardBtn.setDisabled(True)

                self.buttonsWidget.mainWindow.infoScreenWidget.insertCard()
            else:
                self.pinLabel.setStyleSheet('color: red')
                self.pinLabel.setText("Try to enter pin number again")
        except ValueError:
            self.pinLabel.setStyleSheet('color: red')
            self.pinLabel.setText("Enter only number")

class SelectAccount(QDialog):
    def __init__(self, VerifyPIN):
        super().__init__()

        self.verifyPinDiag = VerifyPIN

        self.vertLayout = QVBoxLayout()
        self.selectAccountLabel = QLabel("Select Account")
        self.savingBtn = QPushButton("Savings")
        self.creditBtn = QPushButton("Credit")

        self.savingBtn.clicked.connect(self.clickedSavingBtn)
        self.creditBtn.clicked.connect(self.clickedCreditBtn)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Select Account")
        self.setLayout(self.vertLayout)

        self.vertLayout.addWidget(self.selectAccountLabel)
        self.vertLayout.addWidget(self.savingBtn)
        self.vertLayout.addWidget(self.creditBtn)

    def clickedSavingBtn(self):
        self.verifyPinDiag.buttonsWidget.mainWindow.infoScreenWidget.accountType = "Saving Account"
        self.close()

    def clickedCreditBtn(self):
        self.verifyPinDiag.buttonsWidget.mainWindow.infoScreenWidget.accountType = "Credit Account"
        self.close()

class EnterCredit(QDialog):
    def __init__(self, text):
        super().__init__()

        self.vertLayout = QVBoxLayout()
        self.enterCreditLabel = QLabel()
        self.creditEditLabel = QLineEdit()
        self.creditEditLabel.setValidator(QIntValidator(0, 100000, self.creditEditLabel))
        self.enterBtn = QPushButton("Enter")

        self.diagText = text

        self.enterBtn.clicked.connect(self.clickedEnter)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.diagText)
        self.setLayout(self.vertLayout)

        self.vertLayout.addWidget(self.creditEditLabel)
        self.vertLayout.addWidget(self.enterCreditLabel)
        self.vertLayout.addWidget(self.enterBtn)

        self.enterCreditLabel.setText(self.diagText)

    def clickedEnter(self):
        if self.creditEditLabel.text() != "":
            self.close()
        else:
            self.enterCreditLabel.setStyleSheet('color: red')