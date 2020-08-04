from m3.data import rotors
from m3.enigma import enigma
from m3.settings import settings

if __name__ == "__main__":
    s = settings()
    print(enigma(s).encrypt("aaaaa"))