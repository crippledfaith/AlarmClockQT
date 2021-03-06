from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow:QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(480, 200)
        MainWindow.setMinimumSize(QtCore.QSize(480, 200))
        MainWindow.setMaximumSize(QtCore.QSize(480, 200))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        iconFile = 'icon.ico'
        iconPath = os.path.join(application_path, iconFile)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextAlarmLabel = QtWidgets.QLabel(self.centralwidget)
        self.nextAlarmLabel.setGeometry(QtCore.QRect(350, 0, 181, 31))
        self.nextAlarmLabel.setObjectName("nextAlarmLabel")
        self.clockAlarmToggleButton = QtWidgets.QPushButton(self.centralwidget)
        self.clockAlarmToggleButton.setGeometry(QtCore.QRect(5, 5, 121, 31))
        self.clockAlarmToggleButton.setObjectName("clockAlarmToggleButton")
        self.clockGridWidget = QtWidgets.QWidget(self.centralwidget)
        self.clockGridWidget.setGeometry(QtCore.QRect(12, 40, 455, 150))
        self.clockGridWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.clockGridWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.clockGridWidget.setObjectName("clockGridWidget")
        self.clockGridLayout = QtWidgets.QGridLayout(self.clockGridWidget)
        self.clockGridLayout.setContentsMargins(0, 0, 0, 0)
        self.clockGridLayout.setObjectName("clockGridLayout")
        self.dateLabel = QtWidgets.QLabel(self.clockGridWidget)

        font = QtGui.QFont()
        font.setPointSize(23)
        self.dateLabel.setFont(font)
        self.dateLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateLabel.setText("Sunday, September 5, 2021")
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.clockGridLayout.addWidget(self.dateLabel, 0, 0, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.clockGridWidget)

        font = QtGui.QFont()
        font.setPointSize(58)
        self.timeLabel.setFont(font)
        self.timeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.clockGridLayout.addWidget(self.timeLabel, 4, 0, 1, 1)

        self.dateTimeTimer = QtCore.QTimer()

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(12, 40, 455, 150))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horzontalLayout = QtWidgets.QHBoxLayout()
        self.horzontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horzontalLayout.setObjectName("horzontalLayout")
        self.isEveryDayCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.isEveryDayCheckBox.setObjectName("isEveryDayCheckBox")
        self.horzontalLayout.addWidget(self.isEveryDayCheckBox)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setMinimumDateTime(datetime.now())
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horzontalLayout.addWidget(self.dateTimeEdit)
        self.addAlarmButton = QtWidgets.QPushButton()
        self.addAlarmButton.setGeometry(QtCore.QRect(0, 0, 121, 31))
        self.addAlarmButton.setObjectName("addAlarmButton")
        self.horzontalLayout.addWidget(self.addAlarmButton)
        self.verticalLayout.addLayout(self.horzontalLayout)
        self.listView = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alarm Clock QT"))
        self.nextAlarmLabel.setText(_translate("MainWindow", "TextLabel"))
        self.clockAlarmToggleButton.setText(_translate("MainWindow", "Clock/Alarm"))
        self.timeLabel.setText(_translate("MainWindow", "9:53:03 AM"))
        self.isEveryDayCheckBox.setText(_translate("MainWindow", "Every Day"))
        self.addAlarmButton.setText(_translate("MainWindow", "Add Alarm"))
