import pygame
class Fabric():
    def __init__(self,font=None,size=30,color=[0,0,0]):
        self.fornt=pygame.font.Font(font,size)
        self.color=color
    def create(self,text):
        return self.fornt.render(text,0,self.color)
