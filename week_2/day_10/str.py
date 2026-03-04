class base():
    def __str__(self):
        return "hello this is base"
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

b = base()
print(b)   # hello this is base

p = Point(1, 2)
print(p)     # (1, 2)
