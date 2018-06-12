#!/usr/bin/python
# -*- coding: utf-8 -*-


field = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
unfield = {0:"Название игры", 1:"Жанр", 2:"Платформа", 3:"Год выпуска", 4:"Цена", 5:"Разработчик", 6:"Издатель"}

def readData():
    """
    Read Database
    """
    import pickle as pi
    fin = open('data.pi', 'rb')
    data = pi.load(fin)
    return data

def writeData( data ):
    """
    Read Database
    """
    import pickle as pi
    fin = open('data.pi', 'wb')
    pi.dump(data, fin)

def addRecord(data,d):
    """
    Add in database
    """
    data.append(d) # if we will want dictionary we will create dict as POLYNA
    writeData(data)


def posMore( vvod , vivod):
    """
    Get key words and seek them
    Autor: Volkov V.D.
    """
    flag = 0
    i = 0
    games = readData()
    print(vvod)
    for a in games:
        isInVivod = 0
        for c in vivod:
            if (c == a):  
                isInVivod = 1
        if (not(isInVivod)):
            while (i < len(vvod)):
                for b in a:
                    if (flag != i+1):
                        print(b,vvod[i],b==vvod[i])
                        if (b == vvod[i]):
                            flag+=1
                i+=1
                if (flag == len(vvod)):
                    vivod.append(a)
                    print(a)
                    flag = 0
            i = 0
            flag = 0

def pos( vvod ):
    """
    Read key words and seek them
    Autor: Volkov V.D.
    """
    i = 0  
    j = 0
    lis = [] 
    vivod = []
    while (j < len(vvod)):
        if (vvod[j] == '|'):
            lis.append(vvod[i:j])
            posMore(lis,vivod)
            lis = []     
            i = j+1
        if  (vvod[j] == '&'):
            lis.append(vvod[i:j])
            i = j+1
        j+= 1
    lis.append(vvod[i:j]) 
    posMore(lis,vivod)
    for a in vivod:
        for b in a:
            print(b)   
        print()

def sort( vvod , order ):
    """
    Read key words sort
    Autor: Volkov V.D.
    """
    output = []
    priority = []
    nombers = {}
    games = readData()
    if (vvod in field):
        for a in games:
            if (vvod == "Цена"):
                priority.append(int(a[field[vvod]]))
            else:
                priority.append(a[field[vvod]])
        priority = sorted(priority)
        i = 0
        for a in games:
            i = 0
            while ( a[field[vvod]] != str(priority[i]) or i in nombers):
                i+=1
            nombers[i]=a
        if (order == 1):
            j = 0
            while (j < len(nombers)):
                output.append(nombers[j])
                j+=1      
        else:
            if (order == 0):
                j = len(nombers) - 1
                while (j > -1):
                    output.append(nombers[j])
                    j-=1  
            else:
                print("Incorrect input")
    else:
        print("Incorrect input")
    return output
