import re
filepath = 'input'

hgtPat = re.compile(r'^(\d+)(.*)$')
hclPat = re.compile(r'^#[0-9a-f]{6}$')
allowed_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
pidPat = re.compile(r'^[0-9]{9}$')
def byr(f):
	return 1920 <= int(f) <= 2002
def iyr(f):
	return 2010 <= int(f) <= 2020
def eyr(f):
	return 2020 <= int(f) <= 2030
def hgt(f):
	(v, u) = hgtPat.match(f).groups()
	if (u == "cm"):
		return 150 <= int(v) <= 193
	elif (u == "in"):
		return 59 <= int(v) <= 76
	else:
		return False
def hcl(f):
	return hclPat.match(f)
def ecl(f):
	return f in allowed_ecl
def pid(f):
	return pidPat.match(f)

required = {"byr": byr, "iyr": iyr,"eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}

tot = 0
valid = 0
with open(filepath) as fp:
	fields = []
	line = fp.readline()
	while line:
		lf = line.strip().split(" ")
		if (lf[0]):
			fields += lf
		else:
			fields = dict(map(lambda f: f.split(":"), fields))
			tot += 1
			approved = True
			for req in required:
				if (req not in fields):
					approved = False
					break
				elif (not required[req](fields[req])):
					print(f'Failed on {req}: {fields[req]}')
					approved = False
					break
			if (approved):
				valid += 1
			fields = []
		line = fp.readline()

print(f'Found {valid} valid passports out of {tot}')
