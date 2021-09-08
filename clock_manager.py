import winsound
import os
import sys
import math
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from datetime import datetime, timedelta

from alarm import Alarm
from alarm_manager import AlarmManager
from mainui import Ui_MainWindow
from alarmdialog import Ui_AlarmDialog

class Clock_Manager():

    def __init__(self) -> None:
        self.alarmManager = AlarmManager()
        self.alarmManager.setAlarmHandler(self.raiseAlarm)
        self.alarmDialogs = []
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        soundFile = 'Alarm01.wav'
        self.soundPath = os.path.join(application_path, soundFile)
       

    def start(self,ui:Ui_MainWindow):
        self.ui = ui
        self.ui.addAlarmButton.clicked.connect(self.addAlarm)
        self.ui.dateTimeTimer.timeout.connect(self.updateDateTime)
        self.ui.clockAlarmToggleButton.clicked.connect(self.ToggleClockAlarm)
        self.ui.dateTimeTimer.start(1000)
        self.ui.timeLabel.setText(datetime.now().strftime('%I:%M:%S %p'))
        self.ui.dateLabel.setText(f"{datetime.today().strftime('%A, %B %d, %Y')}")
        self.ui.dateTimeEdit.setDateTime(datetime.now())
        self.ui.nextAlarmLabel.setText("No Alarm")
        self.ui.listView.doubleClicked.connect(self.showItem)


    def ToggleClockAlarm(self):
        if self.ui.clockGridWidget.isVisible():
            self.ui.verticalLayoutWidget.setVisible(True)
            self.ui.clockGridWidget.setVisible(False)
            self.loadAlarmToListView(self.alarmManager.alarmList)
        else:
            self.ui.verticalLayoutWidget.setVisible(False)
            self.ui.clockGridWidget.setVisible(True)

    def updateDateTime(self):
        self.ui.timeLabel.setText(datetime.now().strftime('%I:%M:%S %p'))
        self.ui.dateLabel.setText(f"{datetime.today().strftime('%A, %B %d, %Y')}")
        nextAlarm = self.alarmManager.getNextAlarm()
        if nextAlarm == None :
            self.ui.nextAlarmLabel.setText("No Alarm")
        else:
            timeLeft = nextAlarm.getTimeLeft()
            self.ui.nextAlarmLabel.setText(f'Next Alarm in {self.getTimeText(timeLeft)}')
    
    def getTimeText(self,timeLeft:timedelta):
        days = timeLeft.days
        hours = timeLeft.total_seconds() / 3600
        mins = timeLeft.total_seconds() / 60

        if days > 1 :
            return f'{int(math.ceil(days))} days'
        if hours > 1 :
            return f'{int(math.ceil(hours))} hrs'
        if mins > 1 :
            return f'{int(math.ceil(mins))} mins'
        return f'{ int(math.ceil(timeLeft.seconds)) } secs'

    def addAlarm(self):
        alarm = Alarm(self.ui.isEveryDayCheckBox.isChecked(),self.ui.dateTimeEdit.dateTime().toPyDateTime())
        self.alarmManager.addAlarm(alarm)
        self.addAlarmToListView(alarm)

    def loadAlarmToListView(self, alarmList):
        self.ui.listView.clear()
        for alarm in alarmList:
            self.addAlarmToListView(alarm)


    def addAlarmToListView(self, alarm:Alarm):
        item = QListWidgetItem()
        item.setText(alarm.getDisplayDateTime())
        item.setData(QtCore.Qt.UserRole,alarm)
        self.ui.listView.addItem(item)
    
    def raiseAlarm(self,alarm:Alarm):
        alarmDialog = QtWidgets.QMainWindow()
        alarmUI = Ui_AlarmDialog()
        alarmUI.setupUi(alarmDialog)
        winsound.PlaySound(self.soundPath, winsound.SND_LOOP + winsound.SND_ASYNC)
        alarmUI.dateTimeLabel.setText(datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))
        alarmUI.stopButton.clicked.connect(lambda:self.stopAlarm(alarmDialog))
        alarmUI.snoozeButton.clicked.connect(lambda:self.snoozeAlarm(alarmDialog))
        alarmDialog.show()
        self.alarmDialogs.append(alarmDialog)
    
    def stopAlarm(self,alarmDialog:Ui_AlarmDialog):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        self.alarmDialogs.remove(alarmDialog)
        alarmDialog.close()
    
    def snoozeAlarm(self,alarmDialog:Ui_AlarmDialog):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        alarmDialog.component.snoozeTimer.timeout.connect(lambda:self.snoozeTimeOut(alarmDialog))
        alarmDialog.component.snoozeTimer.start(300000)
        alarmDialog.hide()

    def snoozeTimeOut(self,alarmDialog:Ui_AlarmDialog):
        winsound.PlaySound(self.soundPath, winsound.SND_LOOP + winsound.SND_ASYNC)
        alarmDialog.component.dateTimeLabel.setText(datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))
        alarmDialog.component.snoozeTimer.stop()
        alarmDialog.show()
    
    def showItem(self,item:QtCore.QModelIndex):
        alarm:Alarm = item.data(QtCore.Qt.UserRole)
        self.ui.listView.takeItem(item.row())
        #self.ui.isEveryDayCheckBox.setChecked(alarm.isEveryDay)
        #self.ui.dateTimeEdit.setDateTime(alarm.getDateTime())
        self.alarmManager.removeAlarm(alarm)
