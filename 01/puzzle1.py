#!/usr/local/bin/python

filepath = 'input'
with open(filepath) as fp:
   line = fp.readline()
   fuelval=0
   while line:
       fuelval += int(line.strip()) / 3 - 2
       line = fp.readline()

print("Total fuel needed: {}".format(fuelval))
