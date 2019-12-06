#!/usr/local/bin/python

filepath = 'input'
objects = []
orbitMap = {}
orbits = 0

def extract(object):
    path = []
    item = orbitMap[object]
    while item:
        path.insert(0, item)
        item = orbitMap.get(item)
    return path
    

with open(filepath) as fp:
    line = fp.readline()
    while line:
        (center, orbit) = line.strip().split(")")
        objects.append(orbit)
        orbitMap[orbit] = center
        line = fp.readline()

youPath = extract("YOU")
sanPath = extract("SAN")

while (youPath[0] == sanPath[0]):
    print(youPath[0])
    youPath.pop(0)
    sanPath.pop(0)

print(len(youPath) + len(sanPath))
