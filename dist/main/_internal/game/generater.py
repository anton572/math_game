import type.Vector2 as Vector2
import game.object
import random
r=random.Random()
array_type={}
def add_class(class_):
    array_type[class_.__name__]=class_
class basemathgenerator():
    def __init__(self,fabric):
        self.fabric=fabric
    def type_to(self,string:str):
        return int(string)
    def create(self,pos):
        return None
class pluse(basemathgenerator):
    def create(self,pos:Vector2.Vector2):


        a=r.randint(0,10)
        b=r.randint(0,10)
        t="{} + {}".format(a,b)
        result=a+b


        compil_text=self.fabric.create(t)
        pos=pos-Vector2.Vector2(compil_text.get_size())/2
        return game.object.grav(compil_text,result,pos,t)


add_class(pluse)
