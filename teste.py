import time

inicio = time.perf_counter()
print(list(filter(lambda x: x > 1000, map(lambda x: x ** 2, (x for x in range(100) if x % 2 == 0)))))
fim = time.perf_counter()
print(f'{fim - inicio} - Tempo com generator')

inicio2 = time.perf_counter()
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
         86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


def quadrado(lista: list):
    for indice, valor in enumerate(lista):
        lista[indice] = valor ** 2


def filtro(lista: list, lista_vazia):
    for x in lista:
        if x > 500:
            lista_vazia.append(x)
    return lista_vazia


lista_vazia = []

quadrado(lista)
filtro(lista, lista_vazia)
print(lista_vazia)
fim2 = time.perf_counter()
print(f'{fim2 - inicio2 < fim - inicio} - ')
