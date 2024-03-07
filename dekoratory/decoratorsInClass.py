import time


class DecoratorsInClass:

    def __init__(self, roles):
        self.roles = roles

    def measure_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} wykonano w czasie: {end_time - start_time} sekundy")
            return result

        return wrapper

    def autorization(self, func):
        def inner(*args, **kwargs):
            print(f"User has roles: {self.roles}")
            return func(*args, **kwargs)

        return inner

    @measure_time
    def example_function(self):
        time.sleep(2)
        print("Zakończono przykładową funkcję")

    @autorization
    def example_function2(self):
        print("Zakończono przykładową funkcję")


# example
d = DecoratorsInClass(roles=["admin", "user"])
d.example_function()
d.example_function2()
# output
