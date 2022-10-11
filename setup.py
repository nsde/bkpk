from src.bkpk import __version__

import setuptools

setuptools.setup(
    version=__version__,
    install_requires=[ # According to https://github.com/pallets/flask/blob/main/setup.py#L3, this is needed for the GitHub dependency graph.
        'colorama==0.4.5',
        'setuptools==63.2.0'
    ],
)
