class CustomProperty:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    
    def __get__(self,instance,owner):
        if instance is None: 
            return self

        if self.fget is None : 
            raise AttributeError("underadable")
        
        return self.fget(instance)
    
    def __set__(self,instance,value):
        if self.fset is None:
            raise AttributeError('cannot write')
        self.fset(instance,value)
    
    def setter(self, fset):
        return type(self)(self.fget,fset,self.fdel)
