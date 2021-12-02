import sys

with open(sys.argv[1]) as fp:
	now = int(fp.readline().strip())
	busses = fp.readline().strip().split(",")

wt = 999999
best = 0
for b in busses:
	if (b == 'x'):
		continue
	bus = int(b)
	wait = bus - (now % bus)
	print(f'Bus {b} wait time {wait}')
	if (wait < wt):
		wt = wait
		best = bus

print(f'Best bus is {best} you need ot wait {wt} minutes.   ({best * wt})')
