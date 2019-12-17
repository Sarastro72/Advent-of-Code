#!/usr/local/bin/python3

basePattern=[0, 1, 0, -1]

def getPattern(position, length):
    pattern = []
    i = 0
    while (len(pattern) <= length):
        pattern += [basePattern[i]] * (position + 1)
        i = (i + 1) % len(basePattern) 
    return pattern[1:length+1]

with open("input") as fp:
    string = fp.readline().strip()
    input = list(map(int, list(string)))

length = len(input)
for i in range(100):
    output = []
    for op in range(length):
        pattern = getPattern(op, length)
        val = 0
        for ip in range(length):
            val += input[ip] * pattern[ip]
        val = abs(val) % 10
        output.append(val)
    print(output[:8])
    input = output

ostr = "".join([str(d) for d in output[:8]])

print(ostr)