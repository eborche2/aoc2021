with open('file.in') as f:
	content = f.readlines()
content = [list(map(int, x.strip().split(','))) for x in content][0]


def calculate(days):
	master = {}
	for x in range(9):
		master[str(x)] = 0
	for x in content:
		master[str(x)] += 1
	for x in range(days):
		previous = master.copy()
		for key in master.keys():
			if key == '0':
				master['0'] -= previous[key]
				master['6'] += previous[key]
				master['8'] += previous[key]
			else:
				master[key] -= previous[key]
				master[str(int(key) - 1)] += previous[key]
	total = 0
	for x in master.values():
		total += x
	print(total)


# Part 1
calculate(80)
# Part 2
calculate(256)
