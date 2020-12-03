filepath = 'input'

with open(filepath) as fp:
     map = fp.read().splitlines()

height = len(map)
width = len(map[0])

trees = 0
for d in range(0, height):
	x = d * 3 % width
	t = map[d][x]
	if(t == '#'):
		trees += 1

print(f'Encountered {trees} trees')

