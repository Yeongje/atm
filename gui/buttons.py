from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QFont

from core.accounts import Accounts
from gui.dialoag import VerifyPIN, EnterCredit


class ButtonWidget(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        self.insertCardBtn = QPushButton("Insert Card")
        self.withdrawBtn = QPushButton("Withdraw")
        self.balanceBtn = QPushButton("Balance")
        self.depositBtn = QPushButton("Deposit")
        self.exitBtn = QPushButton("EXIT")

        self.vertLayout = QVBoxLayout()

        self.insertCardBtn.clicked.connect(self.clickedInsertCard)
        self.withdrawBtn.clicked.connect(self.clickedWithdraw)
        self.balanceBtn.clicked.connect(self.clickedBalance)
        self.depositBtn.clicked.connect(self.clickedDeposit)

        self.exitBtn.clicked.connect(self.exitAtm)

        self.initUI()

    def initUI(self):
        self.vertLayout.addWidget(self.insertCardBtn)
        self.vertLayout.addWidget(self.withdrawBtn)
        self.vertLayout.addWidget(self.balanceBtn)
        self.vertLayout.addWidget(self.depositBtn)
        self.vertLayout.addWidget(self.exitBtn)

        self.withdrawBtn.setDisabled(True)
        self.balanceBtn.setDisabled(True)
        self.depositBtn.setDisabled(True)

        self.setLayout(self.vertLayout)

    def initAll(self):
        self.insertCardBtn.setDisabled(False)
        self.withdrawBtn.setDisabled(True)
        self.balanceBtn.setDisabled(True)
        self.depositBtn.setDisabled(True)

    def clickedInsertCard(self):
        pinDiag = VerifyPIN(self)
        pinDiag.exec_()
        pinDiag.show()

        self.mainWindow.account = Accounts(pinDiag.pinEditLabel.text())
        self.mainWindow.statusBar().showMessage("Account Number : " + pinDiag.pinEditLabel.text())

    def clickedWithdraw(self):
        enterCredit = EnterCredit("How much would you like to withdraw?")
        enterCredit.exec_()
        enterCredit.show()

        if int(enterCredit.creditEditLabel.text()) > self.mainWindow.account.balance:
            self.mainWindow.infoScreenWidget.showMessage("Your balance is not enough \n"
                                                         "  * Check your balance and try again")
        else:
            self.mainWindow.infoScreenWidget.showMessage("You withdraw $" + enterCredit.creditEditLabel.text())
            self.mainWindow.account.withdraw(int(enterCredit.creditEditLabel.text()))


    def clickedBalance(self):
        self.mainWindow.infoScreenWidget.showMessage("Your balance is now $" + str(self.mainWindow.account.balance))

    def clickedDeposit(self):
        enterCredit = EnterCredit("How much would you like to deposit?")
        enterCredit.exec_()
        enterCredit.show()

        self.mainWindow.account.deposit(int(enterCredit.creditEditLabel.text()))
        self.mainWindow.infoScreenWidget.showMessage("You deposit $" + enterCredit.creditEditLabel.text())


    def exitAtm(self):
        self.mainWindow.initAll()

