class Grandparent:
    def process(self):
        print("👴 Grandparent processing...")

class ParentB(Grandparent):
    def process(self):
        print("👨 Parent B processing...")

class ParentC(Grandparent):
    def process(self):
        print("👩 Parent C processing...")

# The Diamond!
class Child(ParentB, ParentC):
    pass

# --- 1. Let's look at the MRO Queue ---
print("--- MRO Queue ---")
for cls in Child.mro():
    print(cls.__name__)

# --- 2. Let's execute the method ---
print("\n--- Execution ---")
obj = Child()
obj.process()