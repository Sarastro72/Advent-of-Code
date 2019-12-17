#!/usr/local/bin/python
data = []

def getParam(adr, mode):
    if ((mode & 1) == 0):
        return data[data[adr]]
    else:
        return data[adr]

filepath = 'input'
with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    data = list(map(int, strings))

ptr=0
while True:
    cmd = data[ptr] % 100
    pmm = data[ptr] // 100
    if (cmd == 1): # Add
        p1 = getParam(ptr+1, pmm)
        p2 = getParam(ptr+2, pmm // 10)
        data[data[ptr+3]] = p1 + p2
        ptr += 4
    elif (cmd == 2): # Multiply
        p1 = getParam(ptr+1, pmm)
        p2 = getParam(ptr+2, pmm // 10)
        data[data[ptr+3]] = p1 * p2
        ptr += 4
    elif (cmd == 3): # Input
        inp = input("Enter input: ")
        data[data[ptr+3]] = int(inp)
        ptr += 2
    elif (cmd == 4): # Input
        print(getParam(ptr + 1, pmm))
        ptr += 2
    elif (cmd == 5): # Jump if true
        p1 = getParam(ptr+1, pmm)
        p2 = getParam(ptr+2, pmm // 10)
        if (p1 != 0):
            ptr = p2
        else:
            ptr += 3
    elif (cmd == 6): # Jump if false
        p1 = getParam(ptr+1, pmm)
        p2 = getParam(ptr+2, pmm // 10)
        if (p1 == 0):
            ptr = p2
        else:
            ptr += 3
    elif (cmd == 7): # Less than
        p1 = getParam(ptr+1, pmm)
        p2 = getParam(ptr+2, pmm // 10)
        if (p1 < p2):
            data[data[ptr+3]] = 1
        else:
            data[data[ptr+3]] = 0
        ptr += 4
    elif (cmd == 8): # Equals
        p1 = getParam(ptr+1, pmm)
        p2 = getParam(ptr+2, pmm // 10)
        if (p1 == p2):
            data[data[ptr+3]] = 1
        else:
            data[data[ptr+3]] = 0
        ptr += 4
    elif (cmd == 99): # End
        print("Program terminated normally at position {}".format(ptr))
        break
    else:
        print("ERROR: Unknown command at poistion {}".format(ptr))
        break

