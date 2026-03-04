class Counter:
    def __init__(self):
        self.count = 0
        self() # -> will increase the count to 1
        
    def __call__(self):
        self.count += 1
        return self.count

# Create the object
clicker = Counter()

# Use the object like a function!
print(clicker()) # 1
print(clicker()) # 2