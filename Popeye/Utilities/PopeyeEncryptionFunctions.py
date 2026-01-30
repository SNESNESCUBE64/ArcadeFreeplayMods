#The whole point of this is to make encrypting and decrypting the ROMs used in the unprotected
#TPP ROMs easier for the purpose of hand modifying the ROM data. It was used to write freeplay mods.

import os
from datetime import datetime
import shutil
import sys

ROM_MASK = 0x3F
ROM_LIST = ["7a","7b","7c", "7e"]
BUFFER_SIZE = 0x2000

#Sub Functions
#############################################

# TPP hardware obfuscated the address lines so they need to be "unencrypted" in order to made unencrypted ROMs.
# This was accomplished by changing the address bit order and then XOR by a MASK, for this case "ROM_MASK".
# bitorder = (15, 14, 13, 12, 11, 10, 8, 7, 6, 3, 9, 5, 4, 2, 1, 0) ^ 0x3f
# data can be re-encrypted by doing this operations backwards.
def decryptAddress(oldAddress):
    newAddress = 0xFFFF
    newAddress = oldAddress & 0xFC07 #these bits are unchanged

    newAddress = newAddress | ((oldAddress & 0x0010) >> 1) |  \
                 ((oldAddress & 0x0020) >> 1) | ((oldAddress & 0x0200) >> 4) | \
                 ((oldAddress & 0x0008) << 3) | ((oldAddress & 0x0040) << 1) | \
                 ((oldAddress & 0x0080) << 1) | ((oldAddress & 0x0100) << 1)           
    
    newAddress = newAddress ^ ROM_MASK

    return newAddress

def encryptAddress(oldAddress):
    newAddress = 0xFFFF
    oldAddress = oldAddress ^ ROM_MASK #undo the mask
    
    newAddress = oldAddress & 0xFC07 #these bits are unchanged

    newAddress = newAddress | ((oldAddress & 0x0008) << 1) |  \
                 ((oldAddress & 0x0010) << 1) | ((oldAddress & 0x0020) << 4) | \
                 ((oldAddress & 0x0040) >> 3) | ((oldAddress & 0x0080) >> 1) | \
                 ((oldAddress & 0x0100) >> 1) | ((oldAddress & 0x0200) >> 1)

    return newAddress

# TPP hardware also "encrypted" ROM data by shifting bits around.
# bitorder = (3, 4, 2, 5, 1, 6, 0, 7)
# data can be re-encrypted by doing this operations backwards.
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
def getDecryptedBuffer(filename):
    buffer = [0xFF] * BUFFER_SIZE
    obfuscatedBuffer = [0xFF] * BUFFER_SIZE


    with open(filename,"rb") as openedFile:
        for addressCounter in range(BUFFER_SIZE):
            buffer[addressCounter] = int.from_bytes(openedFile.read(1))

    for addressCounter in range(BUFFER_SIZE):
        obfuscatedAddress = decryptAddress(addressCounter)
        obfuscatedBuffer[addressCounter] = decryptROMData(buffer[obfuscatedAddress])

    return obfuscatedBuffer

#This returns a encrypted ROM buffer that aligns both addresses and data as the eproms are supposed to be read.
#With an encrypted ROM buffer, a ROM can be burnt for use on the game board.
def getEncryptedBuffer(filename):
    buffer = [0xFF] * BUFFER_SIZE
    obfuscatedBuffer = [0xFF] * BUFFER_SIZE


    with open(filename,"rb") as openedFile:
        for addressCounter in range(BUFFER_SIZE):
            buffer[addressCounter] = int.from_bytes(openedFile.read(1))

    for addressCounter in range(BUFFER_SIZE):
        obfuscatedAddress = encryptAddress(addressCounter)
        obfuscatedBuffer[addressCounter] = encryptROMData(buffer[obfuscatedAddress])

    return obfuscatedBuffer

#Writes a given buffer to a filepath.
def writeROMData(path, buffer):
    with open(path,"wb") as openedFile:
        for byte in buffer:
            openedFile.write(byte .to_bytes(1, 'little', signed=False))

#Makes a backup of both the encrypted and decrypted ROMs.
def makeBackup(base_dir):
    folderName = "Backup_" + str(int(round(datetime.now().timestamp())))
    path = os.path.join(base_dir, folderName)
    
    if not os.path.exists(path):
        os.makedirs(path) 
    
    for filename in ROM_LIST:
        encFile = os.path.join(base_dir, filename)
        decFile = os.path.join(base_dir, filename + "_Decrypted")
        if os.path.exists(encFile):
            shutil.copy(encFile,path)
        if os.path.exists(decFile):
            shutil.copy(decFile,path)


#Main program
#############################################
base_dir = os.path.dirname(os.path.abspath(__file__))

makeBackup(base_dir)

if len(sys.argv) > 1:
    #check arguements
    if (sys.argv[1] == "-e"):
        #encrypt the roms
        for filename in ROM_LIST:
            obfuscatedBuffer = getEncryptedBuffer(os.path.join(base_dir, filename + "_Decrypted"))
            writeROMData(os.path.join(base_dir, filename), obfuscatedBuffer)
    elif (sys.argv[1] == "-d"):
        #decrypt the roms
        for filename in ROM_LIST:
            obfuscatedBuffer = getDecryptedBuffer(os.path.join(base_dir, filename))
            writeROMData(os.path.join(base_dir, filename + "_Decrypted"), obfuscatedBuffer)
else:
    #Assume decryption
    for filename in ROM_LIST:
        obfuscatedBuffer = getDecryptedBuffer(os.path.join(base_dir, filename))
        writeROMData(os.path.join(base_dir, filename + "_Decrypted"), obfuscatedBuffer)
