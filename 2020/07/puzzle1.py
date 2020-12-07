import re
import sys
from collections import deque

bag_pattern = re.compile(r'^(\d+) (.+) bags?\.?$')

class Rule:
    def __init__(self, line):
    	self.canContain = []
    	(obj, subj) = line.strip().split(" bags contain ")
    	self.name = obj
    	if (subj != "no other bags."):
	    	for c in subj.split(", "):
	    		(n, t) = bag_pattern.match(c).groups()
	    		self.canContain.append(t)

    def __repr__(self):
    	return f'[{self.name} can contain {", ".join(self.canContain)}]'


rules = {}

with open(sys.argv[1]) as fp:
	line = fp.readline()
	while line:
		rule = Rule(line)
		rules[rule.name] = rule
		line = fp.readline()

queue = deque(["shiny gold"])
containers = {}

while queue:
	item = queue.popleft()
	for r in rules.values():
		if (item in r.canContain):
			if (not containers.get(r.name)):
				print(f'{r.name} can contain {item}')
				queue.append(r.name)
				containers[r.name] = r


print(f'Found {len(containers)} bags that can contain shiny golden bags')
