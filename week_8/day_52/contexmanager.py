import asyncio
import time

class AsyncDatabaseConnection:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connected = False

    # 1. ASYNC ENTER: Establishing the connection
    async def __aenter__(self):
        print(f"🔌 [Connecting] Reaching out to {self.db_url}...")
        
        # We can AWAIT inside the enter method! The Event Loop doesn't freeze.
        await asyncio.sleep(1) 
        
        self.connected = True
        print(f"✅ [Connected] Successfully joined {self.db_url}.")
        
        # Return the object so it can be assigned to the 'as' variable
        return self

    # 2. ASYNC EXIT: Tearing down the connection
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"🛑 [Disconnecting] Closing connection to {self.db_url}...")
        
        # We can AWAIT the teardown process too!
        await asyncio.sleep(0.5) 
        
        self.connected = False
        
        # If an error occurred inside the block, we can log it here
        if exc_type:
            print(f"   ⚠️ Connection closed due to error: {exc_val}")

    # 3. A normal async method to do the actual work
    async def fetch_data(self):
        if not self.connected:
            raise ConnectionError("Cannot fetch data without a connection!")
        
        print("   📥 Fetching data from database...")
        await asyncio.sleep(1)
        return {"user": "aryan", "status": "active"}
    

async def handle_user_request(request_id):
    print(f"🌐 Request {request_id} received.")
    
    # We use 'async with' to safely handle the connection lifecycle
    async with AsyncDatabaseConnection(f"db_node_{request_id}") as db:
        data = await db.fetch_data()
        print(f"   📊 Request {request_id} got data: {data}")
        
        if request_id == 2:
   
            raise RuntimeError("Something went wrong in the app!")

async def main():
    start = time.time()

    await asyncio.gather(
        handle_user_request(1),
        handle_user_request(2),
        handle_user_request(3),
        return_exceptions=True
    )
    
    print(f"\n⏱️ All traffic handled in {time.time() - start:.2f} seconds.")

# Boot the Event Loop
asyncio.run(main())