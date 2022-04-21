import math
from asyncio.windows_events import NULL
from sqlite3 import Row


def main():
    print(diamondFormer(21))
    return

def diamondFormer(size):
    diamond = ""
    if size%2 != 0 and size > 0 and size != NULL:
        rowsize = 1
        for i in range(math.floor(size/2)):
            diamond += createRow(rowsize,size)
            rowsize = rowsize+2
        diamond += createRow(size,size)
        rowsize = rowsize-2
        for i in range(math.floor(size/2)):
            diamond += createRow(rowsize,size)
            rowsize = rowsize-2
    else: 
        print("Sorry that size was not valid")
        return False

    return diamond

def createRow(size,totalSize):
    row = ""
    for j in range(math.floor((totalSize-size)/2)):
        row += " "
    for i in range(size):
        row += "*"
    row += "\n"
    return row

main()