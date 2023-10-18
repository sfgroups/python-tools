from fastapi import FastAPI
import threading

app = FastAPI()

# Global variable to be updated by multiple threads
global_variable = 0

# Lock to ensure thread safety when updating the global variable
global_variable_lock = threading.Lock()

# Function to update the global variable
def update_global_variable():
    global global_variable
    with global_variable_lock:
        global_variable += 1

# Define a FastAPI route that triggers the global variable update
@app.get("/update-global-variable")
async def trigger_update():
    # Create and start multiple threads to update the global variable
    num_threads = 5
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=update_global_variable)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return {"message": "Global variable updated."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
