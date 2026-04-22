import asyncio

def func1():
    return "this is normal function"

async def func2():
    return "this is the async function"

print(func1())  # this is normal function
print(func2())  # <coroutine object func2 at 0x00000293A0D78F60>
