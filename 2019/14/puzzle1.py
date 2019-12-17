#!/usr/local/bin/python3
import sys

class Substance:
    def __init__(self, name, amount = 1):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.name}"

class Formula:
    def __init__(self, ingredients, result):
        self.ingredients = ingredients
        self.result = result

    def __str__(self):
        ings = ""
        for i in self.ingredients:
            ings += f"{i}  "
        return f"{ings} -> {self.result}"

    def getIngredients(self, amount):
        mul = amount // self.result.amount
        if (amount % self.result.amount):
            mul += 1

        required = []
        for i in self.ingredients:
            r = Substance(i.name, i.amount * mul)
            required.append(r)
        return Formula(required, Substance(self.result.name, self.result.amount * mul))

def readInput(filepath):
    formulas = {}
    with open(filepath) as fp:
        line = fp.readline().strip()    
        while (line):
            (ing, res) = line.split(" => ")
            (amount, name) = res.split(" ")
            result = Substance(name, int(amount))
            ingredients = []
            for i in ing.split(", "):
                (amount, name) = i.split(" ")
                ingredients.append(Substance(name, int(amount)))
            formulas[result.name] = Formula(ingredients, result)
            line = fp.readline().strip()
    return formulas

def takeFromStore(item):
    have = store.get(item.name)
    if (have and have.amount >= item.amount):
        have.amount -= item.amount
        store[need.name] = have
        print(f"    Had {item} in store. Inventory now at {have}")
        return 0
    elif (have):
        del store[need.name]
        remains = item.amount - have.amount
        print(f"    Took {have} from store. Still need {remains}")
        return remains
    else:
        return item.amount

def addStore(name, amount):
    if (store.get(name)):
        store[name].amount += amount
    else:
        store[name] = Substance(name, amount)
    print(f"    Added {amount} leftover {name} to store, currently holds {store[name].amount}")

def addRequirement(item):
    if (required.get(item.name)):
        print(f"  Add need of {item.amount} to {item.name}")
        required[item.name].amount += item.amount
    else:
        print(f"  Add new need of {item.amount} {item.name}")
        required[item.name] = item
        reqNames.insert(0, item.name)

formulas = readInput("input")
reqNames = ["FUEL"]
required = {"FUEL": Substance("FUEL", int(sys.argv[1]))}
store = {}
inert = {}

while (len(reqNames)):
    need = required[reqNames.pop()]
    del required[need.name]
    print(f"Need {need}")
    amount = takeFromStore(need)
    if (amount):
        formula = formulas.get(need.name)
        if (formula):
            fullFormula = formula.getIngredients(amount)
            for i in fullFormula.ingredients:
                addRequirement(i)
            if (fullFormula.result.amount > amount):
                addStore(need.name, fullFormula.result.amount - amount)
        else:
            if (inert.get(need.name)):
                print(f"  Add {amount} to inert substance {need.name}")
                inert[need.name].amount += amount
            else:
                print(f"  Add {amount} inert substance {need.name}")
                inert[need.name] = need

for i in list(inert):
    print(inert[i])
print(1000000000000)



