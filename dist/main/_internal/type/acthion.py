class acthion():
    def __init__(self):
        self.acthion=[]
    def __iadd__(self,other):

        if not callable(other):
            raise ValueError("funthion eror")
        self.acthion.append(other)
        return self
    def __isub__(self, other):
        if not callable(other):
            raise ValueError("funthion eror")
        self.acthion.remove(other)
        return self
    def invock(self,*a,**ka):
        for i in self.acthion:
            i(*a,**ka)




