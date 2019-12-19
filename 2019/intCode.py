class Process:
    def __init__(self, program, ptr=0, inFunc = None, outFunc = None):
        self.program = program
        self.outFunc = outFunc or (lambda v : print(v))
        self.inFunc = inFunc or (lambda : input("Input: "))
        self.reset(ptr)

    @staticmethod
    def fromFile(filePath, inFunc = None, outFunc = None):
        with open(filePath) as fp:
            strings = fp.readline().strip().split(",")
            program = list(map(int, strings))
            return Process(program, inFunc = inFunc, outFunc = outFunc)

    def reset(self, ptr = 0):
        self.ptr = ptr
        self.mem = [0] * 8096 # 8k shold be enough for everyone
        self.ptr = ptr
        self.running = True
        self.realtiveBase = 0
        for i in range(len(self.program)):
            self.mem[i] = self.program[i]
        return self

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
                    inp = self.inFunc()
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
