class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}!')


print(Program.__dict__)

"""{'__module__': '__main__', 'language': 'Python', 'say_hello': <function Program.say_hello at 0x7ff4b6979ab0>, 
'__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' 
objects>, '__doc__': None} 

"""

# As we can see, the `say_hello` symbol is in the class dictionary.
# We can also retrieve it using either `getattr` or dotted notation:

print(Program.say_hello)
print(getattr(Program, 'say_hello'))
"""
(<function __main__.Program.say_hello()>,
 <function __main__.Program.say_hello()>)
"""

# And of course we can call it, since it is a callable:
Program.say_hello()  # Hello from Python!

# We can even access it via the namespace dictionary as well:
Program.__dict__['say_hello']()  # Hello from Python!
