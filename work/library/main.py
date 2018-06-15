#!/usr/bin/python
# -*- coding: utf-8 -*-


field = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
unfield = {0:"Название игры", 1:"Жанр", 2:"Платформа", 3:"Год выпуска", 4:"Цена", 5:"Разработчик", 6:"Издатель"}

def readData():
    """
    Автор Труханов А.И.
    Читает базу
    """
    import pickle as pi
    fin = open('../data/data.pi', 'rb')
    data = pi.load(fin)
    return data

def writeData( data ):
    """
    Автор: Гуняшов Н.Н.
    Печатает дату
    """
    import pickle as pi
    fin = open('../data/data.pi', 'wb')
    pi.dump(data, fin)

def addRecord(data,d):
    """
    Автор: Волков В.Д.
    Добавляет запись
    """
    data.append(d)
    writeData(data)


def posMore( vvod , vivod):
    """
    Автор Труханов А.И.
    Ищет по множеству параметров
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
    Автор: Гуняшов Н.Н.
    Поиск по параметрам
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
    Автор: Волков В.Д.
    Сортирует
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

def search(a,b,c,d):
    """
    Автор Труханов А.И.
    Поиск в промежутке
    """
    baseOut = []
    base = readData()
    if (len(a) > 0):
        for e in base:
            if (int(e[4]) > int(a)):
                baseOut.append(e)

    if (len(b) > 0):
        if (len(baseOut) == 0):
            for e in base:
                if (int(e[4]) < int(b)):
                    baseOut.append(e)
        else:
            base = []
            for e in baseOut:
                if (int(e[4]) < int(b)):
                    base.append(e)
        baseOut = base

    if (len(c) > 0):
        if (len(baseOut) == 0):
            for e in base:
                if (int(e[3]) > int(c)):
                    baseOut.append(e)
        else:
            base = []
            for e in baseOut:
                if (int(e[3]) > int(c)):
                    base.append(e)
        baseOut = base

    if (len(d) > 0):
        if ( len(baseOut) == 0):
            for e in base:
                if (int(e[3]) < int(d)):
                    baseOut.append(e)
        else:
            base = []
            for e in baseOut:
                if (int(e[3]) < int(d)):
                    base.append(e)
        baseOut = base
    return baseOut

def outBase( data ):
    """
    Автор: Гуняшов Н.Н.
    Выводит базу
    """
    fin = open('../output/base.txt', 'w')
    for a in data:
        for b in a:
            print(b, file=fin)
        print(file=fin)
    fin.close()

def resulttxt(data):
    """
    Автор: Волков В.Д.
    Считает ср. арифм.
    """
    fin = open('../output/result.txt', 'w')
    d=0
    summ=0
    sr=0
    disp=0
    otkl=[]
    summotkl=0
    for a in data:
        d=d+1
    print("Кол-во записей:",file=fin)
    print(d,file=fin)
    for a in data:
        summ=summ+int(a[4])
    sr=summ/d
    print("Среднее арифметическое:",file=fin)
    print(int(sr),file=fin)
    for a in data:
        otkl.append((int(sr)-int(a[4]))**2)
    for a in otkl:
        summotkl=summotkl+a
    disp=summotkl/d
    print("Дисперсия:",file=fin)
    print(int(disp),file=fin)
