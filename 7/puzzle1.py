#!/usr/local/bin/python

def getParam(adr, mode, data):
    if ((mode & 1) == 0):
        return data[data[adr]]
    else:
        return data[adr]

def run(mem, inputs):
    ptr=0
    outputs = []
    while True:
        #print(mem)
        cmd = mem[ptr] % 100
        pmm = mem[ptr] // 100
        if (cmd == 1): # Add
            p1 = getParam(ptr+1, pmm, mem)
            p2 = getParam(ptr+2, pmm // 10, mem)
            mem[mem[ptr+3]] = p1 + p2
            ptr += 4
        elif (cmd == 2): # Multiply
            p1 = getParam(ptr+1, pmm, mem)
            p2 = getParam(ptr+2, pmm // 10, mem)
            mem[mem[ptr+3]] = p1 * p2
            ptr += 4
        elif (cmd == 3): # Input
            inp = inputs.pop(0)
            #print(f"input {inp}")
            mem[mem[ptr+1]] = int(inp)
            ptr += 2
        elif (cmd == 4): # Input
            outputs.append(getParam(ptr + 1, pmm, mem))
            ptr += 2
        elif (cmd == 5): # Jump if true
            p1 = getParam(ptr+1, pmm, mem)
            p2 = getParam(ptr+2, pmm // 10, mem)
            if (p1 != 0):
                ptr = p2
            else:
                ptr += 3
        elif (cmd == 6): # Jump if false
            p1 = getParam(ptr+1, pmm, mem)
            p2 = getParam(ptr+2, pmm // 10, mem)
            if (p1 == 0):
                ptr = p2
            else:
                ptr += 3
        elif (cmd == 7): # Less than
            p1 = getParam(ptr+1, pmm, mem)
            p2 = getParam(ptr+2, pmm // 10, mem)
            if (p1 < p2):
                mem[mem[ptr+3]] = 1
            else:
                mem[mem[ptr+3]] = 0
            ptr += 4
        elif (cmd == 8): # Equals
            p1 = getParam(ptr+1, pmm, mem)
            p2 = getParam(ptr+2, pmm // 10, mem)
            if (p1 == p2):
                mem[mem[ptr+3]] = 1
            else:
                mem[mem[ptr+3]] = 0
            ptr += 4
        elif (cmd == 99): # End
            #print(f"Program terminated normally at position {ptr} with output {outputs}")
            break
        else:
            print("ERROR: Unknown command at poistion {}".format(ptr))
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

def runCombination(combination):
    val = 0
    for phase in combination:
        val = run(program.copy(), [phase, val])[0]
    return val

def tryAll(combination):
    highscore = 0
    for p in permutate(combination):
        score = runCombination(p)
        highscore = max(score, highscore)
    return highscore

filepath = 'input'
with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    program = list(map(int, strings))

print(tryAll([0,1,2,3,4]))








