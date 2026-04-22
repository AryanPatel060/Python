import multiprocessing
import time

def data_producer(queue):
    """Generates raw data and pushes it to the queue."""
    for i in range(1, 4):
        print(f"📦 [Producer] Mining raw block {i}...")
        time.sleep(0.5) # Simulate work
        queue.put(f"Raw_Data_{i}")
        
    # Send a "Poison Pill" to tell the consumer we are done!
    queue.put("DONE")

def data_consumer(queue):
    """Waits for data to appear in the queue and processes it."""
    while True:
        # .get() will block (pause the process) until something arrives!
        item = queue.get()
        
        if item == "DONE":
            print("🛑 [Consumer] Received shutdown signal. Exiting.")
            break
            
        print(f"   ⚙️ [Consumer] Processing {item}...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 1. Create the shared mail carrier
    shared_queue = multiprocessing.Queue()

    # 2. Assign the processes and hand them the queue
    producer = multiprocessing.Process(target=data_producer, args=(shared_queue,))
    consumer = multiprocessing.Process(target=data_consumer, args=(shared_queue,))

    # 3. Start the factory
    consumer.start()
    producer.start()

    producer.join()
    consumer.join()