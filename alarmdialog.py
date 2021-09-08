from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

class Ui_AlarmDialog(QtWidgets.QMainWindow):
    def setupUi(self, Form:QtWidgets.QMainWindow):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(350, 135)
        Form.setMinimumSize(QtCore.QSize(350, 135))
        Form.setMaximumSize(QtCore.QSize(350, 135))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        Form.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        iconFile = 'icon.ico'
        iconPath = os.path.join(application_path, iconFile)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)

        self.snoozeTimer = QtCore.QTimer(Form)
        self.dateTimeLabel = QtWidgets.QLabel(Form)
        self.dateTimeLabel.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dateTimeLabel.setFont(font)
        self.dateTimeLabel.setObjectName("dateTimeLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 70, 341, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.snoozeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.snoozeButton.setFont(font)
        self.snoozeButton.setObjectName("snoozeButton")
        self.horizontalLayout.addWidget(self.snoozeButton)
        Form.component = self
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alarm"))
        self.dateTimeLabel.setText(_translate("Form", "TextLabel"))
        self.stopButton.setText(_translate("Form", "STOP"))
        self.snoozeButton.setText(_translate("Form", "SNOOZE FOR\n5 MINS"))
