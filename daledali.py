from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 10):
        n = randint(0, 100)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto')

def somaPar(Lista):
    soma = 0
    for valor in Lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {Lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números) 