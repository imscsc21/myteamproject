from tkinter import *
import tkinter.messagebox
from socket import *
import json
from Constant import *
from StringData import *
from RegisteredNameCheck import *
from PropertyManager import *
import time, threading
 
 
class SyncThread(threading.Thread):
    def __init__(self):
        self.__port = ServerPropertyManager.getInstance().port_WaitingRoom()
        self.__ipaddr = Constant.serverIp
        threading.Thread.__init__(self)
        self.__suspend = False
        self.__exit = False
        self.__loopControl = True
        self.__rfv = 300/1000
    def run(self):
        
        while True:
            ### Suspend ###
            if self.__suspend:
                time.sleep(0.5)
            ### Process ###
            while(self.__loopControl):
                while self.__suspend:
                    time.sleep(0.5)
                time.sleep(self.__rfv)
            
            
            ### Exit ###
            if self.__exit:
                break
             
    def setRefreshFrequencyValue(sec):
        self.__rfv = sec
        
    def mySuspend(self):
        self.__suspend = True
         
    def myResume(self):
        self.__suspend = False
         
    def myExit(self):
        self.__exit = True
 
class LoginApp(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.create_wdigets()
        
    def create_wdigets(self):
        Label(self,text="대기중인 플레이어").grid(row=0,column=0)
        self.playerlist = Listbox(self)
        self.playerlist.grid(row=1,column=0)
        Label(self,text="사용자 이름").grid(row=3,column=0)
        self.userNameEditText = Entry(self,width=20,justify=CENTER)
        self.userNameEditText.grid(row=4,column=0)
        Button(self, text="접속", command=self.connectWaitRoom).grid(row=5, column=0, columnspan=2)
        Button(self, text="종료", command=self.quit).grid(row=8, column=3, columnspan=2)
    
        
def showWaitingRoomWindow():
    root = Tk()
    root.title("Waiting Room")
    root.geometry("600x600")
    LoginApp(root)
    root.mainloop()
showWaitingRoomWindow()