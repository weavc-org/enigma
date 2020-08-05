class reflector:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class reflectors:
    B = reflector('B', list('YRUHQSLDPXNGOKMIEBFZCWVJAT'))
    C = reflector('C', list('FVPJIAOYEDRZXWGCTKUQSBNMHL'))
    all = [B, C]

    def __init__(self):
        self.names = []
        for l in self.all:
            self.names.append(l.name)

    def find(self, name: str):
        for l in self.all:
            if l.name == name.upper():
                return l

        return None


class rotor:
    def __init__(self, name, turnover, value):
        self.name = name
        self.turnover = turnover
        self.value = value


class rotors:
    I = rotor('I', [17], list('EKMFLGDQVZNTOWYHXUSPAIBRCJ'))
    II = rotor('II', [5], list('AJDKSIRUXBLHWTMCQGZNPYFVOE'))
    III = rotor('III', [22], list('BDFHJLCPRTXVZNYEIWGAKMUSQO'))
    IV = rotor('IV', [10], list('ESOVPZJAYQUIRHXLNFTGKDCMWB'))
    V = rotor('V', [26], list('VZBRGITYUPSDNHLXAWMJQOFECK'))
    VI = rotor('VI', [26, 13], list('JPGVOUMFYQBENHZRDKASXLICTW'))
    VII = rotor('VII', [26, 13], list('NZJHGRCXMYSWBOUFAIVLPEKQDT'))
    VIII = rotor('VIII', [26, 13], list('FKQHTLXOCBJSPDZRAMEWNIUYGV'))
    all = [I, II, III, IV, V, VI, VII, VIII]

    def __init__(self):
        self.names = []
        for l in self.all:
            self.names.append(l.name)

    def find(self, name: str):
        for l in self.all:
            if l.name == name.upper():
                return l

        return None
