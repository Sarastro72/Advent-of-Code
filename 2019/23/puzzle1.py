#!/usr/local/bin/python3
import sys
import os
import time
import concurrent.futures
sys.path.append('..')
from intCode import IntComputer

VIEW = range(50)
DEBUG = False

inputs = []
bufs = []
for i in range(51):
    inputs.append([])
    bufs.append([])

def readOutput(channel, value):
    if (channel in VIEW):
        print(f"[{channel}] produces data")
    buf = bufs[channel]
    buf.append(value)
    if (len(buf) == 3):
        out_chan = buf.pop(0)
        x = buf.pop(0)
        y = buf.pop(0)
        if (out_chan > 49):
            print(f" Got value {value} for channel {out_chan}")
            inputs[50].append(value)
            exit()
        else:
            inputs[out_chan].append([x, y])
            if (out_chan in VIEW): 
                print(f"[{channel}] produced {x}, {y} for [{out_chan}]")

def provideInput(channel):
    #if (channel in VIEW):
        #print(f"[{channel}] polls for data")
    buf = inputs[channel]
    if (buf):
        v = buf[0].pop(0)
        if (channel in VIEW):
            print(f"[{channel}] consumed value {v}")
        if (len(buf[0]) == 0):
            buf.pop(0)
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

while not inputs[50]:
    print("    New round")

    for i in range(50):
        #print(f"   computer {i} runs")
        computers[i].run(suspendOnIO = True, debug = DEBUG)
        #time.sleep(0.1)

print("Exit")
for i, data in enumerate(inputs):
    print(f"{i}  {data}")





