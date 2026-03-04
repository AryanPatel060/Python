# x = 10
# y = "hello"

# print(globals())
# x = 42

# print(globals()['__file__']) # 42
# print(globals()['__file__']) # C:\Users\aryan\2026\Python\week_1\day_5\globals_locals.py
# --------------------------------------------

# x = 100

# def my_function():
#     a = 10
#     b = 20
#     print("Inside function locals():", locals()) #{'a': 10, 'b': 20}

# my_function()

# --------------------------------------------
# def outer():
#     x = 10

#     def inner(y):
#         print(x+y)
    
#     x = x + 1
#     print(x)
#     return inner

# my_function = outer()
# my_function(4)

# --------------------------------------------


x = 10
def outer():
    x = 20
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x) # Prediction: This will print 25
outer()
print(x)     # Prediction: This will print 10
