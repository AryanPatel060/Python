class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        print(f"Creating class {name}")
        print(bases)
        print(namespace)
        return super().__new__(cls, name, bases, namespace)
class Person(metaclass=MyMeta):
    pass
