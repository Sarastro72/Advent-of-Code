filepath = 'input'
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

with open(filepath) as fp:
     map = fp.read().splitlines()

height = len(map)
width = len(map[0])

answer = 1
for slope in slopes:
	trees = 0
	x = 0
	for d in range(0, height, slope[1]):
		t = map[d][x]
		if (t == '#'):
			trees += 1
		x = (x + slope[0]) % width
	print(f'Encountered {trees} trees on slope {slope}')
	answer *= trees

print(f'Answer = {answer}')
