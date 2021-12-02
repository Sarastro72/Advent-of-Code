import sys

with open(sys.argv[1]) as fp:
	depths = list(map(int, fp))

count = 0
for i in range(3, len(depths)):
	if (depths[i] > depths[i - 3]):
		count += 1

print(count)
