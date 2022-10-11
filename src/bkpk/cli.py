import sys
import webbrowser
import colorama

import __init__

from . import pack
from . import unpack
from . import helpers

def main():
    arg = sys.argv
    print(arg)

    if len(arg) == 1:
        print(f'{colorama.Fore.BLUE}Welcome to Backpack (bkpk)!')

        if helpers.query_yes_no('Do you need help? [y=yes|n=no]\nIf so, this project\'s documentation will be opened in a browser.', default='no'):
            webbrowser.open('https://github.com/nsde/bkpk/blob/master/README.md#commands')
            print('Try pressing CTRL+C if you can\'t access the terminal properly.')
        else:
            print('If you experience issues while trying to use bkpk, please report them:\n→ https://github.com/nsde/bkpk/issues/new')

        sys.exit(0)

    if arg[-1].endswith(helpers.FILE_EXTENSION):
        unpack.load(arg[-1])
        print(f'{colorama.Fore.GREEN}BKPK · Unpacking successful!')
    else:
        pack.save(arg[-1])
        print(f'{colorama.Fore.GREEN}BKPK · Unpacking successful!')

    print('BKPK · Done')

main()