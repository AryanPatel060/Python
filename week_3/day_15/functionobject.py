def fun(data , beta = 10):
    return data

print(fun(5))
print(fun.__name__)     # fun
print(fun.__dict__)     # {}

fun.name = "function name"
fun.power = "lightning speed"
print(fun.__dict__)     # {'name': 'function name', 'power': 'lightning speed'}
print(fun.__defaults__) # (10,)
print(fun)              # <function fun at 0x0000020B494204A0>