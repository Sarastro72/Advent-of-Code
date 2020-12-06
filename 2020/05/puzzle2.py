import re

filepath = 'input'

def readValue(v):
	return int(re.sub(r'[BR]', '1', re.sub(r'[FL]', '0', v)), 2)

with open(filepath) as fp:
     values = sorted(list(map(readValue, fp)))

last = False
for i in range(0, 1023):
	if (i not in values):
		if (last):
			print(f"Your seat is {i}")
			break
	else:
		last = True
