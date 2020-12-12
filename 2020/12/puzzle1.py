import sys

dirs = ["E", "S", "W", "N"]
d = 0
x = 0
y = 0

with open(sys.argv[1]) as fp:
	line = fp.readline().strip()
	while line:
		print(line)
		v = int(line[1:])
		if (line.startswith("F")):
			line = f'{dirs[d]}{v}'
			#print(f' {line}')
		if (line.startswith("R")):
			d += int(v / 90)
			d = d % 4
		elif (line.startswith("L")):
			d -= int(v / 90)
			d = d % 4
		elif (line.startswith("E")):
			x += v
		elif (line.startswith("S")):
			y += v
		elif (line.startswith("W")):
			x -= v
		elif (line.startswith("N")):
			y -= v

		print(f'{x},{y} facing {dirs[d]}  dist = {abs(x)+abs(y)}')
		line = fp.readline().strip()
