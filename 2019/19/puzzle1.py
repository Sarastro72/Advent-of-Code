import sys
sys.path.append('..')
from intCode import IntComputer
output = []
process = IntComputer.fromFile(sys.argv[1], outFunc= lambda v : output.append(v))
mmap = []
count = 0
for y in range(50):
    line = ""
    for x in range(50):
        process.reset().run([x,y])
        beam = output.pop()
        if (beam):
            line += "#"
            count += 1
        else:
            line += " "
    mmap.append(line)

for l in mmap:
    print(l)
print(f"Count: {count}")
