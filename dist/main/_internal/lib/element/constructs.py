import pyperclip
from .element import *
from type.update import update
from type import event as ev
from type.acthion import acthion
from type.Vector2 import Vector2
from lib.element.element import Serfase


class Enter(element,Size):
    ctrl=1073742048
    def __init__(self, size,text=""):
        super().__init__()
        self.set_size(size)
        self.Serfase=Serfase(self.size)
        self.Serfase.set_color([255,255,255])
        self.Text=Text(text,30,[0,0,0])
        self.Serfase.set_otherlines(True)
        pos_text=self.size//2-self.Text.get_size()//2
        pos_text=pos_text-pos_text._x+Vector2(5,0)
        self.smehi=pos_text
        self.timer=update(0.5)
        self.cursordrow=Show(Ract([2,self.size.y-10],[0,0,0]))
        self.cursordrowpos=posithion([0,0], self.cursordrow)
        def time():
            if self.selected:
                self.cursordrow.set_show( not self.cursordrow.show)
        self.timer.ontime+=time
        self.Serfase.object.append(posithion(pos_text,self.Text))
        self.corsor=0
        self.expander=Serfase([10,self.size.y])
        self.expander.set_show(False)
        self.expander.set_color([25,50,200])
        self.expander.set_alpha(130)
        self.posexpander=posithion([0,0],self.expander)
        self.Serfase.object.append(self.posexpander)
        self.corsor1=0
        self.cursordrow.set_show( False)
        self.enter=acthion()
        self.selected=False
        self.determine=False
        self.ctrl_tahe=False
        self.posthinmaus=pygame.math.Vector2(0,0)
    def drow(self,serf,pos,debag=False):
        super().drow(serf,pos,debag)
        self.Serfase.drow(serf,pos,debag)
        self.cursordrowpos.drow(serf,pos,debag)
    def update(self,pos):
        super().update(pos)
        self.timer.update()
    def event(self,event,pos):
        super().event(event,pos)

        if self.selected:
            if ev.key.is_me(event):

                if event.up:
                    self.dobis=-1
                    self.writer(event,False)
                else:
                    self.gray_event=event
                    self.writer(event)
        if ev.movedawn.is_me(event):
            self.posthinmaus = event.get_pos()

            if self.determine:
                if pygame.Rect([0,0],self.size.get_pos()).collidepoint(self.posthinmaus):

                    self.corsor= self.pos_determine(pos)

                    self.sinh()
                    max_curs = max([self.get_cursor2(), self.corsor])
                    min_curs=min([self.get_cursor2(),self.corsor])
                    self.expander.set_size(self.size_text(self.get_text()[min_curs:max_curs]))
                    self.posexpander.set_pos([self.size_text(self.get_text()[:min_curs])[0]+5,self.smehi.y-1])
        if ev.clic.is_me(event):

            if event.down(1):

                if pygame.Rect([0,0],self.size.get_pos()).collidepoint(self.posthinmaus):
                    self.selected = True
                    self.corsor1= self.pos_determine(Vector2(0,0))

                    self.expander.set_show(True)
                    self.expander.set_size([1, 1])

                    self.determine=True
                else:
                    self.selected = False
                    self.cursordrow.set_show( False)
            if event.up(1):
                self.determine=False
                self.corsor = self.pos_determine(Vector2(0,0))
                if self.corsor1==self.corsor:
                    self.expander.set_size([1,1])
                    self.expander.set_show(False)
                    self.sinh()

    def get_text(self):
        return self.Text._get_text()
    def writer(self,event,up=True):

        text = self.get_text()
        max_curs = max([self.get_cursor2(), self.corsor])
        min_curs = min([self.get_cursor2(), self.corsor])
        if up:

            if self.ctrl_tahe:
                if event.unicode=='':
                    tex=pyperclip.paste()
                    self.Text.set_text(text[0:min_curs] + tex + text[max_curs:])
                    self.set_of()
                    self.add_curs(len(tex)-(max_curs - min_curs))
                if event.unicode=="\x03":
                    pyperclip.copy(text[min_curs:max_curs])
                if event.unicode=="\x18":
                    pyperclip.copy(text[min_curs:max_curs])
                    self.Text.set_text(text[0:min_curs] +  text[max_curs:])

                    self.set_curs(min_curs)
                    self.set_of()
            else:
                if event.key==self.ctrl:
                    self.ctrl_tahe=True
                elif event.key == 13:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    if self.corsor - 1>=0:
                        self.Text.set_text(text[0:min_curs - int(not self.expander.get_show())] + text[max_curs:])
                        if self.expander.get_show():
                            self.set_curs(min_curs+1)
                        self.expander.set_show(False)
                        self.add_curs(-1)
                elif event.key == pygame.K_RIGHT:
                    self.add_curs(1)
                elif event.key == pygame.K_LEFT:
                    self.add_curs(-1)
                else:
                    self.Text.set_text(text[0:min_curs] + event.unicode + text[max_curs:])
                    self.set_of()
                    self.add_curs(-(max_curs - min_curs))
                    self.add_curs(1)
        else:
            if event.key==13:
                self.enter.invock(self.get_text())
            if event.key==self.ctrl:
                self.ctrl_tahe=False
    def clier(self):
        self.set_curs(0)
        self.Text.set_text('')
    def add_curs(self,caunt):
        self.corsor+=caunt
        self.sinh()
    def set_curs(self,count):
        self.corsor = count
        self.sinh()
    def sinh(self):
        if self.corsor<0:self.corsor=0
        lan_text=len(self.get_text())
        if self.corsor>lan_text:self.corsor=lan_text
        self.cursordrowpos.set_pos((self.size_text(self.get_text()[:self.corsor])[0]+self.smehi.x,5))
    def get_cursor2(self):
        if self.expander.get_show():
            return self.corsor1
        return self.corsor
    def set_of(self):
        self.expander.set_show(False)
    def size_text(self,text):
        return self.Text.font().render(text,False, [0, 0, 0]).get_size()
    def pos_determine(self,pos):
        text = self.get_text()
        if len(text) != 0:
            max = len(text)
            corsor = 0

            while True:
                postex = self.size_text(text[0:corsor])[0] + pos.x + 1 +self.smehi.y
                if postex <= self.posthinmaus.x:
                    corsor = corsor + 1
                    if corsor == max:
                        break
                elif postex > self.posthinmaus.x:
                    corsor = corsor
                    break
            return corsor
        return 0
