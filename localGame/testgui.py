from tkinter import *
import threading
from Deck import *
from Util import *
from Player import *
from Util import *
class MainGame(Frame):
    __isPullCardMode = False
    
    def __init__(self,master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        players = [Player("p"+str(i)) for i in range(1,5)]
        players = Util.chooseDirection(players,False)
        self.__playerNames = [p.name for p in players ]
        self.__maxWidth =master.winfo_screenwidth()
        self.__players={p.name:p for p in players}
        self.__recordRank=[]
        deck = Deck()
        Util.distributeCardToPlayers(players,deck)
        self.create_widgets()
        self.pack(fill=BOTH,padx=10,pady=10)
        
    #isDropCardMode=False
    @staticmethod
    def main():
        window = Tk()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window.geometry(str(screen_width)+"x"+str(screen_height))
        
        mg = MainGame(window)
        #th = threading.Thread(target=mg.auto,args=(50,))
        #th.start()
        window.mainloop()
    isDropCardsMode=True
    def auto(self,count):
        import time
        for _ in range(count):
            self.changeText()
            time.sleep(0.5)
    def getPlayerOrder(self):
        result = ""
        for i in range(len(self.__playerNames)):
            result += self.__playerNames[i]+"\n"
        return result
    def ExistRemoveablePlayer(self):
        if(len(self.__playerNames) >1 and len(self.__players[self.__playerNames[1]].getDeck() )==0 ):
            #현재 플레이어가 다음 플레이어의 마지막으로 남은 1장을 뽑아 다음 플레이어의 순서가 필요없어진경우 플레이어제거  
            name = str(self.__playerNames[1])
            remaincardcount = str(len(self.__players[self.__playerNames[1]].getDeck()))
            self.__playerNames.remove(self.__playerNames[1])
            self.porderlv.delete(1)
            self.__recordRank.append(name+"\n"+remaincardcount)
        if(len(self.__playerNames) >0 and len(self.__players[self.__playerNames[0]].getDeck() )==0 ):
            name = str(self.__playerNames[0])
            remaincardcount = str(len(self.__players[name].getDeck()))
            self.__playerNames = self.__playerNames[1:]
            self.porderlv.delete(0)
            self.__recordRank.append(name+"\n"+remaincardcount)
            
        print("erp")
    def isDropCardMode(self):
        c=False
        for pn in self.__playerNames:
            b=self.__players[pn].hasSameLevelCard()
            print(b)
            c= (c or b)
        if(not c and MainGame.isDropCardsMode):
            MainGame.isDropCardsMode=False
        if(not MainGame.isDropCardsMode):    
            return False
        return c
    def nextPlayerOrder(self,lvChange=False):
        if(len(self.__playerNames) >0 and len(self.__players[self.__playerNames[0]].getDeck() )==0 ):
            self.__playerNames = self.__playerNames[1:]
        else:
            self.__playerNames=Util.moveListOrder(self.__playerNames)
            if(lvChange):
                self.porderlv.insert(self.porderlv.size(),self.porderlv.get(0))
        self.__players[self.__playerNames[0]].getCardFrame().tkraise()
        if(len(self.__playerNames)>1):
            if(self.isDropCardMode()):
                self.__preparingFrame.tkraise()
            else:
                self.__players[self.__playerNames[1]].getPublicCardFrame().tkraise()
            
        if(lvChange):
            self.porderlv.delete(0)
            
        return self.__playerNames
    def refreshPlayerRank(self):
        
        playerns = self.__playerNames
        players = self.__players
        stackrank = self.__recordRank
        temprst = {}
        
            
        for i in range(len(playerns)):
            p=players[playerns[i]]
            if(not len(p.getDeck()) in temprst):
                temprst[len(p.getDeck())] = []
            temprst[len(p.getDeck())].append(p.name)
        keys = list(temprst.keys())
        keys.sort()
        rst = []
        self.pranklv.delete(0, max(self.pranklv.size()-1,0))
        for sr in stackrank:
            name,count=sr.split('\n')
            self.pranklv.insert( self.pranklv.size(),(name +", "+str(count)+"장"))
        for k in keys:
            for n in temprst[k]:
                self.pranklv.insert( self.pranklv.size(),(n +", "+str(k)+"장"))
        print("rpr")        
        
    def changeText(self):
        self.nextPlayerOrder(True)
        #self.lb['text'] = self.nextPlayerOrder()
    
    
    def threadWork(self,f5c,f2c):
        import time
        time.sleep(0.2)
        f5c.configure(scrollregion = f5c.bbox("all"))
        f2c.configure(scrollregion = f2c.bbox("all"))
    def doThread(self,f5c,f2c):
        t = threading.Thread(target=self.threadWork ,args=(f5c,f2c,))
        t.start()
    def popCards(self):
        isSuccess = self.__players[self.__playerNames[0]].delSelectedCardsFromFrame()
        if(isSuccess):
            self.nextPlayerOrder(True)
            
            #self.__players[self.__playerNames[0]].getCardFrame()
    def resize_frame(self, e):
        self._canvas.itemconfig(self._frame_id, height=e.height, width=e.width)        
            
    def transmitCard(self,card,nextTurn=False):
        self.__players[self.__playerNames[0]].importCard(card)
        if(nextTurn):
            self.changeText()
    def checkExpectFail(self,mustFail=False):
        if(len(self.__playerNames)==1):
            if(mustFail):
                pass
            else:
                pass
                
            
    def refreshDisplayedCardFrame(self):
        self.__players[self.__playerNames[0]].getCardFrame().tkraise()
        if(len(self.__playerNames)>1):
            if(self.isDropCardMode()):
                self.__preparingFrame.tkraise()
            else:
                self.__players[self.__playerNames[1]].getPublicCardFrame().tkraise()
    def shuffleCurrentHand(self):
        #print(self.__players[self.__playerNames[0]].getDeck()[0])
        print("sch")
        self.__players[self.__playerNames[0]].shuffleDeck()
        self.__players[self.__playerNames[0]].getCardFrame().update()
        #print("aa")
        #print(self.__players[self.__playerNames[0]].getDeck()[0])
    def create_widgets(self):
        deck = Deck()
        deck.shuffle()
        topframe = PanedWindow(self,orient=VERTICAL)
        topframe.pack(fill=BOTH)
        topframe.grid(row=0,column=0)
        #topframe.columnconfigure(0, weight=1)
        #topframe.columnconfigure(0, weight=1)
        frame4 = PanedWindow(topframe)
        topcardframe = Frame(topframe)
        bottomcardframe = Frame(topframe)
        self.frame5container = Canvas(bottomcardframe,scrollregion=(0,0,1500,0))
        frame5 = Frame(self.frame5container)
        frame5.pack(fill=BOTH,expand=TRUE,padx=10)
        xscoller= Scrollbar(bottomcardframe,orient=HORIZONTAL,command=self.frame5container.xview)
        xscoller.pack(side=BOTTOM,fill=X,padx=10)
        self.frame5container.create_window((0,0), window=frame5, anchor=NW)
        self.frame5container.pack(fill=BOTH,expand=TRUE)
        self.frame5container.configure(xscrollcommand=xscoller.set)
        self.frame5container.create_oval(0,0,400,300,fill='red')
        frame2container = Canvas(topcardframe,scrollregion=(0,0,1500,0))
        frame2 = Frame(frame2container)
        frame2.pack(fill=BOTH,expand=TRUE)
        xscollertop= Scrollbar(topcardframe,orient=HORIZONTAL,command=frame2container.xview)
        xscollertop.pack(side=BOTTOM,fill=X,padx=10)

        frame2container.create_window((0,0), window=frame2, anchor=NW)
        frame2container.pack(side=TOP,fill=X,padx=10)
        frame2container.configure(xscrollcommand=xscollertop.set)
        
        topframe.add(topcardframe,stretch="always")
        topframe.add(frame4,stretch="always")
        topframe.add(bottomcardframe,stretch="always")
        playerorderFrame = PanedWindow(frame4,orient=VERTICAL)
        playerRankFrame = PanedWindow(frame4,orient=VERTICAL)
        middleFrame = PanedWindow(frame4)
        
        self.porderlv = Listbox(playerorderFrame,selectmode=NONE,height=8,width=20)
        self.pranklv = Listbox(playerRankFrame,selectmode=NONE,height=8,width=22)
        playerorderFrame.add(Label(playerorderFrame,text="플레이어 순서"))
        playerRankFrame.add(Label(playerRankFrame,text="플레이어 현재 랭킹"))
        playerorderFrame.add(self.porderlv)
        playerRankFrame.add(self.pranklv)
        frame4.add(playerorderFrame,stretch="always")
        frame4.add(middleFrame,stretch="always")
        frame4.add(playerRankFrame,stretch="always")

        self.__preparingFrame = Frame(frame2)
        #self.__preparingFrame.pack(fill=X,expand=TRUE)
        self.__preparingFrame.pack(fill=X,expand=TRUE)
        self.__preparingFrame.grid(row=0,column=0,stick="news")
        Label(self.__preparingFrame,text="Preparing...").grid(row=0,column=0)
        #self.__preparingFrame.pack()
        playerControllView = PanedWindow(middleFrame)
        playerControllView.add(Button(middleFrame,text="change",command=self.changeText),stretch="always")
        playerControllView.add(Button(middleFrame,text="pop cards",command=self.popCards),stretch="always")
        playerControllView.add(Button(middleFrame,text="shuffle cards",command=self.shuffleCurrentHand),stretch="always")
        middleFrame.add(playerControllView)
        for i in range(len(self.__players)):
            self.porderlv.insert(self.porderlv.size(),self.__playerNames[i])
            self.__players[self.__playerNames[i]].getCardFrame(parent=frame5,mgcls=self ,rootCanvas=self.frame5container)
            self.__players[self.__playerNames[i]].getPublicCardFrame(parent=frame2,mgcls=self,rootCanvas=frame2container)
            
        self.refreshDisplayedCardFrame()
        self.refreshPlayerRank()
        topframe.pack(fill=BOTH,expand=TRUE)
        self.frame5container.configure(scrollregion = self.frame5container.bbox("all"))
        frame2container.configure(scrollregion = frame2container.bbox("all"))
        self.doThread(self.frame5container,frame2container)
MainGame.main()