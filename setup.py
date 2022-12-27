import setuptools

setuptools.setup(
    install_requires=[ # According to https://github.com/pallets/flask/blob/main/setup.py#L3, this is needed for the GitHub dependency graph.
        'colorama==0.4.5',
        'setuptools==65.5.1'
    ],
)
