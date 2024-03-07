class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value + 10


# Użycie
obj = MyClass(value=10)
print(obj.value)
