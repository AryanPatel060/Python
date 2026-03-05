# ====== basic class flow ======= 
class sub():
    pass

s1 = sub()
print(type(s1)) #<class '__main__.sub'>

# ======= normal type behviour ========
n = 5
print(type(n))  #<class 'int'>


# ===== this is the function premade ============
def add(a , b):
    return a + b

#============== dynamic class creation ===========
math = type("math",(),{'add':add})
print(math)      #<class '__main__.math'>

print(math.add(5,4))  # 9






