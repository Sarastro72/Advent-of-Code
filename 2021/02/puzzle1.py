import sys

with open(sys.argv[1]) as fp:
	line = fp.readline().strip()
	p = 0
	d = 0
	while line:
		print(f"{p} * {d}")
		val = int(line.split(" ")[1])
		if (line.startswith("f")):
			p += val
		elif (line.startswith("d")):
			d += val
		elif (line.startswith("u")):
			d -= val


		line = fp.readline().strip()

print(f"{p} * {d}  {p*d}")
