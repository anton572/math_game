from type.Vector2 import Vector2
import time
class redjetbody():
    def __init__(self,object,pos):
        self.object=object
        self.pos=Vector2(pos)
        self.offset=Vector2(0,0)
        self.__gravite=Vector2(0,9.8)
    def updata(self,time):
        self.pos+=self.offset*time
        self.offset+=self.__gravite*time


class physics():
    class __iter():
        def __init__(self,physics):
            self.physics=physics
        def __next__(self):
            return self.physics.__next__()
    def __init__(self):
        self.__object=[]
        self.time=time.time()
    def add(self,object,pos,velosite=[0,0]):
        r=redjetbody(object,pos)
        r.offset=Vector2(velosite)
        self.__object.append(r)
    def _colcul(self,time):
        for i in list(self.__object):
            i.updata(time)
            if i.pos.y>=1500:
                self.__object.remove(i)
    def updata(self):
        t=(self.time-time.time())
        for i in range(7):
            self._colcul(t)
        self.time=time.time()
    def __iter__(self):
        return self.__iter(self.__object.__iter__())




