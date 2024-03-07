import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} wykonano w czasie: {end_time - start_time} sekundy")
        return result

    return wrapper


@measure_time
def example_function():
    time.sleep(2)
    print("Zakończono przykładową funkcję")


example_function()


def autorization(roles):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(f"User has roles: {roles}")
            return func(*args, **kwargs)

        return inner

    return wrapper


@autorization(roles=["admin", "user"])
def example_function():
    print("Zakończono przykładową funkcję")


example_function()
