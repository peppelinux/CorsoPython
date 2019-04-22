import codicefiscale
import datetime


class Persona(object):
    def __init__(self, nome='', cognome='',
                 cf=None, sesso=None,
                 data_nascita=None, municipalita=None):
        """Metodo magico che assolve alla funzione di costruttore
        è un metodo che viene eseguito automaticamente in fase di creazione
        dell'oggetto
        """
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.municipalita = municipalita
        self.sesso = sesso
        self.data_nascita = data_nascita

        # controlli a seguire
        if self.data_nascita:
            # conversione su formati concessi
            for formato in ('%d/%m/%Y', '%Y-%m-%d'):
                try:
                    self.data_nascita = datetime.datetime.strptime(data_nascita, formato)
                    break
                except Exception as e:
                    print(e)
            assert self.data_nascita

        if self.sesso:
           if sesso not in ('M', 'F'):
               raise Exception('Sesso: M o F. Non {}'.format(sesso))

        if self.cf:
            assert codicefiscale.isvalid(self.cf)

        assert nome
        assert cognome


    def calcola_cf(self):
        if not self.data_nascita or \
           not self.municipalita or \
           not self.sesso:
            raise Exception('Dati mancanti')
        return codicefiscale.build(self.cognome,
                                   self.nome,
                                   self.data_nascita,
                                   self.sesso,
                                   self.municipalita)


    def verifica_cf(self, cf=None):
        return codicefiscale.isvalid(cf or self.cf)


class PersonaUnica(Persona):
    _persone = []

    def __new__(cls, *args, **kwargs):
        """new viene chiamato prima di __init__ e consente di fare un
        controllo o una modifica sugli argomenti di creazione prima della
        costruzione dell'oggetto.

        *variabile indica di usare gli elementi di una lista come argomenti
        **variabile indica di usare gli elementi di un dizionario come argomenti con nome
        """
        if kwargs in cls._persone:
            raise Exception('Questa persona esiste già')
        print("Creo una Persona")
        # super è una funzione che esegue il metodo della classe ereditata
        instance = super(PersonaUnica, cls).__new__(cls)
        cls._persone.append(kwargs)
        return instance


class ClasseStatica:
    """
    Una Classe statica presenta metodi come se fossero funzioni
    non ha accesso a self perchè non avviene alcuna inizializzazione
    """
    valori = {}


    @staticmethod
    def stampa(valore):
        print(valore)


    @classmethod
    def stampa_nuovo(cls, valore):
        """
        classmethod condidera di poter accedere a tutti gli attributi
        della classe della quale fa parte
        """
        if not valore in cls.valori.keys():
            print(valore)
            cls.valori[valore] = datetime.datetime.now()
        else:
            raise Exception('{} è stato già stampato in data {}'.format(valore,
                                                                        cls.valori[valore]))


if __name__ == '__main__':
    p = Persona(nome='giuseppe', cognome='de marco', sesso='M',
                data_nascita='2/08/1977', municipalita='D086')
    p.calcola_cf()

    p = Persona(nome='giuseppe', cognome='de marco', cf='DMRGPP77M02D086V')
    p.verifica_cf()

    # Persona unica
    p = PersonaUnica(nome='giuseppe', cognome='de marco', sesso='M')

