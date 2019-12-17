#!/usr/local/bin/python

import os

RES=100

def initMap(res = RES):
    line = [0] * RES
    map = []
    for i in range(RES):
        map.append(line.copy())
    return map

def drawMap(map):
    for y in range(0, RES, 2):
        line=""
        for x in range(RES):
            pp=map[y][x] * 10 + map[y+1][x]
            if (pp == 11):
                line += "█"
            elif (pp == 10):
                line += "▀"
            elif (pp == 1):
                line += "▄"
            else:
                line += " "
        print(line)

class Point:
    def __init__(self, x, y ,vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def tick(self):
        self.x += self.vx
        self.y += self.vy

filepath = 'input'
points = []
with open(filepath) as fp:
   line = fp.readline().strip()
   while(line):
       x = int(line[10:16])
       y = int(line[18:24])
       vx = int(line[36:38])
       vy = int(line[40:42])
       points.append(Point(x, y, vx, vy))
       line = fp.readline().strip()

skip=1
step=0
scale=0
while True:
    if (skip > 0):
        for i in range(skip):
            step += 1
            minx = maxx = points[0].x
            miny = maxy = points[0].y
            for p in points:
                p.tick();
                minx = min(minx, p.x)
                maxx = max(maxx, p.x)
                miny = min(miny, p.y)
                maxy = max(maxy, p.y)

    dx = maxx - minx
    dy = maxy - miny
    sdx = dx / (1.2 ** scale)
    sdy = dy / (1.2 ** scale)
    sxoff = (dx - sdx) / 2
    syoff = (dy - sdy) / 2
    scx = sdx / (RES - 1)
    scy = sdy / (RES - 1)
    scf = max(scx, scy, 1)

    map = initMap()
    for p in points:
        x = int((p.x - minx - sxoff) / scf)
        y = int((p.y - miny - syoff) / scf)
        #print(f"{x},{y}")
        if (x >= 0 and x < RES and y >= 0 and y < RES):
            map[y][x] = 1

    os.system("clear")
    drawMap(map)

    print(f"{scale} {dx} {sdx} {0-minx-sxoff}")
    inp = input(f"{step}: {minx}–{maxx} {scx} {miny}–{maxy} {scy}: ")
    if inp:
        if (inp == "+"):
            scale += 1
            skip = 0
        elif (inp == "-"):
            scale -= 1
            skip = 0
        elif (inp == "."):
            scale = 0
            skip = 0
        elif (inp == "p"):
            for p in points:
                print(f"{p.x},{p.y}")
            skip = 0
            input("Press enter")
        elif (inp == "q"):
            break
        else:
            skip = int(inp)




