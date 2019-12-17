#!/usr/local/bin/python3

with open("input") as fp:
    string = fp.readline().strip()
    input = list(map(int, list(string)))

input = input * 10000

skip = int("".join([str(i) for i in input[:7]]))

length = len(input)
count = 1
for i in range(100):
    output = [0] * length
    for p in range(length-1, skip-1, -1):
        if (p == length-1):
            output[p] = input[p]
        else:
            output[p] = (input[p] + output[p + 1]) % 10
    input = output
    print(f"{count}\r", end="")
    count += 1

ostr = "".join([str(d) for d in output[skip:skip+8]])

print(ostr)
