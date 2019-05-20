import sys
from config import config

class enigma:

    def __init__(self, config = config()):
        self.rotors = config.rotorSettings
        self.reflector = config.reflector
        self.plugboard = config.plugboard
        self.rotorL = config.rotorLeft
        self.rotorM = config.rotorMiddle
        self.rotorR = config.rotorRight
        self.ringS = config.ringSettings

        self.cipher = []
        self.alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.staticRotor=0
        self.tmpStore=0
        self.tmpRotor=self.rotorL
        self.offset=0
        self.rotorsStorePrev=0
        self.fakeRotors=[0,0,0,0]

    def encrypt(self, plaintext):
        
        self.plaintext = list(plaintext.upper())

        #Setup the ring settings with the fake rotors
        #Using fake rotors for this not to upset the turnover point of actual rotor values
        for i in range(0, len(self.rotors)):
            self.fakeRotors[i]=(self.rotors[i]-self.ringS[i])%26
       
        for i in range(0,len(self.plaintext)):

            #Update rotors
            self.rotorUpdates()

            #Character -> plugboard
            self.plaintext[i]=self.plugboardCharacter(self.plaintext[i])

            #Plugboard Character -> static rotor
            self.staticRotor = self.getAlphabetIndexNumber(self.plaintext[i], self.alphabet)

            #Static Character -> tmpStore
            self.tmpStore = self.staticRotor

            #Character -> Rotors
            self.tmpStore = self.rotor(0, False)
            self.tmpStore = self.rotor(1, False)
            self.tmpStore = self.rotor(2, False)

            #Rotors -> Reflector
            self.tmpStore = self.reflect()

            #Reflector -> Rotors
            self.tmpStore = self.rotor(2, True)
            self.tmpStore = self.rotor(1, True)
            self.tmpStore = self.rotor(0, True)

            #Rotors -> Static Rotor
            self.tmpStore = self.rotor(3, True)
        
            #Static Rotor -> Plugboard
            c=self.plugboardCharacter(self.alphabet[self.tmpStore])

            #Plugboard -> Output
            self.cipher.append(c)
            
        return ''.join(self.cipher)

    
    def getAlphabetIndexNumber(self, letter, a):
        #Gets index value for a letter using a, where a is any form of alphabet i.e. Rotor outputs
        for i in range(0, len(a)):
                if a[i]==letter:
                    return i
    
    def rotorUpdates(self):

        #Add one to right rotor on keypress
        self.rotors[0]+=1
        self.fakeRotors[0]+=1
        
        #Check if rotors have reached turnover point
        #If they have, add 1 position to them
        for i in range(0, len(self.rotorR.turnover)):
            if self.rotors[0] == self.rotorR.turnover[i]:
                self.rotors[1]+=1
                self.fakeRotors[1]+=1
                
        for i in range(0, len(self.rotorM.turnover)):
            if self.rotors[1] == self.rotorM.turnover[i]:
                self.rotors[2]+=1
                self.fakeRotors[2]+=1

        #If any rotors are over 25 (Z) then divide by 26 and set to remainder. Simulating a looping alphabet.
        for i in range(0, len(self.rotors)):
            self.rotors[i]=self.rotors[i]%26
            self.fakeRotors[i]=self.fakeRotors[i]%26
        
    def rotor(self, rotorNumber, returning):

        #Put correct rotor data into a tmpRotor variable
        if rotorNumber == 0:
            self.tmpRotor=self.rotorR.value
        elif rotorNumber == 1:
            self.tmpRotor=self.rotorM.value
        elif rotorNumber == 2:
            self.tmpRotor=self.rotorL.value
        elif rotorNumber == 3:
            self.tmpRotor=self.alphabet

        #Work out the offset between rotors, add it to tmpStore
        self.offset = self.fakeRotors[rotorNumber]-self.rotorsStorePrev
        self.tmpStore=(self.tmpStore+self.offset)%26
        self.rotorsStorePrev=self.fakeRotors[rotorNumber]
        
        if returning == True:
            #Return journey, in on the jumbled side, out on alphabet.
            return self.getAlphabetIndexNumber(self.alphabet[self.tmpStore], self.tmpRotor)
        else:
            #Initial journey, in on alphabet, out on the jumbled side.
            return self.getAlphabetIndexNumber(self.tmpRotor[self.tmpStore], self.alphabet)

    def reflect(self):
        #Left rotor output -> Reflector
        self.offset=0-self.rotorsStorePrev
        self.rotorsStorePrev=0
        self.tmpStore=(self.tmpStore+self.offset)%26
        return self.getAlphabetIndexNumber(self.reflector.value[self.tmpStore], self.alphabet)

    def plugboardCharacter(self, c):
        #Checks for character in plugboard settings
        for pair in self.plugboard:
            if c in pair:
                if c == pair[0]:c=pair[1]
                elif c == pair[1]:c=pair[0]
                else:sys.exit("Something went wrong inside the plugboard.")
        return c