class vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):    
        return f"value of vector is({self.x} , {self.y})"
    
    def __add__(self, other):
        return vector(self.x+other.x , self.y+other.y)
    
    def __sub__(self, other):
         return vector(self.x-other.x , self.y-other.y)
    
    def __mul__(self,scale):
        return vector(
            self.x*scale,self.y*scale
        )

v1 = vector(2,6)
v2 = vector(7,12)

v = v1-v2

print(v) # value of vector is(-5 , -6)

v = v*-2

print(v) # value of vector is(10 , 12)