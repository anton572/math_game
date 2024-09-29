from pygame.math import Vector2 as V2
class Vector2(V2):
    def __init__(self, x, y=None):

        if isinstance(x,Vector2) or isinstance(x,V2):
            super().__init__(x.x, x.y)
        elif isinstance(x,type) and isinstance(x,list):
            super().__init__(*x)
        else:
            super().__init__(x,y)
    def set_pos(self, x, y):
        self.x, self.y = x, y
    def get_pos(self):
        return self.x, self.y
    def minus(self):
        return Vector2(-self.x,-self.y)
    def __mul__(self, other):
        if isinstance(other,Vector2) or isinstance(other,V2):
            return Vector2(other.x*self.x,other.y*self.y)
        return super().__mul__(other)
    def __getattr__(self, item):

        if item[0] =='_':
            str=item[1:]
            if str[0]=='x':
                x=self.x
            elif str[0]=='y':
                x=self.y
            else:

                x=int(str[0])
            if len(str)>1:
                if str[1]=='x':
                    y=self.x
                elif str[1]=='y':
                    y=self.y
                else:
                    y=int(str[1])
            else:
                y=0
            return Vector2(x,y)


