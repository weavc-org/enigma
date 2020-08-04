from .rotors import rotors, reflectors

class settings:

    def __init__(self):
        self.alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # set defaults
        self.left_rotor = rotors.I
        self.middle_rotor = rotors.II
        self.right_rotor = rotors.III
        self.reflector = reflectors.B
        self.plugboard = []
        self.ring_settings = [0,0,0]
        self.rotor_settings = [0,0,0]

    def __repr__(self):
        return "{ left_rotor: %s, middle_rotor: %s, right_rotor: %s, reflector: %s, plugboard: %s, ring_settings: %s, rotor_settings: %s }" % \
            (self.left_rotor.name, self.middle_rotor.name, self.right_rotor.name, self.reflector.name, self.plugboard, self.ring_settings, self.rotor_settings)

    def is_valid(self):
        errs = []
        if self.left_rotor is None:
            errs.append("left rotor not set")
        if self.middle_rotor is None:
            errs.append("middle rotor not set")
        if self.right_rotor is None:
            errs.append("right rotor not set")
        if self.reflector is None:
            errs.append("reflector not set")

        for i in self.ring_settings:
            if i < 0 or i > 25:
                errs.append("invalid value %s in ring settings" % i)

        for i in self.rotor_settings:
            if i < 0 or i > 25:
                errs.append("invalid value %s in ring settings" % i)

        m = self.is_plugboard_valid()
        if m is not None:
            errs.append(m)

        if len(errs) > 0:
            return False, errs

        return True, []

    def is_plugboard_valid(self):

        for ele in self.plugboard:
            if len(ele) != 2:
                return "invalid character sets in plugboard"

        p = ''.join(self.plugboard)
        for c in p:
            if p.count(c) > 1:
                return "duplicate characters in plugboard"

        return None


    def set_values(self, left_rotor: str, middle_rotor: str, right_rotor: str, reflector: str, plugboard: str, 
        left_ring_setting: str, middle_ring_setting: str, right_ring_setting: str, 
        left_rotor_setting: str, middle_rotor_setting: str, right_rotor_setting: str):
        
        # takes string inputs and sets & checks values

        # set rotors and reflectors
        self.left_rotor = rotors().find(left_rotor) 
        self.middle_rotor = rotors().find(middle_rotor)
        self.right_rotor = rotors().find(right_rotor)
        self.reflector = reflectors().find(reflector)

        #set plugboard
        plugboard = plugboard.replace(" ", "")
        plugboard = plugboard.upper()
        if plugboard == "":
            self.plugboard = []
        else:
            self.plugboard = plugboard.split(",")
        
        # ring settings
        self.ring_settings[0] = self.alphabet_index(right_ring_setting)
        self.ring_settings[1] = self.alphabet_index(middle_ring_setting)
        self.ring_settings[2] = self.alphabet_index(left_ring_setting)

        # rotor settings
        self.rotor_settings[0] = self.alphabet_index(right_rotor_setting)
        self.rotor_settings[1] = self.alphabet_index(middle_rotor_setting)
        self.rotor_settings[2] = self.alphabet_index(left_rotor_setting)

        return self.is_valid()

    def alphabet_index(self, s: str): 
        if s.upper() in self.alphabet:
            return self.alphabet.index(s.upper())
        
        return -1

