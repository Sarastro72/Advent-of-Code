#!/usr/local/bin/python3
import sys
import os
import time
sys.path.append('..')
import intCode

def readOutput(o):
    global outputStr
    if (o > 255):
        print(f"Dust: {o}")
    if (o != 10):
        outputStr += chr(o)
    elif (len(outputStr) > 0):
        if (not mapDone):
            smap.append(outputStr)
        else:
            print(outputStr)
        outputStr = ""

inputBuf=[]
def provideInput():
    global inputBuf, mapDone
    if (not mapDone):
        mapDone = True
        smap.pop() # Remove input header
        printMap()
        p = findBot()
        print(f"Bot found at {p}")
        path = findpath(p["x"], p["y"], 0)
        print("Path: " + " ".join(path))
        print("Solution:")
        solution = segment([path], 3)
        inputBuf += formatMain(solution["main"])
        inputBuf += formatSegment(solution["segments"][0])
        inputBuf += formatSegment(solution["segments"][1])
        inputBuf += formatSegment(solution["segments"][2])
        inputBuf += list("n\n")
    if (len(inputBuf) == 0):
        str = input("> ")
        inputBuf = list(str + "\n")
    #print(f"Sending {ord(inputBuf[0])}")
    return ord(inputBuf.pop(0))

def formatMain(main):
    trans = []
    for s in main:
        trans.append(chr(65 + s))
        trans.append(",")
    print("".join(trans[:-1]))
    trans[-1] = "\n"
    return trans

def formatSegment(seg):
    trans = []
    for i in range(0, len(seg), 2):
        trans.append(seg[i])
        trans.append(",")
        for c in seg[i + 1]:
            trans.append(c)
        if (i < len(seg) - 2):
            trans.append(",")
    print("".join(trans))
    trans.append("\n")
    return trans

def pos(x,y):
    if (y < 0 or y >= len(smap) or x < 0 or x >= len(smap[0])):
        return "."
    return smap[y][x]

def posd(x,y,direction):
    p = move(x,y,direction)
    return pos(p["x"], p["y"])

def move(x,y,direction):
    direction = direction % 4
    if (direction == 0):
        y -= 1
    elif (direction == 1):
        x += 1
    elif (direction == 2):
        y += 1
    elif (direction == 3):
        x -= 1
    return {"x": x, "y": y}

def isScaffold(x,y,direction):
    return posd(x,y,direction) == "#"

def isIntersection(x,y):
    return (pos(x,y) == "#" and
        pos(x+1,y) == "#" and
        pos(x-1,y) == "#" and
        pos(x,y+1) == "#" and
        pos(x,y-1) == "#")

def findBot():
    for y in range(len(smap)):
        for x in range(len(smap[0])):
            if (pos(x,y) == "^"):
                return {"x": x, "y": y}


def findpath(x, y, direction):
    path = []
    while True:
        if isScaffold(x, y, direction + 1):
            direction += 1
            path.append("R")
        elif isScaffold(x, y, direction - 1):
            direction -= 1
            path.append("L")
        else: 
            return path
        steps = 0
        while (isScaffold(x,y,direction)):
            p = move(x,y,direction)
            x = p["x"]
            y = p["y"]
            steps += 1
        path.append(str(steps))

def segment(lists, nsegments, segments=[]):
    if (nsegments == len(segments)):
        #print(lists)
        for l in lists:
            if (type(l) is list):
                return [] # No solution    
        return {"main": lists, "segments": segments} # Solution
    for segLength in range(2, 11, 2):
        for l in lists:
            if (type(l) is list):
                if (segLength <= len(l)):
                    sub = l[:segLength]
                    #print(f"sub {sub}")
                    oLists = splitAll(lists, sub, len(segments))
                    #print(oLists)
                    oSegments = segments.copy()
                    oSegments.append(sub)
                    #print(oSegments)
                    solution = segment(oLists, nsegments, oSegments)
                    if (solution):
                        return solution


def splitAll(lists, subList, index):
    output = []
    for l in lists:
        if (type(l) is list):
            output += split(l, subList, index)
        else:
            output.append(l)
    return output

def split(oList, subList, index):
    i = 0
    sLen = len(subList)
    skip = []
    splitted = []
    while (i < len(oList)):
        if (oList[i:i+sLen] == subList):
            if(skip):
                splitted.append(skip)
                skip = []
            splitted.append(index)
            i += sLen
        else:
            skip += oList[i:i+2]
            i += 2
    if (skip):
        splitted.append(skip)
    #print(f"oList: {oList}")
    #print(f"Splitted: {subList} – {splitted}")
    return splitted

def printMap():
    for s in smap:
        print(f"|{s}|")

with open("input") as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

smap = []
mapDone = False
outputStr=""
direction = 0

program[0] = 2

def qInput():
    global inputBuf
    if (len(inputBuf) == 0):
        str = input("> ")
        inputBuf = list(str + "\n")
    print(f"Sending {ord(inputBuf[0])}")
    return ord(inputBuf.pop(0))

def qOutput(o):
    global outputStr
    if (o > 255):
        print(f"Dust: {o}")
    if (o != 10):
        outputStr += chr(o)
    elif (len(outputStr) > 0):
        print(f"| {outputStr} |")
        outputStr = ""

p = intCode.Process(program, inFunc = provideInput, outFunc=readOutput)
p.run()


