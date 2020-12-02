import re

filepath = 'input'
pattern = re.compile(r'(\d+)-(\d+) (.): (.*)')

valid = 0
with open(filepath) as fp:
	line = fp.readline()
	while line:
		(fro, to, c, pw) = pattern.match(line).groups()
		print(f'{fro} - {to} {c}   {pw}')
		v = f'{pw[int(fro)-1]}{pw[int(to)-1]}'
		if (v.count(c) == 1):
			print(f'{pw} is valid ({v})')
			valid += 1

		line = fp.readline()

print(f'Found {valid} valid passwords')
