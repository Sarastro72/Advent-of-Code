#!/usr/local/bin/python3

start=138241
end=  674034

def getDigit(number, ordinal):
    return (number // ordinal) % 10

def isGoodPin(pin):
    pair = False
    last = pin % 10
    rep = 1
    while (pin > 0):
        pin = pin // 10
        digit = pin % 10
        if (digit > last):
            return False
        if (digit == last):
            rep += 1
        else:
            if (rep == 2):
                pair = True
            rep = 1
        last = digit
    return pair or rep == 2

def loop(number, ordinal):
    #print(f"{number}, {ordinal}")
    val = 0
    digit = getDigit(number, ordinal)
    for i in range(digit, 10):
        if (ordinal == 1):
            if (isGoodPin(number)):
                print (f"{number} is good")
                val += 1
            number += 1
        else:
            nextOrdinal = ordinal // 10
            val += loop(number, nextOrdinal)
            number += ordinal
            number = number // ordinal * ordinal
            number += digit

        if (number >= end):
            break    
    print(val)
    return val

print (isGoodPin(123345))
print (isGoodPin(123456))

loop(start, 100000)