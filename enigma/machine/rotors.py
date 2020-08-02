class reflector:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class reflectors:
    def __init__(self):
        self.B = reflector('B', list('YRUHQSLDPXNGOKMIEBFZCWVJAT'))
        self.C = reflector('C', list('FVPJIAOYEDRZXWGCTKUQSBNMHL'))

        self.all = [self.B, self.C]

    def find(self, name: str):
        for l in self.all:
            if l.name == name.upper():
                return l
        
        return None

class rotor(reflector):
    def __init__(self, name, turnover, value):
        self.name = name
        self.turnover = turnover
        self.value = value

class rotors(reflectors):
    def __init__(self):
        self.I = rotor('I', [17], list('EKMFLGDQVZNTOWYHXUSPAIBRCJ'))
        self.II = rotor('II', [5], list('AJDKSIRUXBLHWTMCQGZNPYFVOE'))
        self.III = rotor('III', [22], list('BDFHJLCPRTXVZNYEIWGAKMUSQO'))
        self.IV = rotor('IV', [10], list('ESOVPZJAYQUIRHXLNFTGKDCMWB'))
        self.V = rotor('V', [26], list('VZBRGITYUPSDNHLXAWMJQOFECK'))
        self.VI = rotor('VI', [26,13], list('JPGVOUMFYQBENHZRDKASXLICTW'))
        self.VII = rotor('VII', [26,13], list('NZJHGRCXMYSWBOUFAIVLPEKQDT'))
        self.VIII = rotor('VII', [26,13], list('FKQHTLXOCBJSPDZRAMEWNIUYGV'))

        self.all = [self.I, self.II, self.III, self.IV, self.V, self.VI, self.VII, self.VIII]