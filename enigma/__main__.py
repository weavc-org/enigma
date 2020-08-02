#!/usr/bin/env python3

from machine.rotors import rotors
from machine.enigma import enigma
from machine.settings import settings
from app import new_app

if __name__ == "__main__":
    server = new_app()
    server.run(host='0.0.0.0', port=5500)