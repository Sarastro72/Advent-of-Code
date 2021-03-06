#!/usr/local/bin/python3
import re

lineMap={}
closestCollision=1000000
px=0
py=0

def pos():
    return f"{px},{py}"

def movePos(direction):
    global px,py
    if (direction == "R"):
        px+=1
    elif (direction == "L"):
        px-=1
    elif (direction == "U"):
        py+=1
    elif (direction == "D"):
        py-=1
    else:
        print (f"Unknown direction {direction}!!!")


cMatch= re.compile(r'(\w)(\d+)')
def drawLine(command, label):
    global closestCollision
    (direction, dist) = cMatch.match(command).groups()
    #print(f"{direction} {dist}")
    for n in range(int(dist)):
        movePos(direction)
        #print(pos())
        if (pos() in lineMap and lineMap[pos()] != label):
            manhattan = abs(px) + abs(py)
            print(f"collision at {pos()}, distance {manhattan}!")
            if (manhattan < closestCollision):
                closestCollision = manhattan
        lineMap[pos()] = label

def drawPath(line, label):
    global px, py
    px=0
    py=0
    for c in line:
        drawLine(c, label)


filepath = 'input'
with open(filepath) as fp:
   line1 = fp.readline().strip().split(",")
   line2 = fp.readline().strip().split(",")

drawPath(line1, "1")
drawPath(line2, "2")
print(f"Closest intersection is at {closestCollision}")
