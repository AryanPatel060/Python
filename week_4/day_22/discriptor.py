class desc:
    def __set_name__(self,owner,name):
        self._name = name
    def __get__(self,instance,owner):
        return instance.__dict__.get(self._name)
    def __set__(self,instance,name):
        instance.__dict__[self._name] = name
        return 
    

class temp():
    name = desc()
    email = desc()

t1 = temp()
t1.name = 'aryan'
t1.email = "aryan@gmail.com"
print(t1.name) # aryan
print(t1.email) 

t2 = temp()
t2.name = 'patel'
t2.email = "patel@gmail.com"

print(t1.name) #patel
print(t1.email) 