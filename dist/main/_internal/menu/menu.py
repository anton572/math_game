from lib.element.constructs import grup_object,Vector2,Button,posithion,Ract,Text
from lib.event import get_type
import configurator
class const():
    size_start_button='size start button'
    size_satings_button='size settings button'
    pos_start_button='pos start button'
    pos_satings_button='pos settings button'
class menu():
    def __init__(self,conf:configurator.configurator,api):
        self.conf=conf
        self.grup=grup_object()
        self.api=api
        self.conf_manu={const.size_start_button:[200,30],const.size_satings_button:[200,30],const.pos_start_button:[0,600],const.pos_satings_button:[300,600]}


        start_button=Button(self.conf_manu[const.size_start_button])
        start_button.clic+=lambda :self.create()
        self.grup.object.append(posithion(self.conf_manu[const.pos_start_button],start_button))
        r=Ract(self.conf_manu[const.size_start_button],[200,200,200])
        start_button.object.append(r)
        text=Text("Играть",30,self.conf.get("color start",[255,50,20]))
        start_button.object.append(posithion([self.conf_manu[const.size_start_button][0]/2-text.get_size().x/2,0],text))

        satings_button=Button(self.conf_manu[const.size_satings_button])
        satings_button.clic+=lambda :self.api.satings()
        self.grup.object.append(posithion(self.conf_manu[const.pos_satings_button],satings_button))

        r=Ract(self.conf_manu[const.size_satings_button],[200,200,200])
        satings_button.object.append(r)
        text=Text("Настройки", 30, self.conf.get("color satings", [255, 50, 20]))
        satings_button.object.append(posithion([self.conf_manu[const.size_satings_button][0]/2-text.get_size().x/2,0],text))
        print(self.grup.object)
    def create(self):
        self.api.create_game()
    def updata(self):
        self.grup.update(Vector2.zero)
    def event(self,event):
        ev=get_type(event)
        if ev!=None:
            self.grup.event(ev,Vector2.zero)
    def draw(self,serf):
        self.grup.drow(serf,Vector2.zero)
