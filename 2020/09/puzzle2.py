import sys

with open(sys.argv[1]) as fp:
	stream = list(map(int, fp))

target = 85848519
first=0
last=1
summ = stream[first] + stream[last]
while (summ != target):
	if (summ < target):
		last +=1
		summ += stream[last]
	else:
		summ -= stream[first]
		first +=1

lowest = min(stream[first:last+1])
highest = max(stream[first:last+1])

print(f'The range from {stream[first]} to {stream[last]} works, answer is {lowest + highest}')
