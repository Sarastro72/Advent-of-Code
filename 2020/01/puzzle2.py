filepath = 'input'
target = 2020

with open(filepath) as fp:
     values=  sorted(list(map(int, fp))) #sorted(fp.read().splitlines())

for mid in range(1,len(values) - 2):
	bot=0
	top=len(values) - 1
	while (top != mid and bot != mid):
		sum = values[top] + values[mid] + values[bot]
		print(f"{values[top]} + {values[mid]} + {values[bot]} = {sum}")
		if (sum == target):
			print(f"Answer = {values[top] * values[mid] * values[bot]}")
			quit()
		if (sum > target):
			top -= 1
		else:
			bot += 1
