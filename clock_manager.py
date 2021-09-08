from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from datetime import datetime, timedelta
import calendar
import multiprocessing
import winsound

import math
from alarm import Alarm
from alarm_manager import AlarmManager
from mainui import Ui_MainWindow
from alarmdialog import Ui_AlarmDialog

class Clock_Manager():

    def __init__(self) -> None:
        self.alarmManager = AlarmManager()
        self.alarmManager.setAlarmHandler(self.raiseAlarm)

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
        self.alarmDialog = QtWidgets.QMainWindow()
        self.alarmUI = Ui_AlarmDialog()

        self.alarmUI.setupUi(self.alarmDialog)
        self.alarmUI.player = multiprocessing.Process(target=winsound.PlaySound, args=("Alarm01.wav", winsound.SND_LOOP))
        self.alarmUI.player.start()
        self.alarmUI.dateTimeLabel.setText(datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))
        self.alarmUI.stopButton.clicked.connect(self.stopAlarm)
        self.alarmDialog.show()
    
    def stopAlarm(self):
        self.alarmUI.player.terminate()
        self.alarmDialog.close()
    
    