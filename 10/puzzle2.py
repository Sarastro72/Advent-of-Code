#!/usr/local/bin/python
import math

filepath = 'input'
# Best position from puzzle 1
ox = 23
oy = 19

def getAngle(dx, dy):
    a = math.atan2(dx, dy)
    if (a < 0):
        a = a + (2*math.pi)
    return a * 360 / (2 * math.pi)

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rx = x - ox
        self.ry = oy - y
        self.angle = int(getAngle(self.rx, self.ry) * 1000)

    def __str__(self):
        return f"Asteroid @({self.x},{self.y}) {self.sortable()}"

    def sortable(self):
        sdist = math.fabs(self.rx) + math.fabs(self.ry)
        return "%06d:%03d" % (self.angle, sdist)

asteroids = []
with open(filepath) as fp:
    line = fp.readline().strip()
    y = 0
    while line:
        for x in range(len(line)):
            if line[x] == "#":
                a = Asteroid(x, y)
                asteroids.append(a)
        line = fp.readline().strip()
        y += 1

asteroids.sort(key=lambda a: a.sortable())
asteroids.pop(0) # Remove center

lastAngle = -1
i = 0
destroyed = 0
while True:
    target = asteroids[i]
    if (target.angle != lastAngle):
        destroyed += 1
        print(f"#{destroyed} Boom, {target} is destroyed!")
        asteroids.pop(i)
        lastAngle = target.angle
    else:
        i += 1
    if (i >= len(asteroids)):
        print("Full revolution. Starting new lap:")
        i = 0
        lastAngle = -1
    if (destroyed == 200 or len(asteroids) == 0):
        break



