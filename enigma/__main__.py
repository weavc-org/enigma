from cmd import cmd
from web import start

import sys

if __name__ == "__main__":
    if '--web' in sys.argv:
        start()
    else:
        cmd()