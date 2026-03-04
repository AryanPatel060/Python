import gc
import sys

# 1. Create a cycle
a = {}
b = {}
a['b'] = b
b['a'] = a

# 2. Drop the main references
# del a
# del b

# 3. Manually trigger the "Specialist"
# b =gc.collect() # This returns the number of unreachable objects found/cleaned
print(sys.getrefcount(a))