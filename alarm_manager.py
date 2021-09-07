from alarm import Alarm


from typing import List

class AlarmManager:

    def __init__(self) -> None:
        self.alarmList = []
        self.handler = None

    def getActiveAlarms(self)->List[Alarm]:
        newList = []
        for alarm in self.alarmList :
            if alarm.getIsActive() and alarm.isDisabled == False :
                newList.append(alarm)
        return newList

    def addAlarm(self,alarm:Alarm):
        self.alarmList.append(alarm)
        alarm.setHandler(self.alarmRaised)
    
    def setAlarmHandler(self,handler):
        self.handler = handler

    def alarmRaised(self,alarm:Alarm):
        if self.handler != None :
            self.handler(alarm)
    
    def getNextAlarm(self)->Alarm:
        if len(self.getActiveAlarms()) != 0:
            newList = sorted(self.getActiveAlarms(),key=lambda x: x.getTimeLeft(),reverse=False)
            return newList[0]
        return None




