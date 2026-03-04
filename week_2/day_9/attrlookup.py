class C:
    @property
    def x(self):
        return 42

c = C()
c.__dict__['x'] = 100

print(c.x)   # 42


class B:
    def x(self):
        return 42

b = B()
b.__dict__['x'] = 100

print(b.x)   # 100