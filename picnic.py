#!/usr/bin/python

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'apples': 4, 'celery': 3, 'beers': 2}
printPicnic(picnicItems, 12, 5)