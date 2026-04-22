from customProperty import CustomProperty
 

class useCProperty:
    def __init__(self,data):
        self.data = data

    @CustomProperty
    def cprop(self):
        return self.data
    
    @cprop.setter
    def cprop(self,value):
        if value == 'name':
            raise ValueError("value can not be 'name'")
        self._cprop = value


cp1 = useCProperty('aryan')

cp1.cprop = "hello"
print(cp1.cprop)

cp1.cprop = "name"
N


    