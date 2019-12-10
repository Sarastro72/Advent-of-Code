#!/usr/local/bin/python
import math

filepath = 'input'

def readPos(x, y):
    return map[y][x]

def isAsteroid(x, y):
    return readPos(x,y) >= 0

def canSee(px, py, tx, ty, map):
    dx = tx - px
    dy = ty - py
    if (dx == 0 and dy == 0):
        return False # Same asteroid
    gcd = math.gcd(dx, dy)
    sx = dx // gcd
    sy = dy // gcd
    for s in range(gcd - 1):
        px += sx
        py += sy
        if isAsteroid(px, py):
            return False # Asteroid in the way
    return True # Nothing in the way

def countVisible(px, py, map):
    visible = 0
    for y in range(maxy):
        for x in range(maxx):
            if (isAsteroid(x, y)):
                if canSee(px, py, x, y, map):
                    visible += 1
    return visible

def printMap():
    print("    ", end = "")
    for x in range(maxx):
        print("%03d " % x, end = "")
    print()
    for y in range(maxy):
        print("%03d " % y, end = "")
        for x in range(maxx):
            if (readPos(x,y) >= 0):
                print("%03d " % readPos(x,y), end = "")
            else:
                print(" .  ", end = "")
        print()

map = []
with open(filepath) as fp:
    line = fp.readline().strip()
    while line:
        row = []
        for c in line:
            if c == "#":
                row.append(0)
            else:
                row.append(-1)
        map.append(row)
        line = fp.readline().strip()

maxy = len(map)
maxx = len(map[0])

for y in range(maxy):
    for x in range(maxx):
        if isAsteroid(x, y):
            map[y][x] = countVisible(x, y, map)

printMap()
print()

best = 0
bx = by = 0
for y in range(maxy):
    for x in range(maxx):
        v = readPos(x, y)
        if(v > best):
            best = v
            bx = x
            by = y

print(f" Best location found at {bx},{by} with {best} visible astroids.")


