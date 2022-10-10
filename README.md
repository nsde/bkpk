# 🎒 Backpack (`bkpk`)
A super simple and lightweight zip alternative. No encryption, compression or anything, just a simple file packer and unpacker using the Python builtin `pickle`. Supports files of pretty much any type.

## Commands
### Zipping a folder / Creating a backpack
- `bkpk example/`

This will create a `example.bkpk` in your current directory.

### Unzipping a backpack
- `bkpk example.bkpk`

This will create all directories and files which are stored in the backpack.
