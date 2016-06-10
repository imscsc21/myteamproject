from tkinter import *
import tkinter.messagebox
from socket import *
import json
from Constant import *
from StringData import *
from RegisteredNameCheck import *
class LoginApp(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.create_wdigets()
        
    def create_wdigets(self):
        Label(self,text="서버IP 주소").grid(row=0,column=0)
        self.serveripedittext = Entry(self,width=20,justify=CENTER)
        self.serveripedittext.grid(row=1,column=0)
        Label(self,text="사용자 이름").grid(row=3,column=0)
        self.userNameEditText = Entry(self,width=20,justify=CENTER)
        self.userNameEditText.grid(row=4,column=0)
        Button(self, text="접속", command=self.connectWaitRoom).grid(row=5, column=0, columnspan=2)
        Button(self, text="종료", command=self.quit).grid(row=8, column=3, columnspan=2)
    
    def connectWaitRoom(self):
        iptext = self.serveripedittext.get()
        userName = self.userNameEditText.get()
        if(not self.isIpaddressFormat(iptext)):
            tkinter.messagebox.showinfo(StringData.getIpFormatErrorMsgBoxTitle(),StringData.getIpFormatErrorMsgBoxContent())
        elif(userName == [] or userName == ''):
            tkinter.messagebox.showinfo(StringData.getUserNameEmptyErrorMsgBoxTitle(),StringData.getUserNameEmptyErrorMsgBoxContent())
        else:
            try:
                rnc = RegisteredNameCheck(iptext)
                
                if(not rnc.checkName(userName)):
                    cons = Constant.getInstance()
                
                    Constant.serverIp = iptext
                    tkinter.messagebox.showinfo("성공","로그인됨")
                else:
                    tkinter.messagebox.showinfo("실패","이미 사용중인 이름")
            except:
                tkinter.messagebox.showinfo(StringData.getLoginSocketErrorMsgBoxTitle(),StringData.getLoginSocketMsgBoxContent())
        
    def isIpaddressFormat(self,text):
        if text.find(".") == -1:
            return False
        else:
            sp = text.split('.')
            if(len(sp) != 4):
                return False
            for v in sp:
                try:
                    chk = int(v)
                    if(not (0<= chk <= 255)):
                        return False
                except:
                    return False
            
            return True
        
def showLoginWindow():
    root = Tk()
    root.title("Login")
    root.geometry("600x600")
    LoginApp(root)
    root.mainloop()
showLoginWindow()