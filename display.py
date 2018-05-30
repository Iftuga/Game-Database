#!/usr/bin/python
# -*- coding: utf-8 -*-

def display():
    # first part
    import main
    import tkinter as tk
    class MainWindow:
        def __init__(self):
            self.flagSort = 0
            self.currSort = ""
            self.base = main.readData()
            self.pNG = []
            self.pP = []
            self.pG = []
            self.pY = []
            self.pD = []
            self.pPu = []
            self.pPr = []

#Поле = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
            self.posNameGame = tk.Button( root, text = "Название игры", bg = "white", fg="black")
            i = 0
            self.exit = tk.Button( root, text = "Exit", command = root.destroy, bg = "white", fg="black")
            while ( i < len(self.base)):
                self.pNG.append(tk.Entry(root))
                i = i + 1
            self.posPlat = tk.Button( root, text = "Платформа", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pP.append(tk.Entry(root))
                i = i + 1
            self.posGenre = tk.Button( root, text = "Жанр", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pG.append(tk.Entry(root))
                i = i + 1
            self.posYear = tk.Button( root, text = "Год выпуска", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pY.append(tk.Entry(root))
                i = i + 1
            self.posDevel = tk.Button( root, text = "Разработчик", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pD.append(tk.Entry(root))
                i = i + 1
            self.posPublisher = tk.Button( root, text = "Издатель", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pPu.append(tk.Entry(root))
                i = i + 1
            self.posPrice = tk.Button( root, text = "Цена", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pPr.append(tk.Entry(root))
                i = i + 1
            self.frame = tk.Frame(root)
            self.init_widget()
        def init_widget(self):
            #self.frame.place( x = 100, y = 50, width = 750, height = (len(self.base) + 1) * 25)
            self.posNameGame.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Название игры"))
            self.posNameGame.place(x = 100, y = 50, width = 125, height = 25)
            self.posPlat.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Платформа"))
            self.posPlat.place(x = 225, y = 50, width = 100, height = 25)
            self.posGenre.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Жанр"))
            self.posGenre.place(x = 325, y = 50, width = 50, height = 25)
            self.posYear.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Год выпуска"))
            self.posYear.place(x = 375, y = 50, width = 100, height = 25)
            self.posDevel.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Разработчик"))
            self.posDevel.place(x = 475, y = 50, width = 100, height = 25)
            self.posPublisher.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Издатель"))
            self.posPublisher.place(x = 575, y = 50, width = 100, height = 25)
            self.posPrice.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Цена"))
            self.posPrice.place(x = 675, y = 50, width = 50, height = 25)
            self.exit.bind('<ButtonRelease-1>')
            self.exit.place(x = 850, y = 650, width = 75, height = 40)
            self.buttSort()
#Поле = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
        def buttSort(self):
            i = 0
            while ( i < len(self.base)):
                self.pNG[i].delete(0,1999)
                self.pNG[i].insert(0,self.base[i][0])
                self.pNG[i].place(x = 100, y = 50 + ( i + 1 ) * 25, width = 125, height = 25 )
                self.pP[i].delete(0,1999)
                self.pP[i].insert(0,self.base[i][2])
                self.pP[i].place(x = 225, y = 50 + ( i + 1 ) * 25, width = 100, height = 25 )
                self.pG[i].delete(0,1999)
                self.pG[i].insert(0,self.base[i][1])
                self.pG[i].place(x = 325, y = 50 + ( i + 1 ) * 25, width = 50, height = 25 )
                self.pY[i].delete(0,1999)
                self.pY[i].insert(0,self.base[i][3])
                self.pY[i].place(x = 375, y = 50 + ( i + 1 ) * 25, width = 100, height = 25 )
                self.pD[i].delete(0,1999)
                self.pD[i].insert(0,self.base[i][5])
                self.pD[i].place(x = 475, y = 50 + ( i + 1 ) * 25, width = 100, height = 25 )
                self.pPu[i].delete(0,1999)
                self.pPu[i].insert(0,self.base[i][6])
                self.pPu[i].place(x = 575, y = 50 + ( i + 1 ) * 25, width = 100, height = 25 )
                self.pPr[i].delete(0,1999)
                self.pPr[i].insert(0,self.base[i][4])
                self.pPr[i].place(x = 675, y = 50 + ( i + 1 ) * 25, width = 50, height = 25 )
                i = i + 1

        def sortDisp(self, event, newSort):
            if ( self.currSort == newSort ):
                self.flagSort = (self.flagSort + 1) % 2
            else: 
                self.flagSort = 1
            self.base = main.sort(newSort, self.flagSort)
            self.currSort = newSort
            self.buttSort()



    root = tk.Tk()
    root.title("Games Date Base")
    root.geometry('1280x720')

    # second part

    #posNameGame = tk.Button( root, width = 100, height = 100, text = "Название игры", bg = "white", fg="black")
    #posNameGame.bind("<Button-1>", sortDisp(currSort, flagSort))
    window = MainWindow()
#    posNameGame.bind("<Button-1>", flagSort = (flagSort + 1) % 2 if ( currSort == "Название игры" ) else flagSort = 1, main.sort("Название игры", flagSort), currSort = "Название игры")
    #posNameGame.place(x = 50, y = 50, width = 175, height = 25)
    #print(flagSort)
    #posNameGame.pack()
    root.mainloop()
display()
