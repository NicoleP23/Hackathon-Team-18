#! /usr/bin/python3
from receiveCreate import FileModified

numSalads = 0
numCases = 0

def file_modified():
    print("File Modified!")
    return False

def resetNumSalads():
    numSalads = 0

def resetNumCases():
    numCases = 0

def getNumSalads():
    return numSalads

def getNumCases():
    return numCases

def incNumSalads():
    numSalads = numSalads + 1

def incNumCases():
    numCases = numCases + 1

def pack():
    if (getNumSalads() < 25):
        return
    else:
        # attach GTIN and SSCC to case
        incNumCases()
        resetNumSalads()

def ship():
    if (getNumCases() < 40):
        return
    else:
        # attach SSCC to pallet
        resetNumCases()






fileModifiedHandler = FileModified(r"rfidData.txt",file_modified)
fileModifiedHandler.start()


# receive raw materials (event begins upon scan)
# transform raw materials into salad (event begins upon scan of )