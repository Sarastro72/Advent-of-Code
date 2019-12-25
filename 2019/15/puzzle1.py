#!/usr/local/bin/python3
import sys
import os
import time
sys.path.append('..')
import intCode

class Position:
    def __init__(self, x, y, distance=0, back=0):
        self.x = x
        self.y = y
        self.distance = distance
        self.back = back

    def __str__(self):
        return(f"({self.x},{self.y})")

    def clone(self):
        return Position(self.x, self.y, self.distance, self.back)

    def move(self, d):
        if (d == 1): # North
            self.y -= 1
            self.back = 2
        elif (d == 2): # South
            self.y += 1
            self.back = 1
        elif (d == 3): # West
            self.x -= 1
            self.back = 4
        elif (d == 4): # East
            self.x += 1
            self.back = 3
        self.distance += 1
        return self

def initMap():
    map = []
    for y in range(SIZE):
        map.append([FOG] * SIZE)
    return map

def printMap():
    os.system("clear")
    for y in range(SIZE):
        line = ""
        for x in range(SIZE):
            if (x == pos.x and y == pos.y):
                line += "[]"
            else:
                line += CHARS[mapAt(x,y)] * 2
        print(line)
    print(f"Bot @ {pos}, path length {len(path)}")

WALL = 0
FREE = 1
O2 = 2
FOG = 3

CHARS = "█ O░"


SIZE=50
fmap = initMap()
fmap[SIZE // 2][SIZE // 2] = FREE
path =[]
distance = 0
pos = Position(SIZE // 2, SIZE // 2)


def mapAt(x, y):
    if (x >= SIZE or x < 0 or y >= SIZE or y < 0):
        return WALL
    else:
        return fmap[y][x]

def look(d):
    p = pos.clone().move(d)
    return mapAt(p.x, p.y)

def draw(e):
    fmap[pos.y][pos.x] = e

def advance(d):
    path.append(pos.clone())
    pos.move(d)

def provideInput():
    global pos
    for d in range(1,5):
        if (look(d) == FOG):
            advance(d)
            print(f"Sending {d}")
            return d
    if (len(path) > 0):
        back = pos.back
        pos = path.pop()
        return back
    else:
        return 5 #Quit

def readOutput(output):
    global pos
    print(f"Read {output}")
    draw(output)
    if(output == WALL):
        pos = path.pop()
    printMap()
    if (output == O2):
        input(f"Found O2 at distance {len(path)}")
    time.sleep(0.01)


with open("input") as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

p = intCode.IntComputer(program, inFunc = provideInput, outFunc=readOutput)
p.run()


