# -*- coding: utf-8 -*-
"""
Created on Apr 2018

@author: Труханов А.И.
"""

def base():
    """
    База данных
    Возвращает список списков
    Поля = ["Название игры", "Жанр", "Год выпуска", "Цена",
            "Разработчик", "Издатель"]
    Автор Труханов А.И.
    """
    W1 = ["Warcraft", "Стратегия", 1994, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    W2 = ["Warcraft 2", "Стратегия", 1995, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    W3 = ["Warcraft 3", "Стратегия", 2002, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    WOW = ["World of Warcraft", "ММОРПГ", 2004, 549,
           "Blizzard Entertainment", "Blizzard Entertainment"]
    D1 = ["Diablo", "РПГ", 1996, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    D2 = ["Diablo 2", "РПГ", 2000, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    D3 = ["Diablo 3", "РПГ", 2012, 999,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    SC1 = ["Star Craft", "Стратегия", 1998, 599,
           "Blizzard Entertainment", "Blizzard Entertainment"]
    SC2 = ["Star Craft 2", "Стратегия", 2010, 1699,
           "Blizzard Entertainment", "Blizzard Entertainment"]
    HS = ["Hearthstone", "ККИ", 2014, 0,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    HOTS = ["Heroes of the Storm", "МОБА", 2015, 0,
            "Blizzard Entertainment", "Blizzard Entertainment"]
    OW = ["Overwatch", "Шутер", 2016, 1999,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    return [W1, W2, W3, WOW, D1, D2, D3, SC1, SC2, HS, HOTS, OW]
