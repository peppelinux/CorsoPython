#!/usr/bin/env python3
import random
import sys


class IndovinaParola:
    """Gioco: Indova la parola, con suggerimenti ed esempi"""
    def __init__(self, parola=None,
                 file_lista_parole='./lista_parole.txt'):
        parola = parola or self.get_parola_casuale()
        self.parola = parola
        self.esempio = ['*' for i in range(len(parola))]
        print(('La parola da indovinare '
               'contiene {} caratteri').format(len(parola)))

    @classmethod
    def get_parola_casuale(cls, file_lista_parole='./lista_parole.txt'):
        with open(file_lista_parole, 'r') as f:
            lista_parole = f.readlines()
        random.shuffle(lista_parole)
        pos = random.randint(0, len(lista_parole))
        return lista_parole[pos].replace('\n','')


    def confronta(self, tentativo):
        if tentativo[0] == self.parola[0]:
            print('Inizia per {}.'.format(tentativo[0]))
        elif tentativo[-1] == self.parola[-1]:
            print('Finisce per {}.'.format(tentativo[-1]))
        else:
            lettere_in_comune = []
            for lettera in tentativo:
                if lettera in self.parola:
                    lettere_in_comune.append(lettera)
            print(('{} ha {} lettere in '
                   'comune con la parola '
                   'da indovinare.').format(tentativo,
                                            len(lettere_in_comune)))


    def suggerimento(self, tentativo):
        suggerimento = input('Accetti un suggerimento? [y/n/esci]')
        if suggerimento == 'n' or not suggerimento:
            return
        elif suggerimento == 'esci':
            print(('Ti sei arreso, '
                   'la parola era {}').format(self.parola))
            sys.exit(0)

        print('Suggerimento: ', end='')
        if tentativo:
            self.confronta(tentativo)
        else:
            posizioni_nascoste = [i for i in range(len(self.esempio)) if self.esempio[i] == '*']
            posizione_casuale = random.choice(posizioni_nascoste)
            self.esempio[posizione_casuale] = self.parola[posizione_casuale]
            print(('La parola da indovinare contiene '
                   'la lettera {} : {}').format(self.parola[posizione_casuale],
                                                ''.join(self.esempio)))

    def run(self):
        cnt = 1
        while 1:
            tentativo = input('Inserisci la parola: ')
            if tentativo == self.parola:
                print(('Complimenti, hai indovinato '
                       'la parola al tentativo numero {}').format(cnt))
                break
            elif not tentativo:
                self.suggerimento(tentativo)
            elif len(tentativo) != len(self.parola):
                print(('{} contiene {} caratteri, '
                       'mentre la parola da indovinare '
                       'ne contiene {}').format(tentativo,
                                                len(tentativo),
                                                len(self.parola)))
            else:
                self.suggerimento(tentativo)
            cnt += 1


if __name__ == '__main__':
    ip = IndovinaParola()
    ip.run()
