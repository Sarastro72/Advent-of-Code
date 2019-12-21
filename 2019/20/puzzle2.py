#!/usr/local/bin/python3
import sys
import time
import collections

class Map:
    portalByPos = {}
    portalByName = {}
    def __init__(self, file):
        with open(sys.argv[1]) as f:
            self.mmap = [l.rstrip('\n') for l in f]
            self.xs = len(self.mmap[0])
            self.ys = len(self.mmap)
            print(f"Read map of size {self.xs}, {self.ys}")

    def isLetterAt(self, x, y):
        return "A" <= self.at(x,y) <= "Z"

    def radialDistance(self, x, y):
        return max(abs(self.xs // 2 - x), abs(self.ys // 2 - y))

    def findPortals(self):
        for y in range(len(self.mmap)):
                for x in range(len(self.mmap[0])):
                    if (self.isLetterAt(x, y)):
                        self.resolvePortal(x, y)
        for (name, portal) in self.portalByName.items():
            self.mapPortalPaths(portal)
        for n, p in self.portalByName.items():
            print(f"{n} -> {p}")

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
        self.portalByPos[(x, y)] = name
        portal = self.portalByName.get(name)
        if (portal):
            op = portal[0]
            if (self.radialDistance(x, y) > self.radialDistance(op[0], op[1])):
                self.portalByName[name + "0"] = ((x, y), [])
                self.portalByName[name + "1"] = portal
                self.portalByPos[(x, y)] = name + "0"
                self.portalByPos[portal[0]] = name + "1"
            else:
                self.portalByName[name + "1"] = ((x, y), [])
                self.portalByName[name + "0"] = portal
                self.portalByPos[(x, y)] = name + "1"
                self.portalByPos[portal[0]] = name + "0"
            del self.portalByName[name]
        else:
            self.portalByName[name] = ((x, y), [])

    def mapPortalPaths(self, portal):  
        pos = portal[0]
        hasbeen={pos: 1}
        togo = collections.deque([(pos, 0)])
        while togo:
            (x, y), distance = togo.popleft()
            distance += 1
            for np in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if not hasbeen.get(np):
                    hasbeen[np] = 1
                    c = mmap.at(np[0], np[1])
                    if (self.portalByPos.get(np)):
                        destination = self.portalByPos[np]
                        portal[1].append((destination, distance))
                    elif (c == "."):
                        togo.append((np, distance))

    def findPath(self, dep, dest, path = []):
        togo = collections.deque([(dep, -1, [dep])])
        visited = []
        while togo:
            (name, dist, path) = togo.popleft()
            name = self.otherSide(name)
            level = self.levelOf(name)
            dist += 1
            (pos, reachable) = self.portalByName[name[:3]]
            for (nextp, leg) in reachable:
                if (nextp == dest and level == 0):
                    return (dist + leg, path + [nextp])
                if (len(nextp) < 3):
                    continue
                nextp = f"{nextp}{level}"
                if (nextp in visited):
                    continue
                if (level == 0 and self.sideOf(nextp) == 0):
                    continue
                visited.append(nextp)
                oldLen = len(togo)
                for i, (p, d, pt) in enumerate(togo):
                    if (dist + leg < d):
                        togo.insert(i, (nextp, dist + leg, path + [nextp]))
                        break
                if (oldLen == len(togo)):
                    togo.append((nextp, dist + leg, path + [nextp]))

    @staticmethod
    def baseOf(name):
        return name[:2]

    @staticmethod
    def sideOf(name):
        return int(name[2:3])

    @staticmethod
    def levelOf(name):
        return int(name[3:] or 0)

    @staticmethod
    def otherSide(name):
        if (len(name) < 3):
            return name
        base = Map.baseOf(name)
        side = Map.sideOf(name)
        level = Map.levelOf(name)
        if (side == 0):
            side = 1
            level -= 1
        else:
            side = 0
            level += 1
        return f"{base}{side}{level}"

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
