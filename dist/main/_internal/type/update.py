from type import acthion
import time
class update():

    def __init__(self,times):
        self.ontime=acthion.acthion()
        self.maxtime=times
        if callable(times):
            self.F=times
            self.maxtime=self.F()
            self.ontime+=lambda :self.settime(self.F())
        self.time=time.time()
    def settime(self,time):
        self.maxtime=time
    def update(self):
        if time.time()-self.time>=self.maxtime:
            self.ontime.invock()
            self.time=time.time()
