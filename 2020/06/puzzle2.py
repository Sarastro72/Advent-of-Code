filepath="input"

with open(filepath) as fp:
	answers = {}
	people = 0
	count = 0
	line = fp.readline()
	while line:
		line = line.strip()
		if (line):
			people += 1
			for a in line:
				answers[a] = answers.get(a, 0) + 1
		else:
			for a in answers.values():
				if a == people:
					count += 1
			print(f'group count {count}  ({people} people)')
			answers = {}
			people = 0
		line = fp.readline()

print(f'Total count {count}')
