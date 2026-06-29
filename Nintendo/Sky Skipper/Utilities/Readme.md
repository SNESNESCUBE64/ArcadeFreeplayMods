# Sky Skipper Encryption Utility
This is a tool that utilizes python to encrypt or decrypt the ROMs used in the arcade game Popeye. This utility is meant for use on the unprotected Revision D ROMs but may work with other revisions. It can also be used for performing the same functions on Sky Skipper ROMs.

## Usage
### Arguements
- Game
    - -s     Sky Skipper
    - -p     Popeye
- Function
    - -d     Decrypt
    - -e     Encrypt

To use this script, place the python script in the same folder as the ROMs (7a, 7b, 7c, and 7e) and execute the following in a command prompt:
```
python TnxTppEncryptionFunctions.py -s -d
```
or
```
python TnxTppEncryptionFunctions.py -s -e
```

For Windows users, batch scripts are provided for ease of use. 

## Theory of Operation
The ROMs are less encrypted and moreso obfuscated. The address and data lines are switched around in hardware so they appear jumbled in ROMs.

For the data lines, the bit order for each byte is as follows:
```
bitorder = (3, 4, 2, 5, 1, 6, 0, 7)
```

The address lines are a little bit different, the bytes have a different order but there is also a XOR operation of 0x3F. It is as follows:
```
bitorder = (15, 14, 13, 12, 11, 10, 8, 7, 0, 1, 2, 4, 5, 9, 3, 6) ^ 0xfc
 ```

 With these in mind, it is fairly simple to decrypt the ROMs for hand editing. That is how the freeplay mod was made.