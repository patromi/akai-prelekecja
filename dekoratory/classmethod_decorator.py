class MyClass:
    class_variable = "test"
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        #print(cls.instance_variable) # Błąd
        return cls.class_variable

print(MyClass.class_method())