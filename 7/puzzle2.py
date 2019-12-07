#!/usr/local/bin/python

def getParam(adr, mode, data):
    if ((mode & 1) == 0):
        return data[data[adr]]
    else:
        return data[adr]

class Program:
    def __init__(self, mem, ptr=0):
        self.mem = mem.copy()
        self.ptr = ptr
        self.running = True
    
    def run_prog(self, inputs):
        outputs = []
        while True:
            #print(self.mem)
            cmd = self.mem[self.ptr] % 100
            pmm = self.mem[self.ptr] // 100
            if (cmd == 1): # Add
                p1 = getParam(self.ptr+1, pmm, self.mem)
                p2 = getParam(self.ptr+2, pmm // 10, self.mem)
                self.mem[self.mem[self.ptr+3]] = p1 + p2
                self.ptr += 4
            elif (cmd == 2): # Multiply
                p1 = getParam(self.ptr+1, pmm, self.mem)
                p2 = getParam(self.ptr+2, pmm // 10, self.mem)
                self.mem[self.mem[self.ptr+3]] = p1 * p2
                self.ptr += 4
            elif (cmd == 3): # Input
                if (len(inputs) < 1):
                    #print("Waiting for input...")
                    break 
                inp = inputs.pop(0)
                #print(f"input {inp}")
                self.mem[self.mem[self.ptr+1]] = int(inp)
                self.ptr += 2
            elif (cmd == 4): # Input
                outputs.append(getParam(self.ptr + 1, pmm, self.mem))
                self.ptr += 2
            elif (cmd == 5): # Jump if true
                p1 = getParam(self.ptr+1, pmm, self.mem)
                p2 = getParam(self.ptr+2, pmm // 10, self.mem)
                if (p1 != 0):
                    self.ptr = p2
                else:
                    self.ptr += 3
            elif (cmd == 6): # Jump if false
                p1 = getParam(self.ptr+1, pmm, self.mem)
                p2 = getParam(self.ptr+2, pmm // 10, self.mem)
                if (p1 == 0):
                    self.ptr = p2
                else:
                    self.ptr += 3
            elif (cmd == 7): # Less than
                p1 = getParam(self.ptr+1, pmm, self.mem)
                p2 = getParam(self.ptr+2, pmm // 10, self.mem)
                if (p1 < p2):
                    self.mem[self.mem[self.ptr+3]] = 1
                else:
                    self.mem[self.mem[self.ptr+3]] = 0
                self.ptr += 4
            elif (cmd == 8): # Equals
                p1 = getParam(self.ptr+1, pmm, self.mem)
                p2 = getParam(self.ptr+2, pmm // 10, self.mem)
                if (p1 == p2):
                    self.mem[self.mem[self.ptr+3]] = 1
                else:
                    self.mem[self.mem[self.ptr+3]] = 0
                self.ptr += 4
            elif (cmd == 99): # End
                self.running = False
                #print(f"Program terminated with {outputs}")
                break
            else:
                self.running = False
                print("ERROR: Unknown command at position {}".format(self.ptr))
                break
        return outputs

def permutate(list):
    permutations = []
    ll = len(list)
    if (ll < 2):
        return [list]
    for i in range(ll):
        perm = list.copy()
        first = perm.pop(i)
        for last in permutate(perm):
            last.insert(0, first)
            permutations.append(last)
    return permutations

def initProgs():
    progs = []
    for i in range(5):
        progs.append(Program(program))
    return progs

def runCombination(combination):
    progs = initProgs()
    output = [0]
    while (progs[4].running):
        for i in range(5):
            if(combination):
                output.insert(0, combination.pop(0))
            #print(f"running prog {i} with input {output}")
            output = progs[i].run_prog(output)
    return output[0]

def tryAll(combination):
    highscore = 0
    for p in permutate(combination):
        score = runCombination(p.copy())
        if (score > highscore):
            highscore = score
            print(f"New highscore {highscore} for combination {p}")
    return highscore

filepath = 'input'
with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

tryAll([5,6,7,8,9])






