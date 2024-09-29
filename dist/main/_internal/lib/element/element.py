import pygame
from type import event as ev
from type.Vector2 import Vector2
from type.acthion import acthion
pygame.font.init()
class element():
    def update(self,pos):
        pass
    def event(self,event,pos):
        pass
    def drow(self,serf,pos,debag=False):
        pass
class Size():
    def set_size(self,size):
        self.size= Vector2(size)
    def get_size(self):
        return self.size


class posithion(element):
    def __init__(self, pos, element):
        pos=Vector2(pos)
        self.pos=pos
        self.element=element
    def update(self,pos):
        self.element.update(pos+self.pos)
    def event(self,event:ev.event,pos):
        self.element.event(event.minus(self.pos),pos+self.pos)
    def drow(self,serf,pos,debag=False):
        self.element.drow(serf,pos+self.pos)
    def set_pos(self,pos):
        self.pos=Vector2(pos)

class Show(posithion):
    def __init__(self, element):
        super().__init__([0,0],element)
        self.show=True
    def set_show(self,show):
        self.show=show
    def update(self,pos):
        if self.show:
            self.element.update(pos+self.pos)
    def event(self,event:ev.event,pos):
        if self.show:
            self.element.event(event.minus(self.pos),pos+self.pos)
    def drow(self,serf,pos,debag=False):
        if self.show:
            self.element.drow(serf,pos+self.pos)
class grup_object(element):
    def __init__(self):
        self.object=[]
    def drow(self,serf,pos=Vector2(0,0),debag=False):

        super().drow(serf,pos)
        for i in self.object:

            i.drow(serf,pos,debag)
    def update(self,pos=Vector2(0,0)):
        super().update(pos)
        for i in self.object:
            i.update(pos)
    def event(self,event,pos=Vector2(0,0)):
        super().event(event,pos)
        for i in self.object:
            i.event(event,pos)
class Text(element,Size):
    def __init__(self, text:str, font_size:int, color:list[3]):
        super().__init__()
        self.__text = text
        self.__font_size = font_size
        self.__color = color
        self.__font = pygame.font.Font(None, self.__font_size)
        self._rendered_text = self.__font.render(self.__text, True, self.__color)
    def set_text(self, text):
        self.__text = text
        self._rendered_text = self.__font.render(self.__text, True, self.__color)
    def font(self):
        return self.__font
    def set_font_size(self, font_size):
        self.__font_size = font_size
        self.__font = pygame.font.Font(None, self.__font_size)
        self._rendered_text = self.__font.render(self.__text, True, self.__color)
    def _get_text(self):
        return self.__text
    def set_color(self, color):
        self.__color = color
        self._rendered_text = self.__font.render(self.__text, True, self.__color)
    def get_size(self):
        size=self._rendered_text.get_size()
        return Vector2(size)
    def drow(self, screen,pos,debag=False):
        screen.blit(self._rendered_text, pos.get_pos())

class Button(grup_object,Size):
    def __init__(self,size):
        super().__init__()
        self.set_size(size)
        self.rect=pygame.Rect([0,0,*self.size.get_pos()])
        self.clic=acthion()
        self.in_button=False
    def event(self,event,pos):

        if ev.clic.is_me(event):
            if self.in_button:
                if event.down(1):
                    self.clic.invock()
        elif ev.movedawn.is_me(event):
            self.in_button=self.rect.collidepoint(event.get_pos())

class Ract(element,Size):
    def __init__(self, size, color):
        super().__init__()
        self.set_size(size)
        self.color=color
        self.width=0
    def set_color(self,color):
        self.color=color
    def drow(self,serf,pos,debag=False):
        super().drow(serf,pos)
        pygame.draw.rect(serf,self.color,[list(pos),self.size.get_pos()],self.width)
class Line(element,Size):
    def __init__(self,size,color,width):
        super().__init__()
        self.set_size(size)
        self.color=color
        self.width=width
    def drow(self,serf,pos,debag=False):
        pygame.draw.line(serf, self.color,pos.get_pos(),(pos+self.size).get_pos(),self.width)
