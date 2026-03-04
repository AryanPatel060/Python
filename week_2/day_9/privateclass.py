class Private():
    def __init__(self):
        self.data = "this is the data"
        self._privateData = "this is private data"

    def __getattr__(self,name):
        print("attr get called")
        return f"{name} not exists"
    
    def __getattribute__(self, name):
        if name.startswith('_'):
            raise ArithmeticError(f"can not access {name}, may be its private")
        return super().__getattribute__(name)
    
p = Private()

print(p.data)  # Works fine
print(p.name)
try:
    print(p._privateData)  # Should trigger our custom error
except AttributeError as e:
    print(e)

