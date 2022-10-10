from pack import *
from unpack import *
from models import *

# CLI
import sys
import helpers
import webbrowser

arg = sys.argv
print(arg)

if len(arg) == 1:
    print('Welcome to Backpack (bkpk)!')

    if helpers.query_yes_no('Do you need help? [y=yes|n=no]\nIf so, this project\'s documentation will be opened in a browser.', default='no'):
        webbrowser.open('https://github.com/nsde/bkpk/blob/master/README.md#commands')
        print('Try pressing CTRL+C if you can\'t access the terminal properly.')
    else:
        print('If you experience issues while trying to use bkpk, please report them:\n→ https://github.com/nsde/bkpk/issues/new')

    sys.exit(0)

if arg[-1].endswith(FILE_EXTENSION):
    load(arg[-1])
else:
    save(arg[-1])
    print('BKPK · Successfully created ')

print('BKPK · Done')