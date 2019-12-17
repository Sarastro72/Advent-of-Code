#!/usr/local/bin/python
import sys

def run_program(noun, verb):
    data = list(map(int, strings))
    data[1] = noun
    data[2] = verb

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

    return data[0]

filepath = 'input'
with open(filepath) as fp:
    strings = fp.readline().strip().split(",")

for noun in range(99):
    for verb in range(99):
        result = run_program(noun, verb)
        print("noun {}, verb {}, result {}".format(noun, verb, result))
        if (result == 19690720):
            print("Found the correct pair!")
            sys.exit(0)
