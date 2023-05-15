from random import shuffle


def geradorDados(num):
    dado = [x for x in range(num)]
    shuffle(dado)
    return dado


dataset0 = geradorDados(9)
dataset1 = geradorDados(5000)
dataset2 = geradorDados(10000)
dataset3 = geradorDados(50000)
dataset4 = geradorDados(100000)
dataset5 = geradorDados(500000)