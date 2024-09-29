import pygame.math
import pygame
class event():
    @staticmethod
    def is_me(object):
        return event==type(object)
    def minus(self,pos):
        return event()
class pos():
    def __init__(self,event:[pygame.event.Event,pygame.math.Vector2],rel=None):
        if isinstance(event,pygame.event.Event):
            self.pos=pygame.math.Vector2(event.pos)
            self.rel=pygame.math.Vector2(event.rel)
        elif isinstance(rel,pygame.math.Vector2) and isinstance(event,pygame.math.Vector2):
            self.pos=event
            self.rel=rel
        elif isinstance(event,pygame.math.Vector2):
            self.pos=event
            self.rel=pygame.math.Vector2(0,0)
    def __mul__(self, other):
        if isinstance(other,pos):
            return pos(self.pos-other.pos,self.rel)
        elif isinstance(other,pygame.math.Vector2):
            return pos(self.pos-other,self.rel)
        elif isinstance(other,list):
            return pos(self.pos-pygame.math.Vector2(other),self.rel)
    def get_pos(self):
        return self.pos
    def get_rel(self):
        return self.rel
    def minus(self,pos):
        return self.__mul__(pos)
    @staticmethod
    def is_me(object):
        return pos==type(object)
class clic():
    def __init__(self,event:pygame.event):
        self.button=event.button
        self.isdown=event.type==pygame.MOUSEBUTTONDOWN
    def up(self,button):
        return not self.isdown and self.button==button
    def down(self,button):
        return self.isdown and self.button==button
    def minus(self,pos):
        return self
    @staticmethod
    def is_me(object):
        return clic==type(object)
class key(event):
    def __init__(self,event):
        self.key=event.key
        self.unicode=event.unicode
        self.up=event.type==pygame.KEYUP
    def minus(self,pos):
        return self
    @staticmethod
    def is_me(object):
        return key==type(object)
class MOUSEWHEEL():
    def __init__(self,event):
        self.event=event
    def get_pos(self):
        return pygame.math.Vector2(self.event.x,self.event.y)
    def minus(self,pos):
        return self
    @staticmethod
    def is_me(object):
        return MOUSEWHEEL==type(object)
def get_type(event):
    if event.type==pygame.MOUSEMOTION:
        return pos(event)
    elif event.type in [pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP]:
        return clic(event)
    elif event.type in [pygame.KEYUP,pygame.KEYDOWN]:
        ob=key(event)
        return ob
    elif event.type==pygame.MOUSEWHEEL:
        return MOUSEWHEEL(event)

