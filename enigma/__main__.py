#!/usr/bin/env python3

from enigma import enigma as Enigma
from config import config as Config

if __name__ == "__main__":
    config = Config()
    en = Enigma(config)
    print(en.encrypt('helloworld'))
    