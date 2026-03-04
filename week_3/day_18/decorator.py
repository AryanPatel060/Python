def retry(attempts=3):
    # Level 1: Receives the decorator arguments
    
    def decorator(func):
        # Level 2: Receives the target function
        
        def wrapper(*args, **kwargs):
            # Level 3: Receives the function's arguments (The actual execution)
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            print("All attempts exhausted.")
            
        return wrapper
        
    return decorator

# --- Test Drive ---
@retry(attempts=3)
def unstable_network():
    raise ConnectionError("Timeout!")

unstable_network()