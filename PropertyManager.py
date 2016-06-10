import json
from socket import *
class ServerPropertyManager:
    __instance = None
    @property
    def serverport(self):
        return self.__serverport
    
    def setServerIp(self,ipaddr):
        self.__ip=ipaddr
    @staticmethod
    def getInstance():
        if(ServerPropertyManager.__instance == None):
            ServerPropertyManager.__instance = ServerPropertyManager(8997)
        return ServerPropertyManager.__instance
    @property
    def port_WaitingRoom(self):
        return self.__port_wr
    @property
    def port_CheckWaitingRoom(self):
        return self.__port_cwr
    @property
    def port_Game(self):
        return self.__port_g
    @property
    def port_TransmitProperty(self):
        return self.__port_tp
    @property
    def port_CheckName(self):
        return self.__port_cn
    @property
    def isLoadedData(self):
        return self.__ild
    def setData(self,d):
        for key in d:
            keydasi = str(key)
            if(keydasi=="port.waiting_room"):
                self.__port_wr = int(d[key])
            elif(keydasi == "port.check_waiting_room"):
                self.__port_cwr = int(d[key])
            elif(keydasi == "port.game"):
                self.__port_g = int(d[key])
            elif(keydasi == "port.check_name"):
                self.__port_cn = int(d[key])
            elif(keydasi == "port.transmit_property"):
                self.__port_tp = int(d[key])
    def printData(self):
        print(self.port_WaitingRoom, self.port_CheckWaitingRoom,self.port_Game, self.port_CheckName )                
    def loadPropertyFromServer(self):
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((self.__ip,8997))
        rawdata = s.recv(2000000)
        data = json.loads(rawdata.decode("utf-8")) 
        
        self.setData(data)
        self.__ild=True
        s.close()
    def __init__(self,Port):
        self.__serverport = Port
        self.__ild =False
