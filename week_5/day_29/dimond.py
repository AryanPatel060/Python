class b():
    def log(self):
        print("class b")

class c(b):
    def log(self):
        print("class c")

class d(b):
    def log(self,**kwargs):
        print("class d")
        super().log(**kwargs)

class base(d,c):
    pass

b = base()
b.log()
# ===============================================
# class d
# class c