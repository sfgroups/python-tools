import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Check if the instance already exists
        if cls._instance is None:
            with cls._lock:  # Acquire the lock
                # Double-check if another thread has created the instance while waiting for the lock
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Usage example
def create_instance():
    instance = Singleton()
    print(f"Instance ID: {id(instance)}")


# Simulate multiple threads accessing the singleton
threads = []
for _ in range(5):
    thread = threading.Thread(target=create_instance)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
