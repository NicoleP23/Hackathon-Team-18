#! /usr/bin/python3
from receiveCreate import FileModified

def file_modified():
    print("File Modified!")
    return False

fileModifiedHandler = FileModified(r"rfidData.txt",file_modified)
fileModifiedHandler.start()