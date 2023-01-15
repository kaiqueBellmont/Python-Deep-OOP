from typing import *

"""
Objetos são como containers, que tem estado e comportamento.
"""


class MyCar:
    # Estado / State
    def __init__(
            self: object,
            brand: str,
            model: str,
            year: int,
            speed: float = 0,
    ) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    # Comportamento
    def accelerate(self, value: Optional[int] = 5) -> None:
        self.speed += value

    # Instanciação do objeto. / Atrelando como instancia da classe MyCar


car = MyCar(
    brand="Ferrari",
    model="599XX",
    year=2010
)

print(car.speed)
car.accelerate()
print(car.speed)

"""
PS: Classes são um  como "amontoado" de funções, que se transformam em métodos
somente após terem um objeto atrelado a ela.
"""
print(type(MyCar))  # type

print(type(MyCar.accelerate))  # <class 'function'>
print(type(car.accelerate))  # <class 'method'>

print(isinstance(car, MyCar))  # True

print(MyCar.__name__)  # 'MyCar'
