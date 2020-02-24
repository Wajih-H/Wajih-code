import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.colors import ListedColormap
import unittest
import random


def moveWest(tile):
    def pushWest(y):
        for x in range(1,len(tile[y])):
            if tile[y][x] != 0:
                if tile[y][x-1] == 0:
                    tile[y][x-1] = tile[y][x]
                    tile[y][x] = 0
    def combineWest(y):
        global score
        for x in range(1,len(tile[y])):
            if tile[y][x] != 0:
                if tile[y][x-1] == tile [y][x]:
                    tile[y][x-1] += tile[y][x]
                    score += tile[y][x-1]
                    tile[y][x] = 0
    for y in range(len(tile)):
        for i in range(len(tile[y])-1):
            pushWest(y)
        combineWest(y)
        for i in range(len(tile[y])-1):
            pushWest(y)

def moveEast(tile):
    def pushEast(y):
        for n in range(2,len(tile[y])+1):
            x = -n
            if tile[y][x] != 0:
                if tile[y][x+1] == 0:
                    tile[y][x+1] = tile[y][x]
                    tile[y][x] = 0
    def combineEast(y):
        global score
        for n in range(2,len(tile[y])+1):
            x = -n
            if tile[y][x] != 0:
                if tile[y][x+1] == tile [y][x]:
                    tile[y][x+1] += tile[y][x]
                    score += tile[y][x+1]
                    tile[y][x] = 0
    for y in range(len(tile)):
        for i in range(len(tile[y])-1):
            pushEast(y)
        combineEast(y)
        for i in range(len(tile[y])-1):
            pushEast(y)

def moveNorth(tile):
    def pushNorth():
        for y in range(1,len(tile)):
            if tile[y][x] != 0:
                if tile[y-1][x] == 0:
                    tile[y-1][x] = tile[y][x]
                    tile[y][x] = 0
    def combineNorth():
        global score
        for y in range(1,len(tile)):
            if tile[y][x] != 0:
                if tile[y-1][x] == tile[y][x]:
                    tile[y-1][x] += tile[y][x]
                    score += tile[y-1][x]
                    tile[y][x] = 0
    for x in range(len(tile[0])):
        for i in range(len(tile)-1):
            pushNorth()
        combineNorth()
        for i in range(len(tile)-1):
            pushNorth()

def moveSouth(tile):
    def pushSouth():
        for n in range(2,len(tile)+1):
            y = -n
            if tile[y][x] != 0:
                if tile[y+1][x] == 0:
                    tile[y+1][x] = tile[y][x]
                    tile[y][x] = 0
    def combineSouth():
        global score
        for n in range(2,len(tile)+1):
            y = -n
            if tile[y][x] != 0:
                if tile[y+1][x] == tile[y][x]:
                    tile[y+1][x] += tile[y][x]
                    score += tile[y+1][x]
                    tile[y][x] = 0
    for x in range(len(tile[0])):
        for i in range(len(tile)-1):
            pushSouth()
            combineSouth()
        for i in range(len(tile)-1):
            pushSouth()


class RandomTest(unittest.TestCase):


    def test_choice(self):
        #Test of the function select color
        list_colors = ['red', 'blue', 'orange', 'yellow', 'gray', 'cyan', 'black']
        selected_colors = random.choices(list_colors, k=m)
        self.assertIn(selected_colors , list_colors)
        
if __name__ == "__main__":
    # create the board
    n = int(input("give the size of the board:"))
    print(n)
    m = int(input("give the number of colors:"))
    print(m)
    board = np.random.rand(n, n)
    print(board)
    # color of tiles
    list_colors=['red', 'blue','orange', 'yellow', 'gray', 'cyan', 'black']
    selected_colors= random.choices(list_colors, k=m)
    print("The selected colors:", selected_colors)
    cmap = colors.ListedColormap(selected_colors)
    plt.figure(figsize=(n,n))
    plt.pcolor(board[::-1],cmap=cmap,edgecolors='k', linewidths=3)
    plt.show()
    
    # call of functions
    moveNorth(board)
    moveSouth(board)
    moveEast(board)
    moveWest(board)