def memoize(func):
    # The cache lives in the closure!
    cache = {} 

    def wrapper(*args):
        print(*args)
        # We use the arguments as the dictionary key
        if args in cache:
            print(f"Grabbing from cache for {args}...")
            return cache[args]
            
        print(f"Calculating for {args}...")
        result = func(*args)
        cache[args] = result
        return result
        
    return wrapper

# --- Test Drive ---
@memoize
def slow_add(a, b):
    # Imagine this takes 5 seconds
    return a + b

print(slow_add(2, 3)) # Calculates: 5
# print(slow_add(2, 3)) # Grabs from cache: 5