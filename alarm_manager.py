from datetime import datetime
from alarm import Alarm
from bson import json_util
import json
import os.path
from os import path

from typing import List

class AlarmManager:

    def __init__(self) -> None:
        self.alarmList = []
        self.handler = None
        self.load()

    def getActiveAlarms(self)->List[Alarm]:
        newList = []
        for alarm in self.alarmList :
            if alarm.getIsActive() and alarm.isDisabled == False :
                newList.append(alarm)
        return newList

    def addAlarm(self,alarm:Alarm):
        self.alarmList.append(alarm)
        alarm.setHandler(self.alarmRaised)
        self.save()


    def removeAlarm(self,alarm:Alarm):
        self.alarmList.remove(alarm)
        alarm.revomeHandler()
        alarm.stopAlarm()
        self.save()


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


    def save(self):
        jsonStr = ""
        list =self.alarmList
        for i in range(0,len(self.alarmList)) :
            jsonStr = jsonStr + F'{{ "isEveryDay":"{list[i].isEveryDay}","datetime":"{list[i].datetime.strftime("%m/%d/%Y %I:%M:%S %p")}","isDisabled":"{list[i].isDisabled}","alarmFile":"{list[i].alarmFile}","id":"{list[i].id}" }}'
            if (i!=0 and len(self.alarmList)==1) or (i != len(self.alarmList)-1) :
                jsonStr = jsonStr + ","


        jsonStr=f"[{jsonStr}]"
        with open("./alarms.json", "w") as file:
            file.write(jsonStr)
    

    def load(self):
        if(path.exists("./alarms.json")==False):
            return
        with open("./alarms.json", 'r') as f:
            dic = json.load(f)
        for o in dic:
            alarm= Alarm(o['isEveryDay']=="True", datetime.strptime(o['datetime'],"%m/%d/%Y %I:%M:%S %p"))
            alarm.isDisabled=o['isDisabled']=="True"
            alarm.alarmFile=o['alarmFile']
            alarm.id=o['id']
            self.alarmList.append(alarm)
            alarm.setHandler(self.alarmRaised)