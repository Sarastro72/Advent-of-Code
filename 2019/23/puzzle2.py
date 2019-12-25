#!/usr/local/bin/python3
import sys
import os
import time
import concurrent.futures
sys.path.append('..')
from intCode import IntComputer

VIEW = [50, 255]
DEBUG = False

inputs = []
bufs = []
inactiveCount = 0
for i in range(51):
    inputs.append([])
    bufs.append([])

def readOutput(channel, value):
    global inactiveCount
    if (channel in VIEW):
        print(f"[{channel}] produces data")
    inactiveCount = 0
    buf = bufs[channel]
    buf.append(value)
    if (len(buf) == 3):
        out_chan = buf.pop(0)
        x = buf.pop(0)
        y = buf.pop(0)
        if (out_chan > 49):
            #print(f" Got value {x} {y} for channel {out_chan}")
            inputs[50] = [x, y]
        else:
            inputs[out_chan] += [x, y]
            if (out_chan in VIEW): 
                print(f"[{channel}] produced {x}, {y} for [{out_chan}]")

def provideInput(channel):
    global inactiveCount
    #if (channel in VIEW):
        #print(f"[{channel}] polls for data")
    cinput = inputs[channel]
    if (cinput):
        v = cinput.pop(0)
        if (channel in VIEW):
            print(f"[{channel}] consumed value {v}")
        inactiveCount = 0
        return v
    else:
        #print(f"[{channel}] no data, got -1")
        return -1

def getOutputfunc(channel):
    return lambda value : readOutput(channel, value)

def getInputfunc(channel):
    return lambda : provideInput(channel)

computers = []
for i in range(50):
    computer = IntComputer.fromFile("input", inFunc = getInputfunc(i), outFunc = getOutputfunc(i))
    computer.run([i], suspendOnIO = True, debug = DEBUG)
    computers.append(computer)

lasty = -1
while True:
    #print("    New round")
    inactiveCount += 1
    for i in range(50):
        #print(f"   computer {i} runs")
        computers[i].run(suspendOnIO = True, debug = DEBUG)
        #time.sleep(0.1)

    if (inactiveCount > 3):
        if (len(inputs[50]) >= 2):
            x = inputs[50].pop(0)
            y = inputs[50].pop(0)
            if (lasty == y):
                print(f"Double y detected: {y}")
                exit()                
            #print(f"Sending {x} {y} to [0] {lasty}")
            inputs[0].append(x)
            inputs[0].append(y)
            lasty = y
            #time.sleep(.5)
        else:
            print("Nothing more to do!")
            exit()

print("Exit")
for i, data in enumerate(inputs):
    print(f"{i}  {data}")





