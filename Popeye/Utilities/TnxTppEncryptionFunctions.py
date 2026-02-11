#The whole point of this is to make encrypting and decrypting the ROMs used in the unprotected
#TPP ROMs easier for the purpose of hand modifying the ROM data. It was used to write freeplay mods.

import os
from datetime import datetime
import shutil
import sys

TPP2_ROM_MASK = 0x3F
TNX_ROM_MASK = 0xFC
TPP2_ROM_LIST = ["7a","7b","7c", "7e"]
TNX_ROM_LIST = ["tnx1-c.2a","tnx1-c.2b","tnx1-c.2c","tnx1-c.2d","tnx1-c.2e","tnx1-c.2f","tnx1-c.2g"]
TPP2_BUFFER_SIZE = 0x2000
TNX_BUFFER_SIZE = 0x1000

#Sub Functions
#############################################

# TPP hardware obfuscated the address lines so they need to be "unencrypted" in order to made unencrypted ROMs.
# This was accomplished by changing the address bit order and then XOR by a MASK, for this case "ROM_MASK".
# bitorder = (15, 14, 13, 12, 11, 10, 8, 7, 6, 3, 9, 5, 4, 2, 1, 0) ^ 0x3f
# data can be re-encrypted by doing this operatiuons backwards.
def TPPDecryptAddress(oldAddress):
    newAddress = 0xFFFF
    newAddress = oldAddress & 0xFC07 #these bits are unchanged

    newAddress = newAddress | ((oldAddress & 0x0010) >> 1) |  \
                 ((oldAddress & 0x0020) >> 1) | ((oldAddress & 0x0200) >> 4) | \
                 ((oldAddress & 0x0008) << 3) | ((oldAddress & 0x0040) << 1) | \
                 ((oldAddress & 0x0080) << 1) | ((oldAddress & 0x0100) << 1)           
    
    newAddress = newAddress ^ TPP2_ROM_MASK

    return newAddress

def TPPEncryptAddress(oldAddress):
    newAddress = 0xFFFF
    oldAddress = oldAddress ^ TPP2_ROM_MASK #undo the mask
    
    newAddress = oldAddress & 0xFC07 #these bits are unchanged

    newAddress = newAddress | ((oldAddress & 0x0008) << 1) |  \
                 ((oldAddress & 0x0010) << 1) | ((oldAddress & 0x0020) << 4) | \
                 ((oldAddress & 0x0040) >> 3) | ((oldAddress & 0x0080) >> 1) | \
                 ((oldAddress & 0x0100) >> 1) | ((oldAddress & 0x0200) >> 1)

    return newAddress

# TNX hardware obfuscated the address lines so they need to be "unencrypted" in order to made unencrypted ROMs.
# This was accomplished by changing the address bit order and then XOR by a MASK, for this case "ROM_MASK".
# bitorder = (15, 14, 13, 12, 11, 10, 8, 7, 0, 1, 2, 4, 5, 9, 3, 6) ^ 0xfc
# data can be re-encrypted by doing this operatiuons backwards.
def TNXDecryptAddress(oldAddress):
    newAddress = 0xFFFF
    newAddress = oldAddress & 0xFC10 #these bits are unchanged

    newAddress = newAddress | ((oldAddress & 0x0040) >> 6) | \
                 ((oldAddress & 0x0008) >> 2) | ((oldAddress & 0x0200) >> 7)  | \
                 ((oldAddress & 0x0020) >> 2) | ((oldAddress & 0x0004) << 3)  | \
                 ((oldAddress & 0x0002) << 5) | ((oldAddress & 0x0001) << 7)  | \
                 ((oldAddress & 0x0080) << 1) | ((oldAddress & 0x0100) << 1) 
    
    newAddress = newAddress ^ TNX_ROM_MASK

    return newAddress

def TNXEncryptAddress(oldAddress):
    newAddress = 0xFFFF
    oldAddress = oldAddress ^ TNX_ROM_MASK #undo the mask
    
    newAddress = oldAddress & 0xFC10 #these bits are unchanged

    newAddress = newAddress | ((oldAddress & 0x0001) << 6) | \
                 ((oldAddress & 0x0002) << 2) | ((oldAddress & 0x0004) << 7)  | \
                 ((oldAddress & 0x0008) << 2) | ((oldAddress & 0x0020) >> 3)  | \
                 ((oldAddress & 0x0040) >> 5) | ((oldAddress & 0x0080) >> 7)  | \
                 ((oldAddress & 0x0100) >> 1) | ((oldAddress & 0x0200) >> 1) 
    
    return newAddress

# TPP hardware also "encrypted" ROM data by shifting bits around.
# bitorder = (3, 4, 2, 5, 1, 6, 0, 7)
# data can be re-encrypted by doing this operatiuons backwards.
def decryptROMData(data):
    newData = 0xff
    
    newData = ((data & 0x80) >> 7) | ((data & 0x01) << 1) | \
              ((data & 0x40) >> 4) | ((data & 0x02) << 2) | \
              ((data & 0x20) >> 1) | ((data & 0x04) << 3) | \
              ((data & 0x10) << 2) | ((data & 0x08) << 4)

    return newData

def encryptROMData(data):
    newData = 0xff
    
    newData = ((data & 0x01) << 7) | ((data & 0x02) >> 1) | \
              ((data & 0x04) << 4) | ((data & 0x08) >> 2) | \
              ((data & 0x10) << 1) | ((data & 0x20) >> 3) | \
              ((data & 0x40) >> 2) | ((data & 0x80) >> 4)

    return newData

