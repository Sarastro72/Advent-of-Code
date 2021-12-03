import sys

def split(str):
	return list(map(int, list(str.strip())))

def filter(list, bitpos, target):
	cnt = acc = 0
	for l in list:
		cnt += 1
		if (l[bitpos] == 1):
			acc += 1
	v = target if (acc >= cnt / 2) else target ^ 1
	res = []
	for l in list:
		if (l[bitpos] == v):
			res.append(l)
	return res

def reduce(list, target):
	bp = 0
	while(len(list) > 1):
		list = filter(list, bp, target)
		bp += 1
	return int("".join(map(str, list[0])), 2)

with open(sys.argv[1]) as fp:
	bits = list(map(split, fp))

o2 = reduce(bits, 1)
co2 = reduce(bits, 0)

print(co2 * o2)
