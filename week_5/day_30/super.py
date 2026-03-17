class Base:
    def __init__(self):
        print("🏠 Base initialized")
        super().__init__()

class ParentB(Base):
    def __init__(self):
        print("👨 Parent B initialized")
        # You might think this calls Base.__init__...
        super().__init__() 
        print("👨 Parent B finished")

class ParentC(Base):
    def __init__(self):
        print("👩 Parent C initialized")
        super().__init__()
        print("👩 Parent C finished")

class Child(ParentB, ParentC):
    def __init__(self):
        print("👶 Child initialized")
        super().__init__()
        print("👶 Child finished")

# Let's run it!
print(f"MRO: {[c.__name__ for c in Child.mro()]}")
print("-" * 30)
c = Child()