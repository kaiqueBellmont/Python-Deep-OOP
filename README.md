<h1> Start Here </h1>

- Scopes and namespaces
- Boolean truth values
- Functions and functions arguments / lambdas
- Packing and unpacking iterables
- Closures: nested scopes and free variables
- Decorators
- Sequences: Iterables e iterators
- Comprehensions (Tem que saber)
- Generators
- Context managers
- mapping types
- PEP8, PEP20, PEP257

>Python 3: Deep Dive OOP - Prerequisites
You should have some basic exposure to creating and using classes in Python

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

```
***
#### Em Breve estarei disponibilizando links e repositorios para auxiliar nos estudos de várias pessoas.
#### Link para os PDFs: [GoogleDrive](https://drive.google.com/drive/folders/1lMyJU2XelVmr_NvuPHFLRzaCoG9TCGwP?usp=sharing)
