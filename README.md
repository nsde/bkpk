# 🎒 Backpack (`bkpk`)
A super simple and lightweight zip alternative. No encryption, compression or anything, just a simple file packer and unpacker using the Python builtin `pickle`. Supports files of pretty much any type.

## Installation
### Pip (recommended)
```
pip install bkpk
```
or
```
python -m pip install bkpk
```

### Manual (advanced users only)
```
git clone https://github.com/nsde/bkpk.git
python bkpk 
```

Please note that this won't create a shell command, so you need to write `python /home/user/Downloads/bkpk/bkpk` (replace the example with your according values!) instead of just `bkpk`. Linux users add rights to the `bkpk.sh` using `sudo chmod +x bkpk.sh` and copy the file using `sudo cp bkpk.sh /usr/bin/bkpk`

## Commands
### Zipping a folder / Creating a backpack
```
bkpk example/
```

This will create a `example.bkpk` in your current directory.

### Unzipping a backpack
```
bkpk example.bkpk
```

This will create all directories and files which are stored in the backpack.

## Python API
```py
import bkpk

bkpk.save('example/')
bkpk.load('example.bkpk')

```
