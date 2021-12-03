import sys

def split(str):
	return list(map(int, list(str.strip())))

with open(sys.argv[1]) as fp:
	bits = list(map(split, fp))

count = 0
acc = [0] * len(bits[0])

for n in bits:
	count += 1
	for i in range(0, len(n)):
		acc[i] += n[i]

gamma = [0] * len(bits[0])
epsilon = [0] * len(bits[0])
for i in range(0, len(acc)):
	if (acc[i] < count / 2):
		gamma[i] = 0
		epsilon[i] = 1
	else:
		gamma[i] = 1
		epsilon[i] = 0

gamma = int("".join(map(str,gamma)), 2)
epsilon = int("".join(map(str,epsilon)), 2)
print(gamma * epsilon)
