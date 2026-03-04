class countmax():
    def __init__(self,count):
        self.limit = count
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.limit > self.current:
            self.current = self.current + 1
            return self.current
        raise BaseException("limit reaches")

counter = countmax(3)
for num in counter:
    print(num)