from tkinter import *
import tkinter.messagebox
import json
from StringData import *
    
class WaitingRoom(Frame):
    def  __init__(self,master,resp):
        super().__init__(master)
        self.__tk = master
        #self.pack(pady=20)
        self.__totalPlayerCount = 0
        self.__firstAccess = True
        self.create_wdigets(resp)
        if (not( "user_name" in resp)):
            resp["user_name"] = []
        if ( not ("computer_count" in resp)):
            resp["computer_count"] = 0
        self.__resp = resp
        
        
    def resizeWindowSize(self):
        width = 0
        height = 0
        width+= self.__lb1.winfo_reqwidth()
        height+= self.__lb1.winfo_reqheight()
        
        width+= self.__btn1.winfo_reqwidth()
        
        width+= self.__btn2.winfo_width()
        height+= self.__btn2.winfo_height()
        
        width+= self.__btn3.winfo_reqwidth()
        height+= self.__btn3.winfo_reqheight()
        
        width+= self.__lb1.winfo_width()
        height+= self.__lb1.winfo_height()
        
        width+= self.label_totalPlayerCount.winfo_reqwidth()
        height+= self.listbox_playerlist.winfo_reqheight()
        height+= self.entry_inputnewplayerName.winfo_reqheight()
        width+= int(width*0.5)
        height += int(height*0.3)
        print((width,height));
        self.__tk.geometry(str(width)+"x"+str(height))
        self.__tk.update()
        
    def destroy(self):
        size = self.listbox_playerlist.size() 
        if(size>1):
            for i in range(size):
                self.__resp["user_name"].append(self.listbox_playerlist.get(i))
            super().destroy()
        else:
            self.showDialogHadMinPlayer()
    def showDialogHadMinPlayer(self):
        tkinter.messagebox.showinfo(StringData.getDlgTitle_minPlayer(),StringData.getDlgContent_minPlayer())
    
    def quit(self):
        size = self.listbox_playerlist.size()
        if(size>1):
            for i in range(size):
                self.__resp["user_name"].append(self.listbox_playerlist.get(i))
            super().quit()
        else:
            self.showDialogHadMinPlayer()
    def doSyncCkbEnableComputer(self):
        pass
        
    def create_wdigets(self,resp=None):
        self.__lb1 = Label(self,text=StringData.getLableTitlePlayerCountHeader())
        self.__lb1.grid(row=0,column=0)
        self.label_totalPlayerCount= Label(self,justify=LEFT,text=str(self.__totalPlayerCount)+"명")
        self.label_totalPlayerCount.grid(row=0,column=1)
        self.__btn1 = Button(self,text=StringData.getBtnTxtPlayerDel(),command=self.delPlayer)
        self.__btn1.grid(row=0,column=3)
        self.listbox_playerlist = Listbox(self,selectmode="SINGLE",height=8,width=35)
        self.listbox_playerlist.grid(row=1,column=0,columnspan=4)
        self.entry_inputnewplayerName = Entry(self,width=20,justify=LEFT)
        self.entry_inputnewplayerName.grid(row=2,column=0,columnspan=2)
        self.__btn2 = Button(self,text=StringData.getBtnTxtPlayerAdd(),command=self.addPlayer)
        self.__btn2.grid(row=2,column=3)
        self.__btn3 = Button(self,text=StringData.getBtnTxtDoPlay(),command=self.quit)
        self.__btn3.grid(row=3,column=4)
        #self.__ckb_enable_computer = Checkbutton(master,text="컴퓨터 사용",command=self.doSyncCkbEnableComputer).
        if("user_name" in resp and resp["user_name"] != None and type(resp["user_name"]) == list and self.__firstAccess == True):
            self.__firstAccess = False
            
            tl = resp["user_name"]
            print ("enter",tl)
            for v in tl:
                print(v)
                if(v != ''  ):
                    self.listbox_playerlist.insert(self.listbox_playerlist.size(),v)
                    
            self.label_totalPlayerCount['text'] = str(self.listbox_playerlist.size())+StringData.getPeopleCountUnit()
            #resp["user_name"].clear()    
        self.entry_inputnewplayerName.bind("<Return>",self.addPlayer)
        self.pack(padx=20,pady=20)
        #self.resizeWindowSize()
    #def eventInput(self,event):
    #    self.addPlayer()
    
    def delPlayer(self):
        idx = self.listbox_playerlist.curselection()
        if(idx != ()):
            self.listbox_playerlist.delete(idx)
            self.label_totalPlayerCount['text'] = str(self.listbox_playerlist.size())+StringData.getPeopleCountUnit()
            
    def addPlayer(self,event=None):
        pname = self.entry_inputnewplayerName.get()
        if(pname == '' or pname == []):
            tkinter.messagebox.showinfo(StringData.getErrorText(),StringData.getUserNameEmptyErrorMsgBoxContent())
        else:
            size = self.listbox_playerlist.size()
            hasSamePlayer = False
            for i in range(size):
                if(pname == self.listbox_playerlist.get(i)):
                    hasSamePlayer = True
                    break
            if(hasSamePlayer):
                tkinter.messagebox.showinfo(StringData.getDlgTitle_existRegisteredPlayer(),StringData.getDlgContent_existRegisteredPlayer())
            elif(size>7):
                tkinter.messagebox.showinfo(StringData.getDlgTitle_maxPlayer(),StringData.getDlgContent_maxPlayer())
            else:
                self.listbox_playerlist.insert(self.listbox_playerlist.size(),pname)
                self.label_totalPlayerCount['text'] = str(self.listbox_playerlist.size())+StringData.getPeopleCountUnit()
            
        self.entry_inputnewplayerName.delete(0,END)
class InputView:
    @staticmethod
    def getPlayerNameList():
        response = {}
        root = Tk()
        root.title("Waiting Room")
        WaitingRoom(root,response)
        root.mainloop()
        return response
    @staticmethod
    def getPlayerNameListWithParam(resp):
        
        root = Tk()
        root.title("Waiting Room")
        WaitingRoom(root,resp)
        root.mainloop()
        return resp
def main():
    playerNameList = {}
    playerNameList = InputView.getPlayerNameList()
    while(playerNameList["user_name"] == [] or not ( 2<=len(playerNameList["user_name"])<=8)):
        playerNameList = InputView.getPlayerNameListWithParam(playerNameList)
    print(playerNameList)
main()
