import re

filepath = 'input'
pattern = re.compile(r'(\d+)-(\d+) (.): (.*)')

valid = 0
with open(filepath) as fp:
	line = fp.readline()
	while line:
		(fro, to, c, pw) = pattern.match(line).groups()
		print(f'{fro} - {to} {c}   {pw}')
		count = pw.count(c)
		if (count >= int(fro) and count <= int(to)):
			print(f'{pw} is valid')
			valid += 1

		line = fp.readline()

print(f'Found {valid} valid passwords')
