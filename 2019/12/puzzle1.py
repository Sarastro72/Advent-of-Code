#!/usr/local/bin/python3
import re

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
        return f"({self.x}+{self.vx}, {self.y}+{self.vy}, {self.z}+{self.vz} +{self.energy()})"

    def attractedBy(self, moons):
        for moon in moons:
            self.vx += sign(moon.x - self.x)
            self.vy += sign(moon.y - self.y)
            self.vz += sign(moon.z - self.z)

    def tick(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def energy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic =  abs(self.vx) + abs(self.vy) + abs(self.vz)
        return potential * kinetic

    def state(self):
        return [self.x,self.y,self.z,self.vx,self.vy,self.vz]


class PlanetSystem:
    def __init__(self, moons):
        self.moons = moons

    def __str__(self):
        psstr = ""
        energy = 0
        for moon in moons:
            psstr += str(moon) + "\n"
            energy += moon.energy()
        psstr += f"e={energy}\n"
        return psstr

    def tick(self):
        for moon in self.moons:
            moon.attractedBy(self.moons)
        for moon in self.moons:            
            moon.tick()

    def energy(self):
        energy = 0
        for moon in self.moons:
            energy += moon.energy()

    def state(self):
        state = []
        for moon in self.moons:
            state += moon.state()
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

moons = readMoons("input")
ps = PlanetSystem(moons)
print(ps)
for i in range(1000):
    ps.tick()

print(ps)
