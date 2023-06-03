import threading


def my_thread_func(name):
    local_variable = "This is a local variable."
    print(f"Thread {name}: {local_variable}")


def main():
    thread1 = threading.Thread(target=my_thread_func, args=("Thread 1",))
    thread2 = threading.Thread(target=my_thread_func, args=("Thread 2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
