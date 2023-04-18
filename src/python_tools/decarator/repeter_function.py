class Repeter:

    def repeat(num_repeats):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(num_repeats):
                    func(*args, **kwargs)

            return wrapper

        return decorator

    @repeat(num_repeats=3)
    def say_hello(name):
        print(f"Hello, {name}!")


if __name__ == "__main__":
    obj = Repeter()
    obj.say_hello("Alice")
