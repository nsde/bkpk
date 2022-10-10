from setuptools import setup, find_packages

setup(
    name='bkpk',
    version='0.1',
    summary='A simple Python CLI boilerplate project',
    license='MIT',
    author="NSDE",
    author_email='mail@onlix.me',
    packages=find_packages('bkpk'),
    package_dir={'': 'bkpk'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords=['backpack', 'bkpk', 'zip', 'unzip', 'package', 'backpkg', 'bkpack', 'backpk', 'bkpkg', 'compress', 'file'],
    description_file='README.md',
    scripts=['bj'],
    install_requires=[],
    home_page='https://github.com/nsde/bkpk',
    'requires_dist'
)

 = setuptools
classifier =
    Development Status :: 5 - Production/Stable
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Operating System :: OS Independent
    Programming Language :: Python
    Topic :: Software Development :: Build Tools
    Topic :: Software Development :: Libraries :: Python Modules
    Topic :: System :: Archiving :: Packaging


[options]
packages = find:
install_requires =
    click
    colorama
setup_requires =
    pytest-runner
    wheel
tests_requires =
    pytest
entry_points =
    [console_scripts]
    sample_cli=sample:cli
[options.extras_require]
dev =
    pytest
    pylint
    Sphinx
    wheel

[options.packages.find]
exclude = tests

[build_sphinx]
project = Python CLI Boilerplate Project
release = 0.1.0
copyright = Copyright 2022 Keath Milligan
config_dir = docs

[aliases]
test=pytest