import asyncio
import time

async def background_worker(task_id):
    """A slow background job (e.g., sending an email or processing an image)."""
    print(f"   ⚙️ [Worker {task_id}] Started in background.")
    await asyncio.sleep(3)  # Simulating network I/O
    print(f"   ✅ [Worker {task_id}] Finished!")

async def server_handler():
    print("👤 User connected.")
    
    # 1. SCHEDULE THE TASK (Fire and Forget)
    # The moment this line runs, the Event Loop starts working on it.
    bg_task = asyncio.create_task(background_worker(1))
    
    # 2. DO OTHER THINGS
    # We do NOT await the task yet. We can immediately respond to the user!
    print("🚀 Sent 'Success 200 OK' to User in 0.01 seconds!")
    
    # Let's do some more work while the background task is running...
    for i in range(1, 7):
        print(f"🖥️ Server doing other stuff... ({i}s)")
        await asyncio.sleep(1) 
        
    # 3. CLEAN UP (Optional but recommended)
    # If we need the result of the background task, we can await it here.
    # If it's already done, this returns instantly.
    await bg_task

# Start the Event Loop
print("--- Starting Server ---")
asyncio.run(server_handler())


# --- Starting Server ---
# 👤 User connected.
# 🚀 Sent 'Success 200 OK' to User in 0.01 seconds!    
# 🖥️ Server doing other stuff... (1s)
#    ⚙️ [Worker 1] Started in background.
# 🖥️ Server doing other stuff... (2s)
# 🖥️ Server doing other stuff... (3s)
#    ✅ [Worker 1] Finished!
# 🖥️ Server doing other stuff... (4s)
# 🖥️ Server doing other stuff... (5s)
# 🖥️ Server doing other stuff... (6s)