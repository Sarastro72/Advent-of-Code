import sys

with open(sys.argv[1]) as fp:
     val = sorted(list(map(int, fp)))
val.insert(0, 0)

node = {}
node[0] = 1

for i in range(1, len(val)):
	j = i -1
	comb = 0
	while (j >= 0 and val[j] + 3 >= val[i]):
		comb += node[j]
		j -= 1
	node[i] = comb
	print(f'Ways to {val[i]}: {node[i]}')