class Serfase(grup_object,Size):
    def __init__(self, size):
        self.alpha=255
        self.set_size(size)
        super().__init__()
        self.serf=pygame.Surface(self.size.get_pos())

        self.color=None
        self.show=True
        self.showotherlines=False
        self.Ract=Ract(size,[0,0,0])
        self.Ract.width=1
        self.set_alpha(255)
    @staticmethod
    def get_serf(serf):
        element=Serfase(serf.get_size())
        element.serf=serf
        return element
    def set_otherlines(self,show):
        self.showotherlines=show
    def set_color(self,color=None):
        if color != None:
            if len(color)!=3:
                raise ValueError("len color != 3")
            for i in color:
                if type(i)!=int:
                    raise ValueError(f"no int: {i}")
        self.color=color
    def set_alpha(self,alpha):
        self.alpha=alpha
        self.serf.set_alpha(self.alpha)
    def set_show(self,show):
        self.show=show
    def get_show(self):
        return self.show
    def set_size(self,size):
        self.size=Vector2(size)
        self.serf=pygame.Surface(self.size.get_pos())
        self.set_alpha(self.alpha)
    def drow(self,serf,pos,debag=False,posed=Vector2(0,0)):

        if self.show:

            if self.color!=None:
                self.serf.fill(self.color)
            super().drow(self.serf,posed,True)
            if self.showotherlines:
                self.Ract.drow(self.serf,Vector2(0,0),debag)
            serf.blit(self.serf, pos.get_pos())
    def event(self,event,pos):
        if self.show:
            super().event(event,pos)
class scroler(Serfase,Size):
    def __init__(self, size):
        super().__init__(size)
        self.xy_=Vector2(0,0)
        self.chenge=acthion()
        self.block(True,True)
        self.rangex()
        self.rangey()
        self.work=False
        self.hover=False
    def block(self,x:bool=True,y:bool=True):
        self.blok=Vector2(int(x),int(y))
    def rangex(self,min=None,max=None):
        self.vecx=(min,max)
    def rangey(self,min=None,max=None):
        self.vecy=(min,max)
    def event(self,event,pos):
        if ev.clic.is_me(event):
            if event.down(1) and self.hover:
                self.work=True
            elif event.up(1):
                self.work=False
        if ev.movedawn.is_me(event):
            self.hover=pygame.Rect(Vector2(0,0),self.size ).collidepoint(event.get_pos())
            if self.work:
                self.xy_+=event.get_rel()
                self.xy_=self.corect(self.xy_)

                self.chenge.invock(Vector2(self.xy_))
        super().event(event.minus(self.xy_),pos+self.xy_)
    def corect(self,xy):
        xy=Vector2(xy.x*self.blok.x,xy.y*self.blok.y)

        if self.vecx[0] !=None:
            if self.vecx[0]<xy.x:
                xy.x=self.vecx[0]
        if self.vecx[1] !=None:
            if self.vecx[1]>xy.x:
                xy.x=self.vecx[1]
        if self.vecy[0] !=None:
            if self.vecy[0]>xy.y:
                xy.y=self.vecy[0]
        if self.vecy[1] !=None:
            if self.vecy[1]<xy.y:
                xy.y=self.vecy[1]
        return xy
    def update(self,pos):
        super().update(pos+self.xy_)
    def drow(self,serf,pos,debag=False):
        super().drow(serf, pos,debag,self.xy_)
class scrolbar(grup_object,Size):
    def __init__(self,size,sizescrol,bg,color):
        super().__init__()
        self.set_size(size)
        self.object.append(Ract(self.size,bg))
        self.sizescrol=Vector2(sizescrol).get_pos()
        self.rect=pygame.Rect([0,0,*self.sizescrol])
        self.pos=0
        self.scrol=posithion(Vector2(0,self.pos),Ract(sizescrol,color))
        self.object.append( self.scrol)
        self.chengebar=acthion()
    def event(self,event,pos):
        if ev.movedawn.is_me(event):
            if event.down(1):
                if self.rect.collidepoint(event.get_start().get_pos()):
                    self.pos+=event.get___offset().y
                    self.pos=self.corect(self.pos)
                    self.scrol.set_pos(Vector2(0,self.pos))
                    self.rect.y=self.pos
                    self.chengebar.invock(self.prosent())
    def corect(self,y):
        if 0>y:
            y=0
        if self.size.y-self.sizescrol[1]<y:
            y=self.size.y-self.sizescrol[1]
        return y
    def prosent(self):
        return self.pos*100/(self.size.y-self.sizescrol[1])
