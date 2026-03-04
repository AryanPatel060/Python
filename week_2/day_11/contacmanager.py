import time

class Timer:
    def __enter__(self):
        print("Starting timer...")
        self.start = time.time()
        return self # We can return 'self' or anything else

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.4f} seconds")
        # We'll talk about the exc_* arguments next!

with Timer():
    # Simulate some work
    print(4)
    time.sleep(2)

print("after with")

print(Timer)