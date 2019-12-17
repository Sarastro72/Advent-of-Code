#!/usr/local/bin/python3
import sys

class IntCodePrinter:
    def __init__(self, mem):
        self.mem = mem
        self.ptr = 0
        #print(mem)

    def getParams(self, pos, mode):
        params = []
        for p in range(pos):
            val = self.mem[self.ptr + 1 + p]
            m = (mode // (10 ** p)) % 10
            if (m == 0):
                param = "*%04d" % (val)
            elif (m == 1):
                param = "%d" % (val)
            elif (m == 2):
                param = "b[%d]" % (val)
            params.append(param)
        return params

    def printI(self, inst, nump, mode):
        params = self.getParams(nump, mode)
        pstring = ""
        for p in params:
            pstring += "%-8s " % (p)
        asm = "[%04d]  %-5s  %s" % (self.ptr, inst, pstring)
        raw = self.mem[self.ptr : self.ptr+nump+1]
        print("%-50s %s" % (asm, raw))
        self.ptr += nump + 1

    def print(self):
        while self.ptr < len(self.mem):
            cmd = self.mem[self.ptr] % 100
            mode = self.mem[self.ptr] // 100
            if (cmd == 1): # Add
                self.printI("add", 3, mode)
            elif (cmd == 2): # Multiply
                self.printI("mul", 3, mode)
            elif (cmd == 3): # Input
                self.printI("in", 1, mode)
            elif (cmd == 4): # Output
                self.printI("out", 1, mode)
            elif (cmd == 5): # Jump if true
                self.printI("jtru", 2, mode)
            elif (cmd == 6): # Jump if false
                self.printI("jfls", 2, mode)
            elif (cmd == 7): # Less than
                self.printI("lt", 3, mode)
            elif (cmd == 8): # Equals
                self.printI("eq", 3, mode)
            elif (cmd == 9): # Set relative base
                self.printI("mbase", 1, mode)
            elif (cmd == 99): # End
                self.printI("end", 0, mode)
            else:
                self.printI("nop", 0, 0)

filepath = sys.argv[1]
with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

ip = IntCodePrinter(program)
ip.print()




