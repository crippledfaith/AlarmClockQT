from datetime import datetime, timedelta
from PyQt5 import QtCore
import uuid



class Alarm:

    def __init__(self,isEverDay:bool,dateAndtime:datetime):
        if isEverDay:
            self.datetime= datetime(datetime.now().year,datetime.now().month,datetime.now().day,dateAndtime.hour,dateAndtime.minute,dateAndtime.second)
        else:
            self.datetime = datetime(dateAndtime.year,dateAndtime.month,dateAndtime.day,dateAndtime.hour,dateAndtime.minute,dateAndtime.second)
        self.isEveryDay = isEverDay
        self.id = str(uuid.uuid4())
        self.alarmFile = ''
        self.isDisabled= False
        self.handler=None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkForAlarm)
        self.timer.start(1000)

    
    def getDateTime(self):
        if self.isEveryDay:
            dateAndTime = datetime.now()
            if self.datetime.year != dateAndTime.year and self.datetime.month != dateAndTime.month and self.datetime.day != dateAndTime.day :
                self.datetime= datetime(dateAndTime.year,dateAndTime.month,dateAndTime.day, self.datetime.hour,self.datetime.minute,self.datetime.second)
        return self.datetime
    
    def getTimeLeft(self):
        selfDateTime = self.getDateTime()
        dateTimeNow = datetime.now()
        timeDelta = selfDateTime - dateTimeNow
        if timeDelta.total_seconds() > -1 or self.isEveryDay == False :
            return timeDelta
        dateTime = selfDateTime.__add__(timedelta(days=1))
        timeDelta = dateTime - dateTimeNow
        return timeDelta

    def getIsActive(self):
        return self.getTimeLeft().total_seconds() > 0
    
    def getDisplayDateTime(self):
        if self.isEveryDay :
            return self.getDateTime().strftime("%I:%M:%S %p")
        return self.getDateTime().strftime("%m/%d/%Y %I:%M:%S %p")
    
    def setHandler(self,handler):
        self.handler = handler

    def checkForAlarm(self):
        if self.getIsActive() :
            if self.handler != None:
                timeDelta = self.getTimeLeft()
                if timeDelta.total_seconds()<1 and timeDelta.total_seconds()>-1 :
                    self.handler(self)
        else:
            self.timer.stop()


