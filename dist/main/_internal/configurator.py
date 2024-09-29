import json
class configurator():
    def __init__(self,path):
        self.__path=path
        self.__mod=None
        self.__folder=None
        self.__read()
    def __read(self):
        if self.__mod=='r':
            return None
        self.__mod='r'
        if self.__folder!=None:
            self.__folder.close()
        try:
            self.__folder=open(self.__path,'r')
        except FileNotFoundError:
            self.__write()
            self.__folder.write('{}')
    def __write(self):
        if self.__mod=='w':
            return None
        self.__mod='w'
        if self.__folder!=None:
            self.__folder.close()
        self.__folder=open(self.__path,'w')
    def ALL(self):
        self.__read()
        js=json.loads(self.__folder.read())
        self.__folder=None
        self.__mod=None
        return js
    def get(self,element,stondart=None):

        try:
            return self.ALL()[element]
        except KeyError:
            self.set(element,stondart)
            return stondart
    def set(self,element,value):
        self.__read()
        js=self.ALL()
        self.__write()
        js[element]=value
        s=str(js)
        s=s.replace("'",'"')
        s=s.replace(', "',',\n"')
        self.__folder.write(s)
