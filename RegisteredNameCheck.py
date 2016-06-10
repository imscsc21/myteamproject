import PropertyManager
import json
from socket import *
class RegisteredNameCheck:
    @property
    def nameCheckServerPort(self):
        return self.__ncsp
    def __init__(self,serverip):
        self.__serverIp = serverip
        spm = PropertyManager.ServerPropertyManager.getInstance()
        spm.setServerIp(serverip)
        if(not spm.isLoadedData):
            spm.loadPropertyFromServer()
        self.__ncsp = spm.port_CheckName
    def checkName(self,requestedName):
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((self.__serverIp,self.nameCheckServerPort))
        s.send(str.encode(requestedName))
        rawdata =  s.recv(2000000).decode("utf-8")
        data = json.loads(rawdata)
        s.close()
        return bool(data['isRegisteredName'])
        
            
