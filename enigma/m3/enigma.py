from .settings import settings
import copy

class enigma:

    def __init__(self, settings = settings()):
        
        self.settings = settings

        # make copies of settings variables
        self.tmp_rotor = copy.copy(self.settings.left_rotor)
        self.fake_rotor_settings = copy.copy(self.settings.rotor_settings)
        self.fake_ring_settings = copy.copy(self.settings.ring_settings)

        # setup class variables
        self.cipher = []
        self.alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.static_rotor=0
        self.tmp_store=0
        self.offset=0
        self.tmp_store_last=0
        self.fake_rotors=[0,0,0,0]

    def encrypt(self, plaintext):

        t, errs = self.settings.is_valid()
        if t == False:
            return None, 'settings are not valid'
        
        self.plaintext = list(plaintext.upper())

        #Setup the ring settings with the fake rotors
        #Using fake rotors for this not to upset the turnover point of actual rotor values
        for i in range(0, len(self.fake_rotor_settings)):
            self.fake_rotors[i]=(self.fake_rotor_settings[i]-self.fake_ring_settings[i])%26
       
        for i in range(0,len(self.plaintext)):

            if self.plaintext[i] == " ":
                self.cipher.append(" ")
                continue

            #Update rotors
            self.rotorUpdates()

            #Character -> plugboard
            self.plaintext[i]=self.plugboardCharacter(self.plaintext[i])

            #Plugboard Character -> static rotor
            self.static_rotor = self.getAlphabetIndexNumber(self.plaintext[i], self.alphabet)

            #Static Character -> tmp_store
            self.tmp_store = self.static_rotor

            #Character -> Rotors
            self.tmp_store = self.rotor(0, False)
            self.tmp_store = self.rotor(1, False)
            self.tmp_store = self.rotor(2, False)

            #Rotors -> Reflector
            self.tmp_store = self.reflect()

            #Reflector -> Rotors
            self.tmp_store = self.rotor(2, True)
            self.tmp_store = self.rotor(1, True)
            self.tmp_store = self.rotor(0, True)

            #Rotors -> Static Rotor
            self.tmp_store = self.rotor(3, True)
        
            #Static Rotor -> Plugboard
            c=self.plugboardCharacter(self.alphabet[self.tmp_store])

            #Plugboard -> Output
            self.cipher.append(c)
            
        return ''.join(self.cipher), None 

    
    def getAlphabetIndexNumber(self, letter, a):
        #Gets index value for a letter using a, where a is any form of alphabet i.e. Rotor outputs
        for i in range(0, len(a)):
                if a[i]==letter:
                    return i
    
    def rotorUpdates(self):

        #Add one to right rotor on keypress
        self.fake_rotor_settings[0]+=1
        self.fake_rotors[0]+=1
        
        #Check if rotors have reached turnover point
        #If they have, add 1 position to them
        for i in range(0, len(self.settings.right_rotor.turnover)):
            if self.fake_rotor_settings[0] == self.settings.right_rotor.turnover[i]:
                self.fake_rotor_settings[1]+=1
                self.fake_rotors[1]+=1
                
        for i in range(0, len(self.settings.middle_rotor.turnover)):
            if self.fake_rotor_settings[1] == self.settings.middle_rotor.turnover[i]:
                self.fake_rotor_settings[2]+=1
                self.fake_rotors[2]+=1

        #If any rotors are over 25 (Z) then divide by 26 and set to remainder. Simulating a looping alphabet.
        for i in range(0, len(self.fake_ring_settings)):
            self.fake_rotor_settings[i]=self.fake_rotor_settings[i]%26
            self.fake_rotors[i]=self.fake_rotors[i]%26
        
    def rotor(self, rotorNumber, returning):

        #Put correct rotor data into a tmp_rotor variable
        if rotorNumber == 0:
            self.tmp_rotor=self.settings.right_rotor.value
        elif rotorNumber == 1:
            self.tmp_rotor=self.settings.middle_rotor.value
        elif rotorNumber == 2:
            self.tmp_rotor=self.settings.left_rotor.value
        elif rotorNumber == 3:
            self.tmp_rotor=self.alphabet

        #Work out the offset between rotors, add it to tmp_store
        self.offset = self.fake_rotors[rotorNumber]-self.tmp_store_last
        self.tmp_store=(self.tmp_store+self.offset)%26
        self.tmp_store_last=self.fake_rotors[rotorNumber]
        
        if returning == True:
            #Return journey, in on the jumbled side, out on alphabet.
            return self.getAlphabetIndexNumber(self.alphabet[self.tmp_store], self.tmp_rotor)
        else:
            #Initial journey, in on alphabet, out on the jumbled side.
            return self.getAlphabetIndexNumber(self.tmp_rotor[self.tmp_store], self.alphabet)

    def reflect(self):
        #Left rotor output -> Reflector
        self.offset=0-self.tmp_store_last
        self.tmp_store_last=0
        self.tmp_store=(self.tmp_store+self.offset)%26
        return self.getAlphabetIndexNumber(self.settings.reflector.value[self.tmp_store], self.alphabet)

    def plugboardCharacter(self, c):
        #Checks for character in plugboard settings
        for pair in self.settings.plugboard:
            if c in pair:
                if c == pair[0]:c=pair[1]
                elif c == pair[1]:c=pair[0]
        return c