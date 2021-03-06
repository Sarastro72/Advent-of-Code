#!/usr/local/bin/python3
import sys
import os
import time
sys.path.append('..')
from intCode import IntComputer

inbuf = []
def readInput():
    global inbuf
    if (not inbuf):
        cmd = input("Cmd > ")
        inbuf = [ord(c) for c in cmd] + [10]
    return inbuf.pop(0)

outbuf = ""
outlines = []
def writeOutput(c):
    global outbuf, outlines, l
    if (c > 255):
        outbuf += "'"+str(c)+"'"
        c = 10
    if (c == 10):
        outlines.append(outbuf)
        outbuf = ""
    else:
        outbuf += chr(c)

inputs = []
def prog(cmd):
    global inputs
    inputs += [ord(c) for c in cmd] + [10]

def clearProg():
    global inputs, outbuf, outlines
    inputs = []
    outbuf = ""
    outlines = []

CMD = ["AND", "OR", "NOT"]
REG = "ABCDTJ"
WRREG = "TJ"

def instruction(nr):
    if (nr > 11):
        nr += 2
    if (nr > 32):
         nr += 2
    c = nr % 3
    r = (nr // 3) % 6
    w = (nr // 18) 
    return f"{CMD[c]} {REG[r]} {WRREG[w]}"

proc = IntComputer.fromFile("input", inFunc = readInput, outFunc = writeOutput)

# Brute force it baby
for a in range(8,32):       # FF close to first slution 
    for b in range(32):   # after the fact...
        for c in range(32):
            for d  in range(32):
                clearProg()
                prog(instruction(a))
                prog(instruction(b))
                prog(instruction(c))
                prog(instruction(d))
                prog("WALK")
                it = a
                it = it * 32 + b
                it = it * 32 + c
                it = it * 32 + d
                if (it % 100 == 0):
                    print(f" {it * 10000 // 1048576 / 100}%  \r", end = "")
                it += 1
                proc.reset()
                proc.run(inputs = inputs)
                if (len(outlines) < 6):
                    print()
                    print(instruction(a))
                    print(instruction(b))
                    print(instruction(c))
                    print(instruction(d))
                    print(outlines[-1])




