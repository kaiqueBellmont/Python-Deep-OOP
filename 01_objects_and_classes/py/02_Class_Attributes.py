"""As we saw, when we create a class Python automatically builds-in properties and behaviors into our class object,
like making it callable, and properties like `__name__`. """


class MyClass:
    language = 'python'
    version = 3.6

    # getattr(object_symbol, attribute_name, optional_default)
    # getattr function


print(getattr(MyClass, 'language'))  # python
getattr(MyClass, 'x')  # AttributeError exception
# setattr function setattr(object_symbol, attribute_name, attribute_value)
# this has modified the state of MyClass à MyClass was mutated


print(MyClass.__dict__)  # class namespace
print(type(MyClass.__dict__))  # mappingproxy
m = MyClass()
print(m.__dict__)  # dict


class Person:
    pass


print(Person.__name__)  # 'Person'


# `__name__` is a **class attribute**. We can add our own class attributes easily this way:

class Program:
    language = 'Python'
    version = '3.6'


print(Program.__name__)  # 'Program'
print(Program.language)  # python
