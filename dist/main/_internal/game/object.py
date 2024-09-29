import pygame
class grav():
    def __init__(self,text,result,pos,ins):
        self.text=text
        self.result=result
        self.rect=pygame.Rect(pos,self.text.get_size())
        self.text_isol=ins
