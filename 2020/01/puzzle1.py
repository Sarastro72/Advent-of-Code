filepath = 'input'
target = 2020

with open(filepath) as fp:
     values = sorted(list(map(int, fp)))

bot = 0
top = len(values) - 1

while (top != bot):
	sum = values[top] + values[bot]
	print(f"{values[top]} + {values[bot]} = {sum}")
	if (sum == target):
		print(f"Answer = {values[top] * values[bot]}")
		break
	if (sum > target):
		top -= 1
	else:
		bot += 1
