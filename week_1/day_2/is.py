a = [1, 2, 3]
b = [1, 2, 3]

# print(a == b) # True (They look the same)
# print(a is b) # False (They are different lists in different memory spots)

c = 255
d = 255

# print(c == d) #true
# print(c is d) #true

# a = (1,285858,3,4)
# b = [1,285858,3,4]

# print(a is b) # false
# print(a == b) # false

# print(a[1] == b[1]) # True (They look the same)
# print(a[1] is b[1]) # True 

# a = (1, 285858, 3, 4)

# x = 285858
# b = [1, x, 3, 4]

# print(a[1] is b[1])  # VERY likely False


# def f(a):
#     return a + 285858

# a = (1, f(), 3, 4)
# b = [1, f(), 3, 4]

# print(f(3))  # False
# print(f(3))  # False


def add(a ,b):
    return a +b

a = 3000
b = 7000
c = 10000

print(id(add(a, b))) #2641738326416
print(id(add(b ,a))) #2641738326384
print(id(c))         #2641738320720

print(add(a,b) is add(b,a)) # False
print(add(a,b) == add(b,a)) # True







