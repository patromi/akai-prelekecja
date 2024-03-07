import time

class MyClass:
    _class_variable = "Class Variable"

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @classmethod
    def class_method(cls):
        return cls._class_variable

    @staticmethod
    def static_method():
        return "Static Method"

    @staticmethod
    def measure_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} executed in {end_time - start_time} seconds")
            return result
        return wrapper

    @staticmethod
    def handle_errors(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(f"An error occurred: {e}")
                result = None
            return result
        return wrapper

    @staticmethod
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            print(f"Function {func.__name__} called with arguments {args} and {kwargs}")
            result = func(*args, **kwargs)
            print(f"Function returned: {result}")
            return result
        return wrapper

    @staticmethod
    def repeatable(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                results = []
                for _ in range(times):
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator

@MyClass.measure_time
def example_function():
    time.sleep(2)
    print("Example function completed")

@MyClass.handle_errors
def example_function_with_error():
    result = 10 / 0  # Trigger a division by zero error
    print(f"Result: {result}")

@MyClass.log_function_call
def add_numbers(a, b):
    return a + b

@MyClass.repeatable(times=3)
def roll_dice():
    import random
    return random.randint(1, 6)

# Przykłady użycia
example_function()


example_function_with_error()
print(add_numbers(3, 5))
print(f"Dice rolls: {roll_dice()}")

x = MyClass(10)
x.class_method()