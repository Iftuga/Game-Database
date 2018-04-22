#!/usr/bin/python
# -*- coding: utf-8 -*-


Поле = {"Название игры":0, "Платформа":1, "Жанр":2, "Год выпуска":3, "Разработчик":4, "Издатель":5, "Цена":6}


def dataRead():
    """
    Read Database
    """
    f = open('./data.txt','r')
    f.read(25)
    dataStr = f.read(9999)
    i = 0
    even = 0
    j = 0
    game = []
    games = []
    while (j < len(dataStr)):
        if (dataStr[j] == '"'):
            if (even == 0):
                i = j + 1
                even += 1
            else:
                even = 0
                game.append(dataStr[i:j])
        if (dataStr[j] == ']'):
            games.append(game)
            game = []
        j+=1
    return games
        
def posMore( vvod , vivod):
    """
    Get key words and seek them
    Autor: Volkov V.D.
    """
    flag = 0
    i = 0
    games = dataRead()
    for a in games:
        isInVivod = 0
        for c in vivod:
            if (c == a):  
                isInVivod = 1
        if (not(isInVivod)):
            while (i < len(vvod)):
                for b in a:
                    if (flag != i+1):
                        if (b == vvod[i]):
                            flag+=1
                i+=1
                if (flag == len(vvod)):
                    vivod.append(a)
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
    priority = []
    nombers = {}
    games = dataRead()
    if (vvod in Поле):
        for a in games:
            priority.append(a[Поле[vvod]])
        priority = sorted(priority)
        i = 0
        for a in games:
            i = 0
            while ( a[Поле[vvod]] != priority[i] or i in nombers):
                i+=1
            nombers[i]=a
        if (order == 1):
            j = 0
            while (j < len(nombers)):
                print(nombers[j])
                j+=1      
        else:
            if (order == 0):
                j = len(nombers) - 1
                while (j > -1):
                    print(nombers[j])
                    j-=1  
            else:
                print("Incorrect input")
    else:
        print("Incorrect input")
