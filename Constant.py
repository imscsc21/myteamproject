class Constant:
    __instance = None
    
    @staticmethod
    def getInstance():
        if(Constant.__instance == None):
            Constant.__instance = Constant()
        return Constant.__instance
        
    serverIp = ""
    