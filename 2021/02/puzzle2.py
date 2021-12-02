import sys

with open(sys.argv[1]) as fp:
	line = fp.readline().strip()
	a = 0
	p = 0
	d = 0
	while line:
		print(f"{p} * {d}")
		val = int(line.split(" ")[1])
		if (line.startswith("f")):
			p += val
			d += a * val
		elif (line.startswith("d")):
			a += val
		elif (line.startswith("u")):
			a -= val


		line = fp.readline().strip()

print(f"{p} * {d}  {p*d}")
