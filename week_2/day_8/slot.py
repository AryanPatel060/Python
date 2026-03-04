import sys
from pympler import asizeof

class Standard:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Slotted:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create 100,000 instances
std_instances = [Standard(1, 2) for _ in range(100000)]  #15201160
slot_instances = [Slotted(1, 2) for _ in range(100000)] #5601048



print(asizeof.asizeof(std_instances))
print(asizeof.asizeof(slot_instances))

# Note: sys.getsizeof doesn't always account for the __dict__ size perfectly.
# A better way is to use a library like 'pympler' or check total process memory.