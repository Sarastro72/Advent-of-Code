#!/usr/local/bin/python

filepath = 'input'
with open(filepath) as fp:
    strings = fp.readline().strip().split(",")
    data = list(map(int, strings))

ptr=0
while True:
    cmd = data[ptr]
    if (cmd == 1): # Add
        data[data[ptr+3]] = data[data[ptr+1]] + data[data[ptr+2]]
    elif (cmd == 2): # Multiply
        data[data[ptr+3]] = data[data[ptr+1]] * data[data[ptr+2]]
    elif (cmd == 99): # End
        print("Program terminated normally at position {}".format(ptr))
        break
    else:
        print("ERROR: Unknown command at poistion {}".format(ptr))
        break
    ptr += 4

print("Data: {}".format(data))
