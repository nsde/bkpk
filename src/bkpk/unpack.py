import os
import sys
import pickle

from . import models

def reconstruct(name: str, package: dict) -> dict:
    """Creates all files and folders from a root folder name and package dictionary."""

    for path, content in package.items():
        path = f'{name}/{path}'

        if content is models.Directory:
            os.makedirs(path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)

            with open(path, 'wb') as fp:
                fp.write(content)

def load(target: str):
    """Wrapper for reconstruct()"""
    name = target.replace(models.FILE_EXTENSION, '')

    with open(target, 'rb') as fp:
        return reconstruct(name, pickle.load(fp))

if __name__ == '__main__':
    reconstruct(sys.argv[1])