#This returns a decrypted ROM buffer that aligns both addresses and data as the machine sees it.
#With a decrypted buffer, a decrypted ROM can be written for the purpose of easier editing by humans.
def getDecryptedBuffer(filename, buffer_size, game):
    buffer = [0xFF] * buffer_size
    obfuscatedBuffer = [0xFF] * buffer_size


    with open(filename,"rb") as openedFile:
        for addressCounter in range(buffer_size):
            buffer[addressCounter] = int.from_bytes(openedFile.read(1))

    for addressCounter in range(buffer_size):
        if game == "-s":
            obfuscatedAddress = TNXDecryptAddress(addressCounter)
        else:   
            obfuscatedAddress = TPPDecryptAddress(addressCounter)

        obfuscatedBuffer[addressCounter] = decryptROMData(buffer[obfuscatedAddress])

    return obfuscatedBuffer

#This returns a encrypted ROM buffer that aligns both addresses and data as the eproms are supposed to be read.
#With an encrypted ROM buffer, a ROM can be burnt for use on the game board.
def getEncryptedBuffer(filename, buffer_size, game):
    buffer = [0xFF] * buffer_size
    obfuscatedBuffer = [0xFF] * buffer_size
    obfuscatedAddress = 0xFFFF

    with open(filename,"rb") as openedFile:
        for addressCounter in range(buffer_size):
            buffer[addressCounter] = int.from_bytes(openedFile.read(1))

    for addressCounter in range(buffer_size):
        if game == "-s":
            obfuscatedAddress = TNXEncryptAddress(addressCounter)
        else:
            obfuscatedAddress = TPPEncryptAddress(addressCounter)    
        obfuscatedBuffer[addressCounter] = encryptROMData(buffer[obfuscatedAddress])

    return obfuscatedBuffer

#Writes a given buffer to a filepath.
def writeROMData(path, buffer):
    with open(path,"wb") as openedFile:
        for byte in buffer:
            openedFile.write(byte .to_bytes(1, 'little', signed=False))

#Makes a backup of both the encrypted and decrypted ROMs.
def makeBackup(base_dir, rom_list):
    folderName = "Backup_" + str(int(round(datetime.now().timestamp())))
    path = os.path.join(base_dir, folderName)
    
    if not os.path.exists(path):
        os.makedirs(path) 
    
    for filename in rom_list:
        encFile = os.path.join(base_dir, filename)
        decFile = os.path.join(base_dir, filename + "_Decrypted")
        if os.path.exists(encFile):
            shutil.copy(encFile,path)
        if os.path.exists(decFile):
            shutil.copy(decFile,path)

#Function that only prints the arguments and how to use this script
def printArguments():
    print("Expected Arguement format: python TnxTppEncryptionFunction.py *game* *function*")
    print("Game Arguement options:")
    print("   -s          TNX ROM Set")
    print("   -p          TPP2 Unprotected ROM Set")
    print("Function arguement options:")
    print("   -e          Encrypt ROMs")
    print("   -d          Decrypt ROMs")


#Main program
#############################################
base_dir = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) > 2:
    #check arguements
    if sys.argv[1] == "-p":
        makeBackup(base_dir, TPP2_ROM_LIST)
        if (sys.argv[2] == "-e"):
            #encrypt the roms
            for filename in TPP2_ROM_LIST:
                obfuscatedBuffer = getEncryptedBuffer(os.path.join(base_dir, filename + "_Decrypted"),TPP2_BUFFER_SIZE,"-p")
                writeROMData(os.path.join(base_dir, filename), obfuscatedBuffer)
        elif (sys.argv[2] == "-d"):
            #decrypt the roms
            for filename in TPP2_ROM_LIST:
                obfuscatedBuffer = getDecryptedBuffer(os.path.join(base_dir, filename),TPP2_BUFFER_SIZE,"-p")
                writeROMData(os.path.join(base_dir, filename + "_Decrypted"), obfuscatedBuffer)
        else:
            print("Error: Bad Function Argument")
            printArguments()
    elif sys.argv[1] == "-s":
        makeBackup(base_dir, TNX_ROM_LIST)
        if (sys.argv[2] == "-e"):
            #encrypt the roms
            for filename in TNX_ROM_LIST:
                obfuscatedBuffer = getEncryptedBuffer(os.path.join(base_dir, filename + "_Decrypted"),TNX_BUFFER_SIZE,"-s")
                writeROMData(os.path.join(base_dir, filename), obfuscatedBuffer)
        elif (sys.argv[2] == "-d"):
            #decrypt the roms
            for filename in TNX_ROM_LIST:
                obfuscatedBuffer = getDecryptedBuffer(os.path.join(base_dir, filename),TNX_BUFFER_SIZE,"-s")
                writeROMData(os.path.join(base_dir, filename + "_Decrypted"), obfuscatedBuffer)
        else:
            print("Error: Bad Function Argument")
            printArguments()
    else:
        print("Error: Bad Game Argument")
        printArguments()

elif len(sys.argv) > 1:
    if sys.argv[1] == "-help":
        printArguments()
    else:
        print("Error: Invalid Arguements")
        printArguments()

else:
    print("Error: Invalid Arguements")
    printArguments()
