#!/usr/local/bin/python

filepath = 'input'
objects = []
orbitMap = {}
orbits = 0

def depth(orbit):
    depth = -1
    while orbit:
        depth += 1
        orbit = orbitMap.get(orbit)
    return depth


with open(filepath) as fp:
    line = fp.readline()
    while line:
        (center, orbit) = line.strip().split(")")
        objects.append(orbit)
        orbitMap[orbit] = center
        line = fp.readline()

for o in objects:
    orbits += depth(o)

print(orbits)