filepath="input"

with open(filepath) as fp:
	answers = {}
	count = 0
	line = fp.readline()
	while line:
		line = line.strip()
		if (line):
			for a in line:
				answers[a] = 1
		else:
			print(f'Group answered {"".join(sorted(answers.keys()))} {len(answers)}')
			count += len(answers)
			answers = {}
		line = fp.readline()

print(f'Total count {count}')
