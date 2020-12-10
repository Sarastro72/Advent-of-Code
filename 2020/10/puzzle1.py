import sys

with open(sys.argv[1]) as fp:
     val = sorted(list(map(int, fp)))
val.insert(0, 0)

ones = 0
threes = 1
for i in range(1, len(val)):
	diff = val[i] - val[i-1]
	if (diff == 1):
		ones += 1
	elif (diff == 3):
		threes += 1

print(f'ones: {ones}, threes {threes}, answer {ones * threes}')
