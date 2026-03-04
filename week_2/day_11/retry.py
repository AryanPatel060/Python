class Retry:
    def __init__(self, attempts=3):
        self.attempts = attempts

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(self.attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            print("All attempts failed.")
        return wrapper

@Retry(attempts=3)
def unstable_network_call():
    raise ConnectionError("Network down!")

unstable_network_call()