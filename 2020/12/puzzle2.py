import sys

sx = 0
sy = 0
wx = 10
wy = -1


def rot(i):
	global wx, wy
	for i in range(0, i % 4):
		t = -wy
		wy = wx
		wx = t

with open(sys.argv[1]) as fp:
	line = fp.readline().strip()
	while line:
		print(line)
		v = int(line[1:])
		if (line.startswith("F")):
			sx += wx * v
			sy += wy * v
		elif (line.startswith("R")):
			rot(int(v / 90))
		elif (line.startswith("L")):
			rot(int(-v / 90))
		elif (line.startswith("E")):
			wx += v
		elif (line.startswith("S")):
			wy += v
		elif (line.startswith("W")):
			wx -= v
		elif (line.startswith("N")):
			wy -= v

		print(f'ship {sx},{sy}  wp {wx},{wy}  dist = {abs(sx)+abs(sy)}')
		line = fp.readline().strip()
