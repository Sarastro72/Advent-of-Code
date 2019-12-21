#!/usr/local/bin/python3
import sys
import collections

class Map:
    portalsByPos = {}
    portalsByName = {}
    def __init__(self, file):
        with open(sys.argv[1]) as f:
            self.mmap = [l.rstrip('\n') for l in f]
            self.xs = len(self.mmap[0])
            self.ys = len(self.mmap)

    def isLetterAt(self, x, y):
        return "A" <= self.at(x,y) <= "Z"

    def findPortals(self):
        for y in range(len(self.mmap)):
                for x in range(len(self.mmap[0])):
                    if (self.isLetterAt(x, y)):
                        self.resolvePortal(x, y)
        for (pos, name) in self.portalsByPos.items():
            portal = self.portalsByName.get(name)
            self.mapPortalPaths(self.portalsByName[name])
        print(f"ByName: {self.portalsByName}")

    def resolvePortal(self, x, y):
        name = self.at(x,y)
        if (self.isLetterAt(x + 1, y)):
            name += self.at(x + 1, y)
            if (self.at(x + 2, y) == "."):
                self.addPortal(name, x + 2, y)
            elif (self.at(x - 1, y) == "."):
                self.addPortal(name, x - 1, y)
        elif (self.isLetterAt(x, y + 1)):
            name += self.at(x, y +1)
            if (self.at(x, y + 2) == "."):
                self.addPortal(name, x, y + 2)
            elif (self.at(x, y - 1) == "."):
                self.addPortal(name, x, y - 1)

    def addPortal(self, name, x, y):
        self.portalsByPos[(x, y)] = name
        p = self.portalsByName.get(name)
        if (p):
            p[0].append((x, y))
        else:
            self.portalsByName[name] = ([(x, y)], [])

    def mapPortalPaths(self, portal):  
        for pos in portal[0]:
            hasbeen={pos: 1}
            togo = collections.deque([(pos, 0)])
            while togo:
                (x, y), distance = togo.popleft()
                distance += 1
                for np in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if not hasbeen.get(np):
                        hasbeen[np] = 1
                        c = mmap.at(np[0], np[1])
                        if (self.portalsByPos.get(np)):
                            destination = self.portalsByPos[np]
                            portal[1].append((destination, distance))
                        elif (c == "."):
                            togo.append((np, distance))

    cache = {}
    def findPath(self, dep, dest, path = []):
        if (dep == dest):
            print("Heureka")
            return (-1, path + [dest])
        cachehit = self.cache.get((dep, dest))
        if (cachehit):
            return cachehit
        npath = path.copy()
        npath.append(dep)
        portal = self.portalsByName[dep]
        shortest = 999999
        best = []
        for (name, leg) in portal[1]:
            if (name in npath):
                continue
            (sublength, subpath) = self.findPath(name, dest, npath)
            length = sublength + leg + 1
            if (length < shortest):
                shortest = length
                best = subpath
        self.cache[(dep, dest)] = (shortest, best)
        return (shortest, best); 


    def at(self, x, y):
        if (0 <= x < self.xs and 0 <= y < self.ys):
            return self.mmap[y][x]
        else:
            return " "

    def draw(self):
        for l in self.mmap:
            print(l)


mmap = Map(sys.argv[1])
mmap.findPortals()
print(mmap.findPath("AA", "ZZ"))
