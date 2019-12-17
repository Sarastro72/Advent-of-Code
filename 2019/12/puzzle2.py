#!/usr/local/bin/python3
import re
from math import gcd

def sign(a):
    if (a == 0):
        return 0
    return a // abs(a)

class Moon:
    def __init__(self, x, y, z, vx=0, vy=0,vz=0):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __str__(self):
        return f"({self.x}+{self.vx}, {self.y}+{self.vy}, {self.z}+{self.vz})"

    def attractedBy(self, moons):
        for moon in moons:
            self.vx += sign(moon.x - self.x)
            self.vy += sign(moon.y - self.y)
            self.vz += sign(moon.z - self.z)

    def tick(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def state(self):
        return [self.x,self.y,self.z,self.vx,self.vy,self.vz]


class PlanetSystem:
    def __init__(self, moons):
        self.moons = moons

    def __str__(self):
        psstr = ""
        for moon in moons:
            psstr += str(moon) + "\n"
        return psstr

    def tick(self):
        for moon in self.moons:
            moon.attractedBy(self.moons)
        for moon in self.moons:            
            moon.tick()

    def state(self, pos):
        state = []
        for moon in self.moons:
            state += [moon.state()[pos], moon.state()[pos+3]]
        return state

pattern = re.compile(r'<x=(-?\d+), ?y=(-?\d+), ?z=(-?\d+)>')
def readMoons(filepath):
    moons = []
    with open(filepath) as fp:
        line = fp.readline().strip()
        while line:
            (x,y,z) = pattern.match(line).groups()
            moons.append(Moon(int(x),int(y),int(z)))
            line = fp.readline().strip()
    return moons

def lcm(a, b):
    return a * b // gcd(a, b)

t={"x": 0,"y": 1,"z": 2}
moons = readMoons("input")
ps = PlanetSystem(moons)
print(ps)
initialState={"x": ps.state(0), "y": ps.state(1), "z": ps.state(2)}
solution = {"x": 0,"y": 0,"z": 0}
for i in range(1, 1000000):
    ps.tick()
    done = True
    for axis in ["x", "y", "z"]:
        if (solution[axis] == 0):
            st = ps.state(t[axis])
            if (st == initialState[axis]):
                solution[axis] = i
                print(f"{axis} axis repeats after {i} iterations. {st}")
            else:
                done = False
    if (done):
        break
sx = solution["x"]
sy = solution["y"]
sz = solution["z"]
axisLcm = lcm(lcm(sx, sy), sz)
print(f"Universe repeats after {sx * sy * sz} but also after {axisLcm} iterations")




