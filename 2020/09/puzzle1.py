import sys

with open(sys.argv[1]) as fp:
	stream = list(map(int, fp))

for i in range(25, len(stream)):
	found = False
	#print(f'i = {i}')
	for d in range(2, 26):
		t = i - d
		#print(f'  t = {t}')
		rest = stream[i] - stream[t]
		for s in range(1, d):
			#print(f'    t+s = {t+s}')
			if (stream[t+s] == rest):
				found = True
				print(f'{stream[t]} + {stream[t+s]} = {stream[i]}')
				break
		if (found):
			break
	if (not found):
		print(f'Found faulty number {stream[i]} at position {i}')
		break
