class ReadOnlyPoint:
    def __new__(cls, x, y):
        instance = super().__new__(cls)
        # We can set things here or in init
        return instance

    def __init__(self, x, y):
        # Using __setattr__ to bypass normal assignment
        super().__setattr__('x', x)
        super().__setattr__('y', y)

    def __setattr__(self, name, value):
        raise AttributeError(f"Can't modify {name}")

p = ReadOnlyPoint(10, 20)
p.x = 30  # This will now crash!