#!/usr/local/bin/python3
import collections
import sys

def charRange(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other): 
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def to(self, direction):
        direction = direction % 4
        if (direction == 0):  #north
            return Point(self.x, self.y - 1)
        elif (direction == 1):  #east
            return Point(self.x + 1, self.y)
        elif (direction == 2):  #source
            return Point(self.x, self.y + 1)
        elif (direction == 3):  #west
            return Point(self.x - 1, self.y)


class Map:
    def __init__(self, file):
        with open(sys.argv[1]) as f:
            self.mmap = [l.rstrip('\n') for l in f]

    def findEntrance(self):
        for y in range(len(self.mmap)):
            if ("@" in self.mmap[y]):
                for x in range(len(self.mmap[0])):
                    if (self.mmap[y][x] == "@"):
                        return Point(x,y)

    def at(self, pos):
        return self.mmap[pos.y][pos.x]

    def draw(self):
        for l in self.mmap:
            print(l)


def reachableKeys(mmap, pos, keys):
    reachable = {}
    hasbeen={pos: 1}
    togo = collections.deque([(pos, 0)])
    while togo:
        pt, d = togo.popleft()
        #print(f"Checking {pt} distance {d}")
        for direction in range(4):
            np = pt.to(direction)
            if not hasbeen.get(np):
                hasbeen[np] = 1
                c = mmap.at(np)
                if (c == "#"):
                    continue
                elif ("A" <= c <= "Z" and not c.lower() in keys):
                    continue
                elif ("a" <= c <= "z" and not c in keys):
                    reachable[c] = (np, d + 1)
                else:
                    togo.append((np, d + 1))
    return reachable

visited={}
def traverse(mmap, start, keys=""):
    kfp = "".join(sorted(keys))
    if (start, kfp) in visited:
        return visited[start, kfp]
    if len(visited) % 10 == 0:
        print(keys)
    rk = reachableKeys(mmap, start, keys)
    if len(rk) == 0:
        return 0
    shortest = 999999
    for k, (pos, kd) in rk.items():
        dist = traverse(mmap, pos, keys + k)
        shortest = min(kd + dist, shortest)
    visited[start, kfp] = shortest
    return shortest


mmap = Map(sys.argv[0])
mmap.draw()
start = mmap.findEntrance()
print(f"Start at {start}")
print(traverse(mmap, start, ""))


