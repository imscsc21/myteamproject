import json


class Card:
    __Categories = ["spade","diamond","club","heart","joker"]
    __CategoriesAsArt = ["♠","♦","♣","♥","☢"] 
    __Levels = [ "2","3","4","5","6","7","8","9","10","J","Q","K","A","Jk1" ]
    __category=0
    __level=0
    @staticmethod
    def Categories():
        return Card.__Categories
    @staticmethod
    def CategoriesAsArt():
        return Card.__CategoriesAsArt
    def cloneCard(self):
        result = Card(self.__category,self.__level)
        return result
    @staticmethod
    def Levels():
        return Card.__Levels
    
    def __str__(self):
        return self.__CategoriesAsArt[self.__category]+ " "  +self.getLevelAsString()
    def __init__(self,Category=0,Level=0):
        self.setCardAttribute(Category,Level)
     
    def setCardAttribute(self,Category,Level):
        self.setCategory(Category)
        self.setLevel(Level)
        return self
    def setCategory(self,Category):
        self.__category = Category
        return self
    def getRawCategory(self):
        return self.__category

    def getRawLevel(self):
        return self.__level

    def getRawCategoryAsString(self):
        return str(self.getRawCategory())
	
    def getRawLevelAsString(self):
        return str(self.getRawLevel())
	
    def toJson(self):
        result = {"rawcategory":self.getRawCategoryAsString(),"rawlevel":self.getRawLevelAsString()}
        result = json.dumps(result)
        return result
	
    def getCategoryAsIndex(self):
        return self.getRawCategory()
	
    def getLevelAsIndex(self):
        return self.getRawLevel()
	
    def getCategoryAsString(self):
        return Card.Categories[self.getCategoryAsIndex()]
	
    def getLevelAsString(self):
        return self.__Levels[self.__level]
	
    def setLevel(self, Level):
        self.__level = Level
        return self
    def isDropable(self):
        return True
class JokerCard(Card):
    def getThisAsParent(self):
        return super()
    def __init__(self):
        super().__init__(len(Card.Categories())-1,len(Card.Levels())-1)
    def isDropable(self):
        return False