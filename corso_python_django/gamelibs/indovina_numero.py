#!/usr/bin/env python3
import random

__massimo = 1000

def prendi_numero():
    name = input('scrivi un numero intero: ')
    if not name.isnumeric():
        raise Exception(('Errore: hai inserito "{}" '
                         'che non è un numero. '
                         'Devi inserire un numero').format(name))
    return int(name)


def seleziona_numero_casuale(massimo=__massimo):
    return random.randint(0, massimo)


def esegui(num=None, massimo=__massimo):
    if num and num > massimo:
        raise Exception('Il numero immesso non può essere maggiore di {}'.format(massimo))

    numero = num or seleziona_numero_casuale(massimo)
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
