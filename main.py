from alarmdialog import Ui_AlarmDialog
import asyncio
from mainui import Ui_MainWindow
from clock_manager import Clock_Manager
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
from ctypes import wintypes


isClockVisible = True
def main():
    if __name__ == "__main__":

        myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        manager = Clock_Manager()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.verticalLayoutWidget.setVisible(False)
        manager.start(ui)
        MainWindow.show()
        sys.exit(app.exec_())




main()
