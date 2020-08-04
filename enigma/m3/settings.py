from m3.data import rotors, reflectors
from common.character_arrays import index

class settings:

    def __init__(self):

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

    def to_json(self):
        return { 'left_rotor': self.left_rotor.name, 'middle_rotor': self.middle_rotor.name, 'right_rotor': self.right_rotor.name,
            'reflector': self.reflector.name, 'plugboard': self.plugboard, 'ring_settings': self.ring_settings, 'rotor_settings': self.rotor_settings }
    
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

    def set_values(self, **kwargs):
        vals = vars(self)
        for key, value in kwargs.items():
            if key == 'left_rotor':
                self.left_rotor = rotors().find(value)
            if key == 'middle_rotor':
                self.middle_rotor = rotors().find(value)
            if key == 'right_rotor':
                self.right_rotor = rotors().find(value)
            if key == 'reflector':
                self.reflector = reflectors().find(value)
            if key == 'plugboard':
                plugboard = value.replace(" ", "")
                plugboard = plugboard.upper()
                if plugboard == "":
                    self.plugboard = []
                else:
                    self.plugboard = plugboard.split(",")
            if key == 'left_ring_setting':
                self.ring_settings[2] = index(value)
            if key == 'middle_ring_setting':
                self.ring_settings[1] = index(value)
            if key == 'right_ring_setting':
                self.ring_settings[0] = index(value)
            if key == 'left_rotor_setting':
                self.rotor_settings[2] = index(value)
            if key == 'middle_rotor_setting':
                self.rotor_settings[1] = index(value)
            if key == 'right_rotor_setting':
                self.rotor_settings[0] = index(value)

        return self.is_valid()
            

    def set_all_values(self, left_rotor = 'I', middle_rotor = 'II', right_rotor = 'III',
        reflector = 'B', plugboard = '', left_ring_setting = 'A', middle_ring_setting = 'A', 
        right_ring_setting = 'A', left_rotor_setting = 'A', middle_rotor_setting = 'A', 
        right_rotor_setting = 'A'):

        # takes string inputs and sets & checks values

        # set rotors and reflectors
        if left_rotor is not None:
            self.left_rotor = rotors().find(left_rotor) 
        if middle_rotor is not None:
            self.middle_rotor = rotors().find(middle_rotor)
        if right_rotor is not None:
            self.right_rotor = rotors().find(right_rotor)
        if reflector is not None:
            self.reflector = reflectors().find(reflector)

        #set plugboard
        if plugboard is not None:
            plugboard = plugboard.replace(" ", "")
            plugboard = plugboard.upper()
            if plugboard == "":
                self.plugboard = []
            else:
                self.plugboard = plugboard.split(",")
            
        # ring settings
        if right_ring_setting is not None:
            self.ring_settings[0] = index(right_ring_setting)
        if middle_ring_setting is not None:
            self.ring_settings[1] = index(middle_ring_setting)
        if left_ring_setting is not None:
            self.ring_settings[2] = index(left_ring_setting)

        # rotor settings
        if right_rotor_setting is not None:
            self.rotor_settings[0] = index(right_rotor_setting)
        if middle_rotor_setting is not None:
            self.rotor_settings[1] = index(middle_rotor_setting)
        if left_rotor_setting is not None:
            self.rotor_settings[2] = index(left_rotor_setting)

        return self.is_valid()


