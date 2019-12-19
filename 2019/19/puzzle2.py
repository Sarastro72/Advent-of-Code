import sys
sys.path.append('..')
from intCode import Process
output = []
process = Process.fromFile(sys.argv[1], outFunc= lambda v : output.append(v))

dw = 138
dx = 864

def readBeam(x,y): 
    process.reset().run([x, y])
    return output.pop()

def tryLine(y):
    x = (y * dx // 1010)
    beam = 1
    while (beam):
        beam = readBeam(x, y)
        if (beam):
            x += 1
    x -=1
    if (readBeam(x - 99, y) == 1 and readBeam(x -99, y + 99) == 1):
        print (f"Found fit at ({x-99}, {y})")
        return True
    else:
        return False

step=1024
y = 1000
last = False
while True:
    fit = tryLine(y)
    if (fit and step == 1):
        break
    if (last != fit and step > 1):
        step //= 2
    if fit:
        y -= step
    else:
        y += step
    last = fit
