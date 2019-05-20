import sys
from enigma.rotor import rotor as Rotor

class config:

    def __init__(self):
        self.rotorLeft = Rotor('I')
        self.rotorMiddle = Rotor('II')
        self.rotorRight = Rotor('III')
        self.reflector = Rotor('B')
        self.plugboard = []
        self.ringSettings = [0,0,0]
        self.rotorSettings = [0,0,0]