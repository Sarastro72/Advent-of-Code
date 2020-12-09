import sys
import re

class Interpreter:
	codePat = re.compile(r'(\w+) ([+-?]\d+)')
	pt = 0
	acc = 0
	debug = False

	def __init__(self, code, debug = False):
		self.code = code.splitlines()
		self.debug = debug

	@staticmethod
	def fromFile(self, filepath):
		with open(filepath) as fp:
			return Interpreter(fp.read())

	def step(self):
		if (self.pt >= len(self.code)):
			return False
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
		return True

with open(sys.argv[1]) as fp:
	original = fp.read().splitlines()

for i in range(len(original)):
	if (original[i].startswith("nop")):
		code = original.copy()
		code[i] = code[i].replace("nop", "jmp")
	elif (original[i].startswith("jmp")):
		code = original.copy()
		code[i] = code[i].replace("jmp", "nop")
	else:
		continue

	print(f'Replaced {original[i]} with {code[i]} at {i}')
	comp = Interpreter("\n".join(code))
	visited = {}
	while (not visited.get(comp.pt)):
		visited[comp.pt] = 1
		if (not comp.step()):
			break


	if (not comp.step()):
		print(f'Successfully finished execution with acc={comp.acc}')
		break
	else:
		print(f'Loop detected at {comp.pt} with acc={comp.acc}\n')
