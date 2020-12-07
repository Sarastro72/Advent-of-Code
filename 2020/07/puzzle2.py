import re
import sys

bag_pattern = re.compile(r'^(\d+) (.+) bags?\.?$')

class Rule:
    def __init__(self, line):
    	self.canContain = []
    	(obj, subj) = line.strip().split(" bags contain ")
    	self.name = obj
    	if (subj != "no other bags."):
	    	for c in subj.split(", "):
	    		(n, t) = bag_pattern.match(c).groups()
	    		self.canContain.append((int(n),t))

    def __repr__(self):
    	return f'[{self.name} can contain {", ".join(map(lambda l: l[1], self.canContain))}]'

def mustContain(name):
	count = 0
	rule = rules[name]
	for c in rule.canContain:
		count += c[0] * (1 + mustContain(c[1]))
	print(f'{name} bag must contain {count} bags')
	return count

rules = {}

with open(sys.argv[1]) as fp:
	line = fp.readline()
	while line:
		rule = Rule(line)
		rules[rule.name] = rule
		line = fp.readline()

mustContain("shiny gold")
