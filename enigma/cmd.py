from machine.rotors import rotors
from machine.enigma import enigma
from machine.settings import settings

if __name__ == "__main__":
    s = settings()
    print(enigma().encrypt("Hello World"))