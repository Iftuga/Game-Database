# -*- coding: utf-8 -*-
"""
Created on Apr 2018

@author: Труханов А.И.
"""


def base():
    """
    База данных
    Возвращает список списков
    Поля = ["Название игры", "Жанр", "Платформа", "Год выпуска", "Цена",
            "Разработчик", "Издатель"]
    Автор Труханов А.И.
    """
    W1 = ["Warcraft", "Стратегия", "ПК", "1994", "499",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    W2 = ["Warcraft 2", "Стратегия", "ПК", "1995", "499",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    W3 = ["Warcraft 3", "Стратегия", "ПК", "2002", "499",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    WOW = ["World of Warcraft", "ММОРПГ", "ПК", "2004", "549",
           "Blizzard Entertainment", "Blizzard Entertainment"]
    D1 = ["Diablo", "РПГ", "ПК", "1996", "499",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    D2 = ["Diablo 2", "РПГ", "ПК", "2000", "499",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    D3 = ["Diablo 3", "РПГ", "ПК", "2012", "999",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    SC1 = ["Star Craft", "Стратегия", "ПК", "1998", "599",
           "Blizzard Entertainment", "Blizzard Entertainment"]
    SC2 = ["Star Craft 2", "Стратегия", "ПК", "2010", "1699",
           "Blizzard Entertainment", "Blizzard Entertainment"]
    HS = ["Hearthstone", "ККИ", "ПК", "2014", "0",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    HOTS = ["Heroes of the Storm", "МОБА", "ПК", "2015", "0",
            "Blizzard Entertainment", "Blizzard Entertainment"]
    OW = ["Overwatch", "Шутер", "ПК", "2016", "1999",
          "Blizzard Entertainment", "Blizzard Entertainment"]
    HAL1 = ["Halo", "Шутер", "Консоль", "2001", "499",
          "Bungie", "Microsoft"]
    HAL2 = ["Halo 2", "Шутер", "Консоль", "2004", "499",
          "Bungie", "Microsoft"]
    HAL3 = ["Halo 3", "Шутер", "Консоль", "2007", "499",
          "Bungie", "Microsoft"]
    DST1 = ["Destiny", "Шутер", "Консоль", "2014", "1999",
          "Bungie", "Activision"]
    DST2 = ["Destiny 2", "Шутер", "Консоль", "2017", "1999",
          "Bungie", "Activision"]
    EU1 = ["Europa Universalis", "Стратегия", "ПК", "2000", "199",
          "Paradox Interactive", "Paradox Interactive"]
    EU2 = ["Europa Universalis 2", "Стратегия", "ПК", "2001", "199",
          "Paradox Interactive", "Paradox Interactive"]
    EU3 = ["Europa Universalis 3", "Стратегия", "ПК", "2007", "299",
          "Paradox Interactive", "Paradox Interactive"]
    EU4 = ["Europa Universalis 4", "Стратегия", "ПК", "2013", "699",
          "Paradox Interactive", "Paradox Interactive"]
    HOI1 = ["Hearts of Iron", "Стратегия", "ПК", "2002", "199",
          "Paradox Interactive", "Paradox Interactive"]
    HOI2 = ["Hearts of Iron 2", "Стратегия", "ПК", "2005", "199",
          "Paradox Interactive", "Paradox Interactive"]
    HOI3 = ["Hearts of Iron 3", "Стратегия", "ПК", "2009", "299",
          "Paradox Interactive", "Paradox Interactive"]
    HOI4 = ["Hearts of Iron 4", "Стратегия", "ПК", "2016", "699",
          "Paradox Interactive", "Paradox Interactive"]
    MG1 = ["Magicka", "Приключение", "ПК", "2011", "199",
          "Pieces Interactive", "Paradox Interactive"]
    MG2 = ["Magicka 2", "Приключение", "ПК", "2015", "349",
          "Pieces Interactive", "Paradox Interactive"]
    HD = ["Hay Day", "Стратегия", "Ios&Android", "2012", "0",
          "Supercell", "Supercell"]
    COC = ["Clash of Clans", "Стратегия", "Ios&Android", "2012", "0",
          "Supercell", "Supercell"]
    CR = ["Clash Royale", "ККИ", "Ios&Android", "2016", "0",
          "Supercell", "Supercell"]
    return [W1, W2, W3, WOW, D1, D2, D3, SC1, SC2, HS, HOTS, OW,
            HAL1, HAL2, HAL3, DST1, DST2,
            EU1, EU2, EU3, EU4, HOI1, HOI2, HOI3, HOI4, MG1, MG2,
            HD, COC, CR]
