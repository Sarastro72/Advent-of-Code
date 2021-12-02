import sys

with open(sys.argv[1]) as fp:
	now = int(fp.readline().strip())
	table = fp.readline().strip().split(",")

def get_second(val):
	return val[1]

busses = []
for i in range(0, len(table)):
	if (table[i] == "x"):
		continue
	busses.append((i, int(table[i])))
busses = sorted(busses, key=get_second)

print(table)
print(busses)

quit()

rpos = 0
for o in range(0, len(offsets)):
	target = offsets[o][0]
	bus = offsets[o][2]
	print(f'   Bus {bus}  ({offsets[o][1]})')
	for i in range(0, 10000):
		rpos += offsets[o][1]
		rpos = rpos % first
		if (rpos == target):
			print(f'target hit after {i} ({i * first})')
			break

