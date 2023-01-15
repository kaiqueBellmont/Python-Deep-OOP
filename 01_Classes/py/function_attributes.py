class MyClass:
    def print_me(self):
        print(f'Hi im {self}')


print(type(MyClass.print_me))  # function, ainda nao esta atrelado a nada

m = MyClass()
print(type(m.print_me))  # <class 'method'>, agora está atrelado a uma instancia

equals = m.print_me == MyClass.print_me
print(equals)  # false

# isso m.print_me() == a isso : Myclass.print_me(m)
MyClass.print_me(m)
m.print_me()

#  isso printa o endereço de memória
