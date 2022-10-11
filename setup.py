# https://github.com/pixegami/python-cli-template/blob/main/publish/setup.py
DESCRIPTION = open('src/bkpk/__init__.py').read().split('\n')[1]

import os
import setuptools

# Long Description / Markdown
with open('README.md', 'r') as f:
    long_description = f.read()

reqtxt = 'requirements.txt'

if os.path.exists(reqtxt):
    with open(reqtxt, 'r') as f:
        requirement_packages = [line.strip("\n") for line in f.readlines() if not line.startswith('#')]
    print(f'Set requirements: {requirement_packages}')

else:
    print(f'WARN Requirements file {reqtxt} not found!')
    print('No packages will be required on install.')
    requirement_packages = []

setuptools.setup(
    name='bkpk',
    summary=DESCRIPTION,
    description=DESCRIPTION,
    license='MIT',
    author="NSDE",
    author_email='mail@onlix.me',
    keywords=['backpack', 'bkpk', 'zip', 'unzip', 'package', 'backpkg', 'bkpack', 'backpk', 'bkpkg', 'compress', 'file'],
    long_description=long_description,
    description_file='README.md',
    long_description_content_type="text/markdown",
    
    python_requires='>=3.8',
    install_requires=[ # According to https://github.com/pallets/flask/blob/main/setup.py#L3, this is needed for the GitHub dependency graph.
        'colorama==0.4.5',
        'setuptools==63.2.0'
    ],
)
