import time
import multiprocessing

def cpu_heavy_task(n=50000000):
    """A purely mathematical, CPU-bound task."""
    while n > 0:
        n -= 1

if __name__ == '__main__':
    print("--- 1. Sequential Execution ---")
    start_time = time.time()

    # Run sequentially
    cpu_heavy_task()
    cpu_heavy_task()

    seq_time = time.time() - start_time
    print(f"Sequential Time: {seq_time:.4f} seconds")


    print("\n--- 2. Multiprocessing Execution ---")
    start_time = time.time()

    # We spawn separate PROCESSES, not threads!
    p1 = multiprocessing.Process(target=cpu_heavy_task)
    p2 = multiprocessing.Process(target=cpu_heavy_task)

    p1.start()
    p2.start()

    # Wait for both independent programs to finish
    p1.join()
    p2.join()

    process_time = time.time() - start_time
    print(f"Multiprocessing Time: {process_time:.4f} seconds")