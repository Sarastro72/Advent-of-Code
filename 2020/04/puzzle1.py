
filepath = 'input'
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

tot = 0
valid = 0
with open(filepath) as fp:
	fields = []
	line = fp.readline()
	while line:
		lf = line.strip().split(" ")
		lf = list(map(lambda f: f.split(":")[0], lf))
		if (lf[0]):
			fields += lf
		else:
			tot += 1
			approved = True
			for req in required:
				if (req not in fields):
					#print(f'{fields} is invalid')
					approved = False
					break
			if (approved):
				valid += 1
				print(f'*{valid} {fields}')
			fields = []
		line = fp.readline()

print(f'Found {valid} valid passports out of {tot}')
