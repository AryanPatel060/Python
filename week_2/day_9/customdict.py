class Map:
    def __init__(self, **kwargs):
        self._storage = kwargs

    def __getattr__(self, name):
        if name in self._storage:
            return self._storage[name]
        raise AttributeError(f"No such attribute: {name}")

m = Map(name="Aryan", age=21,city="ahmedabad")
print(m.name) # Aryan
print(m.city) # city
print(m.location) # Raises AttributeError