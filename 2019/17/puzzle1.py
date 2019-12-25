#!/usr/local/bin/python3
import sys
import os
import time
sys.path.append('..')
import intCode

def readOutput(o):
    global outputStr
    if (o != 10):
        outputStr += chr(o)
    elif (len(outputStr) > 0):
        smap.append(outputStr)
        outputStr = ""

outBuf=[]
def provideInput():
    global smap, outputStr
    drawDisplay()
    global outBuf
    if (len(outBuf) == 0):
        str = input("Input: ")
        outBuf = list(str + "\n")
    smap = []
    str=""
    return ord(outBuf.pop(0))

def pos(x,y):
    return smap[y][x]

def isIntersection(x,y):
    return (pos(x,y) == "#" and
        pos(x+1,y) == "#" and
        pos(x-1,y) == "#" and
        pos(x,y+1) == "#" and
        pos(x,y-1) == "#")

def calibrateMap():
    cal = 0
    for y in range(1, len(smap) - 1):
        for x in range(1, len(smap[0]) - 1):
            if isIntersection(x,y):
                cal += x * y
    return cal

def drawDisplay():
    for s in smap:
        print(f"|{s}|")

with open("input") as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

smap = []
outputStr=""

p = intCode.IntComputer(program, inFunc = provideInput, outFunc=readOutput)
p.run()

drawDisplay()
print(f"Calibration value: {calibrateMap()}")
