import time
import threading

def cpu_heavy_task(n=50000000):
    """A purely mathematical, CPU-bound task."""
    while n > 0:
        n -= 1

print("--- 1. Sequential Execution ---")
start_time = time.time()

# We run the task twice, one after the other
cpu_heavy_task()
cpu_heavy_task()

seq_time = time.time() - start_time
print(f"Sequential Time: {seq_time:.4f} seconds")


print("\n--- 2. Threaded Execution ---")
start_time = time.time()

# We run the task twice, but "concurrently" using two threads
t1 = threading.Thread(target=cpu_heavy_task)
t2 = threading.Thread(target=cpu_heavy_task)

t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

thread_time = time.time() - start_time
print(f"Threaded Time:   {thread_time:.4f} seconds")