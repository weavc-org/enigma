#!/usr/bin/env python3

from m3.rotors import rotors
from m3.enigma import enigma
from m3.settings import settings
from app import new_app

if __name__ == "__main__":
    server = new_app()
    server.run(host='0.0.0.0', port=5501)