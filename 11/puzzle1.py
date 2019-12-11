#!/usr/local/bin/python3

filepath = 'input'

size = 100
dir = 0
pos = [size//2, size//2] # x,y
buf = []

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

def turn(tdir):
    global dir
    if (tdir == 0):
        dir = dir - 1
    else:
        dir = dir + 1
    dir = dir % 4

def move(steps):
    if (dir == 0): # north
        pos[1] -= steps
    elif (dir == 1): # east
        pos[0] += steps
    elif (dir == 2): # south
        pos[1] += steps
    else:  # west
        pos[0] -= steps

def validPos():
    return (pos[0] >= 0 and pos[0] < size and pos[1] >= 0 and pos[1] < size)

def paint(color):
    if (validPos()):
        if(color == 0):
            canvas[pos[1]][pos[0]] = "¨"
        else:
            canvas[pos[1]][pos[0]] = "█"

def getInput():
    color = canvas[pos[1]][pos[0]]
    if (color == "█"):
        return 1
    else:
        return 0

def writeOutput(output):
    buf.insert(0, output)
    if (len(buf) == 2):
        paint(buf.pop())
        turn(buf.pop())
        move(1)

def initMap(size):
    array = []
    for y in range(size):
        array.append([" "] * size)
    return array

def drawCanvas():
    count = 0
    for line in canvas:
        print("".join(line))
        for c in line:
            if (c != " "):
                count += 1
    return count


canvas = initMap(100)

# Uncomment this for question 2
#paint(1)

with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))


process = Process(program, inFunc = getInput, outFunc = writeOutput)
process.run()

count = drawCanvas()


print(f"{count} squares have been painted in")