class choice(element):
    class choice_element(grup_object):
        def __init__(self,size,text_color=[250,250,250]):
            super().__init__()
            size=Vector2(size)
            self.Button=Button(size)
            self.Text=Text('',int(size.y*0.9),text_color)
            self.clic=self.Button.clic
            self.object.append(self.Button)
            self.object.append(self.Text)
        def drow(self,serf,pos,debag=False):

            super().drow(serf,pos,debag)
        def set_text(self,text):

            self.Text.set_text(text)

        def setactiv(self, T):
            pass
        def get_text(self):
            return self.Text._get_text()
        def get_size(self):
            return self.Button.size

        def drow(self, serf, pos, debag=False):
            super().drow(serf, pos, debag)

    def __init__(self,size,reb=True):
        self.Buttons = []
        self.chenge = acthion()
        self.size = Vector2(size)
        self.__reb=reb
        if self.__reb:
            self.__g=None
    def add(self,text):
        choice_element=self.choice_element(self.size)
        l=len(self.Buttons)
        choice_element.set_text(text)
        def clic():
            if self.__reb:
                if self.__g!=l:
                    self.chenge.invock(l)
                    self.Buttons[self.__g].element.setactiv(False)
                    self.__g=l
                    self.Buttons[self.__g].element.setactiv(True)


            else:
                self.chenge.invock(l)

        choice_element.clic+=clic
        self.Buttons.append( posithion(self.size._0y*l,choice_element))
        print(self.Buttons)
    def set(self,indax):
        for el in self.Buttons:
            el.element.setactiv(False)
        if indax==None:

            if self.__g==None:
                self.__g=0
                self.Buttons[0].element.setactiv(True)
            return None
        self.__g=indax
        self.Buttons[indax].element.setactiv(True)
    def getindax(self,index):
        return self.Buttons[index].element.get_text()
    def get(self):
        return self.getindax(self.__g)
    def _get_(self):
        return self.__g
    def drow(self,serf,pos,debag=False):

        super().drow(serf,pos,debag)
        for i in self.Buttons:
            i.drow(serf,pos,debag)
    def update(self,pos):
        super().update(pos)
        for i in self.Buttons:
            i.update(pos)
    def event(self,event,pos):
        super().event(event,pos)
        for i in self.Buttons:
            i.event(event,pos)
class bulletin_board(scroler,Size):
    class constructor():
        def __init__(self,H):
            self.H=H
        def constructor(self,indax):
            return element()
        def pos(self,indax):
            return Vector2(indax*self.H,0)
        def get_H(self):
            return self.H
    def __init__(self,size,consructor=constructor(5)):
        super().__init__(size)
        self.constructor = consructor

    def _generate(self,indax):
        return Show(posithion(self.constructor.pos(indax),self.constructor.constructor(indax)))
    def set_max(self,max):
        self.max=max
    def update(self,pos):
        for i in range(len(self.object),self.max):
            self.object.append(self._generate(i))
        lens=len(self.object)
        for i in range(min(lens,self.max)):
            self.object[i].set_show(True)
        for i in range(self.max,lens):
            self.object[i].set_show(False)
        super().update(pos)
    def drow(self,serf,pos,debag=False):
        super().drow(serf,pos,True)
class choise_button(Serfase):
    def __init__(self,size,button_size):
        super().__init__(size)
        r=Ract(button_size,[20,50,255])
        self.button_size=button_size
        self.pos_r=posithion([0,0],r)
        self.object.append(self.pos_r)
        self.len=0
        self.set_color([255,255,255])
    def choi(self,index):
        self.pos_r.set_pos([index*self.button_size[0],0])

    def add(self,button):
        self.object.append(posithion([self.button_size[0]*self.len+2,0],button))
        len=self.len+0
        button.clic+=lambda :self.choi(len)
        self.len+=1
