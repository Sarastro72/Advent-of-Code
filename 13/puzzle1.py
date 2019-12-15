#!/usr/local/bin/python3
import os
from time import sleep

filepath = 'input'
SIZE = 50

class Process:
    def __init__(self, mem, ptr=0, inFunc = None, outFunc = None):
        self.mem = [0] * 8096 # 8k shold be enough for everyone
        self.ptr = ptr
        self.running = True
        self.realtiveBase = 0
        self.outFunc = outFunc or (lambda v : print(v))
        self.infunc = inFunc or (lambda : input("Input: "))
        for i in range(len(mem)):
            self.mem[i] = mem[i]
    
    def getParam(self, pos, mode):
        adr = self.ptr + pos
        mode = mode // (10 ** (pos - 1))
        mode = mode % 10
        if (mode == 0):
            return self.mem[self.mem[adr]]
        elif (mode == 1):
            return self.mem[adr]
        elif (mode == 2):
            return self.mem[self.realtiveBase+self.mem[adr]]
        else:
            print("ERROR: Unknown read mode {mode}!")
            return self.mem[self.mem[adr]]

    def setMem(self, pos, mode, value):
        adr = self.ptr + pos
        mode = mode // (10 ** (pos - 1))
        mode = mode % 10
        if (mode == 0):
            self.mem[self.mem[adr]] = value
        elif (mode == 2):
            self.mem[self.realtiveBase+self.mem[adr]] = value
        else:
            print("ERROR: Unknown write mode {mode}!")

    def run(self, inputs = []):
        outputs = []
        while True:
            #print(self.mem)
            cmd = self.mem[self.ptr] % 100
            mode = self.mem[self.ptr] // 100
            if (cmd == 1): # Add
                p1 = self.getParam(1, mode)
                p2 = self.getParam(2, mode)
                #print(f"add {p1}  {p2}")
                self.setMem(3, mode, p1 + p2)
                self.ptr += 4
            elif (cmd == 2): # Multiply
                p1 = self.getParam(1, mode)
                p2 = self.getParam(2, mode)
                #print(f"mul {p1}  {p2}")
                self.setMem(3, mode, p1 * p2)
                self.ptr += 4
            elif (cmd == 3): # Input
                if (len(inputs) < 1):
                    inp = self.infunc()
                else:
                    inp = inputs.pop(0)
                #print(f"input {inp}")
                self.setMem(1, mode, int(inp))
                self.ptr += 2
            elif (cmd == 4): # Output
                p1 = self.getParam(1, mode)
                self.outFunc(p1)
                #print(f"output {p1}")
                self.ptr += 2
            elif (cmd == 5): # Jump if true
                p1 = self.getParam(1, mode)
                p2 = self.getParam(2, mode)
                #print(f"jtrue {p1} {p2}")
                if (p1 != 0):
                    self.ptr = p2
                else:
                    self.ptr += 3
            elif (cmd == 6): # Jump if false
                p1 = self.getParam(1, mode)
                p2 = self.getParam(2, mode)
                #print(f"jfalse {p1} {p2}")
                if (p1 == 0):
                    self.ptr = p2
                else:
                    self.ptr += 3
            elif (cmd == 7): # Less than
                p1 = self.getParam(1, mode)
                p2 = self.getParam(2, mode)
                #print(f"less {p1} {p2}")
                if (p1 < p2):
                    self.setMem(3, mode, 1)
                else:
                    self.setMem(3, mode, 0)
                self.ptr += 4
            elif (cmd == 8): # Equals
                p1 = self.getParam(1, mode)
                p2 = self.getParam(2, mode)
                #print(f"eq {p1} {p2}")
                if (p1 == p2):
                    self.setMem(3, mode, 1)
                else:
                    self.setMem(3, mode, 0)
                self.ptr += 4
            elif (cmd == 9): # Set relative base
                p1 = self.getParam(1, mode)
                #print(f"addrb {p1}")
                self.realtiveBase += p1
                self.ptr += 2
            elif (cmd == 99): # End
                self.running = False
                #print(f"end")
                #print(f"Program terminated with {outputs}")
                break
            else:
                self.running = False
                print("ERROR: Unknown command at position {}".format(self.ptr))
                break

buf = []
bx = 0
by = 0
px = 0
score = 0
i = 0

def getInput():
    global i
    i += 1
    if (i % 5 == 0):
        drawCanvas()
        print(f"i={i}, by={by}, bx={bx}, px={px}")   
    #sleep(0.05) 
    if (bx < px):
        return -1
    elif (bx > px):
        return 1
    else:
        return 0

def writeOutput(output):
    global bx, bdir, px, by, score
    buf.insert(0, output)
    if (len(buf) == 3):
        x = buf.pop()
        y = buf.pop()
        v = buf.pop()
        if (x == -1 and y == 0):
            score = v
        else:
            place(x,y,v)
            if (v == 3):
                px = x
            elif (v == 4):
                bx = x
                by = y

def place(x, y, v):
    if (x >= 0 and x < SIZE and y >= 0 and y < SIZE):
        canvas[y][x] = v
    else:
        print(f"Canvas overflow for ({x},{y}) = {v}")


def initMap(size):
    array = []
    for y in range(size // 2):
        array.append([0] * size)
    return array

def drawCanvas():
    os.system("clear")
    count = 0
    print(f" Score: {score}")
    for line in canvas:
        str = ""
        for c in line:
            if (c == 0):
                str += " "
            elif (c == 1):
                str += "█"
            elif (c == 2):
                str += "░"
            elif (c == 3):
                str += "–"
            elif (c == 4):
                str += "o"
            if (c == 2):
                count += 1
        print(str)
    return count


canvas = initMap(SIZE)

with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

# Uncomment for question 2
program[0] = 2

process = Process(program, outFunc = writeOutput, inFunc = getInput)
process.run()

count = drawCanvas()
print(f"{count} squares are filled after {i} iterations")
