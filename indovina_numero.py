#!/usr/bin/env python3
import random


def prendi_numero():
    name = input('scrivi un numero intero: ')
    if not name.isnumeric():
        raise Exception(('Errore: hai inserito "{}" '
                         'che non è un numero. '
                         'Devi inserire un numero').format(name))
    return int(name)


def esegui(num=None):
    massimo = 1000
    if num and num > massimo:
        raise Exception('Il numero immesso non può essere maggiore di {}'.format(massimo))

    numero = num or random.randint(0, massimo)
    tentativi = 1
    while 1:
        n = prendi_numero()
        if n == numero:
            print('Complimenti hai indovinato il numero in {} tentativi'.format(tentativi))
            break
        elif n < numero:
            print('{} è minore rispetto al numero da indovinare'.format(n))
        elif n > numero:
            print('{} è maggiore rispetto al numero da indovinare'.format(n))

        if n > massimo:
            print('Attenzione, il numero da indovinare è minore di {}'.format(massimo))
        tentativi += 1


if __name__ == '__main__':
    esegui()
