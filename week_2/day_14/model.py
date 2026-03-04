class CharField():
    def __set_name__(self,owner,name):
        # print(f"setting name{name} , {owner}")
        self.name = name

    def __set__(self, instance, value):
        print(instance) #->here instance is model object
        print(self.name) #->name is username which we have set as key we can say
        instance.__dict__[self.name] = value

    # here owner is Model() class , and instance is object of that model
    def __get__(self,instance,owner):
        print(instance)
        return instance.__dict__[self.name]
    

class Model():
    username = CharField()
    url = CharField()

model = Model()
# print(model)
model.username = "aryan" 
model.url = "abc.com" 

print(model.url)
    