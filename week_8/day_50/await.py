import time
import asyncio

async def fetch_data(id, delay):
    print(f"Task {id}: Starting download...")
    
    await asyncio.sleep(delay) 
    
    print(f"Task {id}: Download complete!")
    return f"Data {id}"

async def main():
    start_time = time.time()
    
    # asyncio.gather() tells the Event Loop: "Run all of these at the same time!"
    results = await asyncio.gather(
        fetch_data(1, 2), # Takes 2 seconds
        fetch_data(2, 3), # Takes 3 seconds
        fetch_data(3, 1)  # Takes 1 second
    )
    
    total_time = time.time() - start_time
    print(f"\nAll tasks finished in {total_time:.2f} seconds.")
    print(f"Results: {results}")

# Start the engine!
asyncio.run(main())
#  -------------- output -------------------
# Task 1: Starting download...
# Task 2: Starting download...
# Task 3: Starting download...
# Task 3: Download complete!
# Task 1: Download complete!
# Task 2: Download complete!

# All tasks finished in 3.02 seconds.
# Results: ['Data 1', 'Data 2', 'Data 3']