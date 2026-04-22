class test:
    def __set_name__(self,owner,name):
        self.public_name = name
        self._private_name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance,self._private_name,'')
    
    def __set__(self, instance, value):
        print(f'{value} is setted')
        setattr(instance, self._private_name, value.upper())

class triel:
    username = test()
    def __init__(self,name):
        self.username = name


t1 = triel('aryan')
# print(t1.username)
