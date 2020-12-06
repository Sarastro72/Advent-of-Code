import re

filepath = 'input'

def readValue(v):
	return int(re.sub(r'[BR]', '1', re.sub(r'[FL]', '0', v)), 2)

with open(filepath) as fp:
     values = sorted(list(map(readValue, fp)))

print(f'Top value {values[-1]}')
