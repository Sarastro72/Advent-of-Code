import sys
import re

class Interpreter:
	codePat = re.compile(r'(\w+) ([+-?]\d+)')
	pt = 0
	acc = 0
	debug = True
	def __init__(self, filepath):
		with open(filepath) as fp:
			self.code = fp.read().splitlines()


	def step(self):
		(cmd, sval) = self.codePat.match(self.code[self.pt]).groups()
		val = int(sval)
		pt_inc = 1
		if (cmd == "acc"):
			self.acc += val
		elif (cmd == "jmp"):
			pt_inc = val
		elif (cmd != "nop"):
			print(f'Unknown command {cmd} {val} at {self.pt}')
		if (self.debug):
			print(f'{self.pt}: {cmd} {val}      acc={self.acc}')
		self.pt += pt_inc


comp = Interpreter(sys.argv[1])

visited = {}

while (not visited.get(comp.pt)):
	visited[comp.pt] = 1
	comp.step()

print(f'Finished execution at {comp.pt} with acc={comp.acc}')
