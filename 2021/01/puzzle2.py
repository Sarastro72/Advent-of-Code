import sys

with open(sys.argv[1]) as fp:
	depths = list(map(int, fp))

count = 0
for i in range(3, len(depths)):
	a = depths[i-3] + depths[i-2]+ depths[i-1]
	b = depths[i-2]+ depths[i-1] + depths[i]
	if (b > a):
		count += 1

print(count)
