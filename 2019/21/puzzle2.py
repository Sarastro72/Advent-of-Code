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

proc = IntComputer.fromFile("input", inFunc = readInput, outFunc = writeOutput)

#    @   v   v   v   v    
#    #####.#.#.##..###
#     123456789
#     ABCDEFGHI

#  (!A or !B or !C) and D and (E or H))

prog("NOT A J")
prog("NOT B T")
prog("OR T J")
prog("NOT C T")
prog("OR T J")
prog("AND D J")
prog("NOT E T")
prog("NOT T T")
prog("OR H T")
prog("AND T J")
prog("RUN")

proc.run(inputs = inputs)

for line in outlines:
    print(line)



