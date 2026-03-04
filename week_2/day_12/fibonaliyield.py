def fibonaci(len):
    prev = 0
    current = 1
    while current < len:
        next = prev + current
        yield next
        prev = current
        current = next
    len = len + 1 

length = 100

for x in fibonaci(length):
    print(x)


#-----------------------------------------------
def fibonacci(limit):
    a, b = 0, 1 
    while a < limit:
        yield a
        a, b = b, a + b  
for x in fibonacci(1):
    print(x, end=" ")


#--------------------------------------------------
def infinite_fibonacci():
    a, b = 0, 1
    while True:     # This loop never ends!
        yield a
        a, b = b, a + b

# Let's create the generator object
fib_gen = infinite_fibonacci()

# We control exactly when it runs by manually calling next()
print(next(fib_gen)) # 0
print(next(fib_gen)) # 1
print(next(fib_gen)) # 1
print(next(fib_gen)) # 2

# Or, we can use a for-loop and break out of it when WE decide to
print("--- Loop Start ---")
for num in fib_gen:
    if num > 50:    # We control the exit condition here, not in the generator
        break
    print(num)