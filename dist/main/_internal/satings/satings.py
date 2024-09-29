from lib.element.constructs import grup_object,Vector2,Button,choice,Text,Line,Show
from lib.element.element import scroler,posithion
from lib.event import get_type
import configurator
class selected(choice.choice_element):
    def __init__(self,size,text_color=[250,250,250]):
        super().__init__(size,text_color)
        cross=grup_object()
        cross.object.append(posithion([5,5],Line([5,-10],[25,255,50],2)))
        cross.object.append(Line([5, 5], [25, 255, 50],2))
        cross_Show=Show(posithion([self.get_size().x/7*6,10],cross))
        self.object.append(cross_Show)
        self.cross_Show=cross_Show
        self.cross_Show.set_show(False)

    def setactiv(self,T):
        self.cross_Show.set_show(T)
def norm(string:str):
    if string=='None':
        return None
    return int(string)
class list(grup_object):
    def __init__(self,size,name:str,color=[255,255,255]):
        super().__init__()
        __scroller =scroler(size)

        self.__choiser=choice([size[0],30])
        self.__choiser.choice_element=selected
        self.__text=Text(name,30,color)
        self.object.append(self.__text)
        self.object.append(posithion([0,self.__text.get_size().y],__scroller))
        __scroller.block(x=False)
        __scroller.set_color([125,125,125])
        __scroller.object.append(self.__choiser)
        self.__s= __scroller
        self.ys = size[0]
    def add(self,text):

        self.__choiser.add(text)
        print(self.ys)
        self.__s.rangey(-30*(len(self.__choiser.Buttons)-1),0)
    def get(self):
        return self.__choiser.get()
    def get_indax(self):
        return self.__choiser._get_()
    def set(self,element):
        self.__choiser.set(norm(element))
import os
class satings():
    def __init__(self,conf:configurator.configurator,api,conf_menu):
        self.conf=conf
        self.grup=grup_object()
        self.api=api
        self.conf_menu=conf_menu

        color=conf.get("цвет текста в меню",[255,255,255])
        configurate=list([170,100],"общая конфигурация",color)
        for i in os.listdir("conf"):
            configurate.add(i)
        self.grup.object.append(configurate)
        difficulty = list([100, 200], "сложность",color)
        for i in os.listdir("difficulty"):
            difficulty.add(i)
        self.grup.object.append(posithion([0,220],difficulty))
        self.configurate=configurate
        self.difficulty = difficulty
        outsettings_button=Button([100,30])
        outsettings_button.object.append(Text("Назад",30,color))
        outsettings_button.clic+=lambda :self.save()
        self.grup.object.append(posithion([0, 440], outsettings_button))
        self.open()
    def save(self):
        print(self.configurate.get(),self.difficulty.get())
        self.conf_menu.set("configurate choice",self.configurate.get_indax())
        self.conf_menu.set("difficulty choice",self.difficulty.get_indax())
        self.api.setdata(self.configurate.get(),self.difficulty.get())
        print(1)
        self.api.update()
        self.api.gomane()
    def open(self):
        self.configurate.set( self.conf_menu.get("configurate choice","None"))
        self.difficulty.set(self.conf_menu.get("difficulty choice", "None"))

    def updata(self):
        self.grup.update(Vector2.zero)
    def event(self,event):
        ev=get_type(event)
        if ev!=None:
            self.grup.event(ev,Vector2.zero)
    def draw(self,serf):

        self.grup.drow(serf,Vector2.zero)
