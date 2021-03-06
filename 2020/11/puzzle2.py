import sys

with open(sys.argv[1]) as fp:
     map1 = fp.read().splitlines()

xd = len(map1[0])
yd = len(map1)

def pos(x, y, map):
	if (0 <= x < xd and 0 <= y < yd):
		return map[y][x]
	else:
		return " "

def neighbours(x, y, map):
	count = 0
	dirs=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
	for d in dirs:
		x1 = x
		y1 = y
		while(True):
			x1 += d[0]
			y1 += d[1]
			c = pos(x1, y1, map)
			if (c == "#"):
				count += 1
				break
			elif(c == "L" or c == " "):
				break
	return count

def iter(map):
	map2 = []
	for y in range(0, yd):
		row = ""
		for x in range(0, xd):
			c = pos(x, y, map)
			n = neighbours(x, y, map)
			#print(f'{c} {n}')
			if (c == "L" and n == 0):
				c =  "#"
			elif (c == "#" and n >= 5):
				c = "L"
			#print(c)
			row += c
		#print(row)
		map2.append(row)
	return map2

def printMap(map):
	for r in map:
		print(r)
	print("")

def countTaken(map):
	count = 0
	for r in map:
		count += r.count("#")
	return count


def mapEqual(map1, map2):
	for r in range(0, yd):
		if (map1[r] != map2[r]):
			return False
	return True


map2 = iter(map1)
while(not mapEqual(map1, map2)):
	printMap(map1)
	map1 = map2
	map2 = iter(map1)

printMap(map2)
print(f'{countTaken(map2)} seats are taken')

