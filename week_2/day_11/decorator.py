def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments received:", args, kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))

# @ means this get call like this  my_decorator(add)