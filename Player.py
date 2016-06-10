import json
from Deck import *
from Card import *

class Player:
    __hand=None
    __name=""
    def __init__(self,name="None"):
        self.__hand = Deck.getEmptyDeck();
        self.setName(name)
    def popTwoCards(self,selectedIndexes):
        maxIdx = max(selectedIndexes)
        minIdx = min(selectedIndexes)
        
        del self.__hand[maxIdx]
        del self.__hand[minIdx]
            
    def popOneCard(self,card):
        for c in self.__hand:
            if(card==c  ):
                self.__hand.remove(c)x
                break
    def selectCard(self,player,waitMode=False):
        pdeck = player.getDeck()
        responseIdx = 0#impl this
        return pdeck[responseIdx]
    
    def exportCard(self,exportingIdx):
        result = self.__hand[exportingIdx].cloneCard()
        del self.__hand[exportingIdx]
        return  result
    def importCard(self,card):
        self.__hand.append(card)

    def setName(self,Name):
        self.__name = Name
        return self
    def getName(self):
        return self.__name
    def getHand(self):
        return self.__hand
    def getDeck(self):
        return self.__hand
    def toJson(self):
        handj = []
        for c in self.__hand:
            handj.add(c.toJson());
        result = {"hand":handj,"name":name}
        result = json.dumps(result)
        return result
class Computer(Player):
    def __init__(self,pname="Computer"):
        super().__init__(pname)
            
    def popTwoCards(self,selectedIndexes):
        card1 = None
        card2 = None
        levelList = Card.Levels()
        for  in range(len(levelList)-1)
        while(type(card1) == JokerCard or type(card2) == JokerCard):
             
        super().popTwoCards(selectedIndexes)
    
    def selectCard(self,player,waitMode=False):
        import random
        pdeck = player.getDeck()
        idx = random.randrange(0, len(player.getDeck()))
        result = player.getDeck()[idx].clone()
        self.importCard(result)
        player.exportCard(idx)
        return result