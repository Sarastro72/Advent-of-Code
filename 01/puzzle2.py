#!/usr/local/bin/python

def calculateFuel(mass, fuel_so_far=0):
    fuel = mass / 3 - 2
    if (fuel <= 0):
        return fuel_so_far

    return calculateFuel(fuel, fuel_so_far + fuel)

    
filepath = 'input'

with open(filepath) as fp:
    line = fp.readline()
    fuelval=0
    while line:
        mass=int(line.strip())
        fuelval += calculateFuel(mass)
        line = fp.readline()

print("Total fuel needed: {}".format(fuelval))


