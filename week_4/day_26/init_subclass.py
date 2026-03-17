class parent():
    def __init_subclass__(cls, **kwargs):
        print(f"object of child {cls.__name__} get created")

        if not hasattr(cls, "_getParentName"):
            print(f"child {cls} do not have method '_getParentName'")

        super().__init_subclass__(**kwargs)

    def __init__(self):
        print("parent object created")

class child1(parent):
    def _getParentName():
        pass

c1 = child1()

