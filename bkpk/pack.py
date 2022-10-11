"""For creating an .bkpk file. CLI Arguments: <file>"""

import sys
import glob
import pickle

def build(origin: str) -> dict:
    """Returns an dictionary with all files from a given path."""
    result = {}

    for path in glob.iglob(origin + '**', recursive=True):
        try:
            with open(path, 'rb') as f: content = f.read()
        except IsADirectoryError: content = Directory

        path = path.replace(origin, '')

        if path:
            result[path] = content 

    return result

def save(origin: str):
    """Wrapper for build()"""
    if not origin.endswith('/'):
        origin += '/'

    result = build(origin)
    
    target = origin[:-1].split('/')[-1] + FILE_EXTENSION

    with open(target, 'wb') as fp:
        pickle.dump(result, fp)

if __name__ == '__main__':
    save(sys.argv[1])
