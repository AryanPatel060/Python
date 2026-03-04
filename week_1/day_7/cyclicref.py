import gc

class Zombie:
    def __init__(self, name):
        self.name = name
        self.friend = None

    def __repr__(self):
        return f"<Zombie {self.name}>"

# Enable automatic garbage collection
gc.enable()

print("Initial object count:", len(gc.get_objects()))

# 1️⃣ Create two objects that reference each other
z1 = Zombie("A")
z2 = Zombie("B")

z1.friend = z2
z2.friend = z1

# Keep their IDs so we can search for them later
z1_id = id(z1)
z2_id = id(z2)

print("Created zombies:", z1, z2)

# 2️⃣ Delete the names
del z1
del z2

print("\nAfter del:")
objs_after_del = gc.get_objects()

# 3️⃣ Show they are still alive in gc
zombies_still_alive = [obj for obj in objs_after_del if id(obj) in (z1_id, z2_id)]
print("Zombies still in gc.get_objects():", zombies_still_alive)

# 4️⃣ Force garbage collection
collected = gc.collect()

print("\nAfter gc.collect():")
print("Objects collected:", collected)

objs_after_gc = gc.get_objects()
zombies_after_gc = [obj for obj in objs_after_gc if id(obj) in (z1_id, z2_id)]
print("Zombies still present:", zombies_after_gc)
