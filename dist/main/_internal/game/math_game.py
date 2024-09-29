import random

from lib.element.constructs import Enter,grup_object,Vector2,posithion,Text,Serfase,Button
from lib.event import get_type
from game.Fabric import Fabric
import game.generater
import time as T
from type.update import update
import configurator
import game.physics as physics
from game.difficulty import hyperbole,get_type_colculate_of_text
def time():
    return T.time()
Vector2.zero=Vector2(0,0)
class const():
    hyperbole=hyperbole.__name__


const=const()
class math():
    def __init__(self,conf:configurator.configurator,conf_hard:configurator.configurator,generator:game.generater.basemathgenerator=game.generater.array_type["pluse"],api=None):
        self.conf=conf
        self.grupstope=grup_object()
        self.grup=grup_object()
        self.api=api

        self.size_Enter=self.conf.get("size Enter",[200,30])
        enter= Enter(self.size_Enter,'')

        enter.enter+=lambda text:self.en(text)
        self.enter=enter
        self.pos=posithion(Vector2.zero,enter)
        self.grup.object.append(self.pos)
        self.Fabric=Fabric(color=self.conf.get("color example",[255,255,255]),size=self.conf.get("size example",30))
        self.objects=[]
        self.random = random.Random()
        self.score=0
        self.fail=0
        self._pass=0

        self.generator:game.generater.basemathgenerator=generator(self.Fabric)
        self.endtime=time()

        type=get_type_colculate_of_text(conf_hard.get("type",const.hyperbole),conf_hard)
        self.timer_add_exemple=update(lambda :type.time(self._pass,self.fail,self.score))
        self.timer_steer=update(1)
        self.physics=physics.physics()
        self.pos_start=self.conf.get("pos spawn example",[200,30])
        self.speed=75
        self.timer_add_exemple.ontime+=self.add

        self.time=conf_hard.get("time game",60)
        collor=conf.get("color timer and score",[250,250,250])
        self.texttime=Text(f"time:{self.time}",20,collor)
        def mis():
            self.time-=1
        self.timer_steer.ontime+=mis
        self.timer_steer.ontime += lambda :self.texttime.set_text(f"time:{self.time}")
        self.timer_steer.ontime += self.cade
        self.score_text = Text("score:0", 20, collor)
        self.grup.object.append(self.texttime)
        self.grup.object.append(posithion([0,50],self.score_text))
        self.game_work=True
    def cade(self):
        if self.time == 0:
            self.stop()
    def stop(self):
        self.game_work=False
        h=50
        self.grupstope.object.append(posithion([0,self.size_serfase[1]//2-h//2],s:=Serfase([self.size_serfase[0],h])))
        d=self.conf.get("color bg end game",[100,100,100])
        s.set_color(d)
        s.set_otherlines(True)
        t=self.conf.get("text in end game","your score:{score}")
        siz=self.conf.get("size text end game",30)
        color=self.conf.get("color text end game",[200,200,200])
        pos=s.get_size()
        t=t.replace('{score}',f"{self.score}")
        tex=Text(t,siz,color)
        s.object.append(posithion([pos.x/2-tex.get_size().x/2,0],tex))
        size_=[200,20]

        s.object.append(posithion([pos.x/2-size_[0]/2,siz],b:=Button(size_)))
        back=self.conf.get("text end button","back")
        color=self.conf.get("color end button",[200,200,200])
        t=Text(back,20,color)
        b.object.append(posithion([size_[0]/2-t.get_size().x/2,0],t))
        b.clic+=lambda:self.api.gomane()
    def en(self,text):
        self.enter.clier()
        try:
            v=self.generator.type_to(text)
        except:
            return None
        for i in self.objects:
            if i.result==v:
                self.objects.remove(i)
                self.score+=1
                self.score_text.set_text(f"score:{self.score}")
                break
        else:
            self.fail+=1
    def add(self):
        v=Vector2(self.pos_start)

        a=self.generator.create(v)

        self.objects.append(a)
    def work(self):
        self.timer_steer.update()
        self.physics.updata()
        self.timer_add_exemple.update()
        self.grup.update(Vector2.zero)
        d = time() - self.endtime
        for i in list(self.objects):
            i.rect.y += self.speed * d
            if i.rect.y + i.rect.h >= self.size_serfase[1] - 70:
                self._pass += 1
                self.objects.remove(i)
                self.createparticle(i)
        self.endtime = time()
    def updata(self):
        if self.game_work:
            self.work()
        else:
            self.enter.clier()
            self.grupstope.update(Vector2.zero)
    def createparticle(self,element):
        l=len(element.text_isol)
        for i in range(l):
            c=element.text_isol[i]
            if c==' ':continue
            S=self.Fabric.create(c)
            offset=i*element.text.get_size()[0]/l
            self.physics.add(S,[element.rect.x+offset,element.rect.y],[self.random.uniform(-40,40),self.random.uniform(0,40)])
    def event(self,event):
        ev=get_type(event)
        if ev!=None:
            if self.game_work:
                self.grup.event(ev,Vector2.zero)
            self.grupstope.event(ev,Vector2.zero)
    def draw(self,serf):
        self.size_serfase=serf.get_size()
        self.pos.set_pos(Vector2(serf.get_size())-Vector2(serf.get_size()[0]//2+self.size_Enter[0]/2,70))
        self.grup.drow(serf,Vector2.zero)
        for i in self.objects:
            serf.blit(i.text,i.rect)
        for i in self.physics:
            serf.blit(i.object,i.pos.get_pos())
        self.grupstope.drow(serf,Vector2.zero)
