
class rotor:

    def __init__(self, _name = 'I'):
        self.name = ''
        self.value = list()
        self.turnover = []

        self._rotorI=list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self._rotorII=list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self._rotorIII=list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
        self._rotorIV=list('ESOVPZJAYQUIRHXLNFTGKDCMWB')
        self._rotorV=list('VZBRGITYUPSDNHLXAWMJQOFECK')
        self._rotorVI=list('JPGVOUMFYQBENHZRDKASXLICTW')
        self._rotorVII=list('NZJHGRCXMYSWBOUFAIVLPEKQDT')
        self._rotorVIII=list('FKQHTLXOCBJSPDZRAMEWNIUYGV')
        self._reflectorB=list('YRUHQSLDPXNGOKMIEBFZCWVJAT')
        self._reflectorC=list('FVPJIAOYEDRZXWGCTKUQSBNMHL')
        self.set(_name)

    def set(self, _name):
        _name=_name.upper()
        if _name == 'I': 
            self.value = self._rotorI
            self.name = 'I'
            self.turnover = [17]
        elif _name == 'II': 
            self.value = self._rotorII
            self.name = 'II'
            self.turnover = [5]
        elif _name == 'III': 
            self.value = self._rotorIII
            self.name = 'III'
            self.turnover = [22]
        elif _name == 'IV': 
            self.value = self._rotorIV
            self.name = 'IV'
            self.turnover = [10]
        elif _name=='V': 
            self.value = self._rotorV
            self.name = 'V'
            self.turnover = [26]
        elif _name == 'VI': 
            self.value = self._rotorVI
            self.name = 'VI'
            self.turnover = [26,13]
        elif _name == 'VII': 
            self.value = self._rotorVII
            self.name = 'VII'
            self.turnover = [26,13]
        elif _name=='VIII': 
            self.value = self._rotorVIII
            self.name = 'VIII'
            self.turnover = [26,13]
        elif _name == 'B': 
            self.value = self._reflectorB
            self.name = 'B'
            self.turnover = []
        elif name=='C': 
            self.value = self._reflectorC
            self.name = 'C'
            self.turnover = []