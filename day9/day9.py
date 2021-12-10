with open('file.in') as f:
	content = f.readlines()
content = [list(map(str, x.strip())) for x in content]
for z, row in enumerate(content):
	content[z] = [int(x) for x in row]
total = 0
watersheds = []


def check_paths(content, need_checked, watershed):
	new_checked = []
	for need in need_checked:
		x = need[0]
		y = need[1]
		watershed.append(str(x) + ',' + str(y))
		if x - 1 >= 0:
			if content[y][x-1] != 9:
				new_checked.append((x-1, y))
		if x + 1 < len(content[y]):
			if content[y][x+1] != 9:
				new_checked.append((x+1, y))
		if y - 1 >= 0:
			if content[y-1][x] != 9:
				new_checked.append((x, y-1))
		if y + 1 < len(content):
			if content[y+1][x] != 9:
				new_checked.append((x, y+1))
	new_checked = list(set(new_checked))
	for new_need in new_checked:
		to_check = str(new_need[0]) + ',' + str(new_need[1])
		if to_check in watershed:
			new_checked = list(filter(lambda a: a != (new_need[0], new_need[1]), new_checked))
	if len(new_checked) > 0:
		return check_paths(content, new_checked, watershed)
	return watershed


def check_watersheds(watersheds, val):
	for each in watersheds:
		for value in each:
			if val == value:
				return True
	return False


for y, row in enumerate(content):
	for x, col in enumerate(row):
		val = str(x) + ',' + str(y)
		if not check_watersheds(watersheds, val) and col != 9:
			watersheds.append(check_paths(content, [[x, y]], []))
		check = True
		if x - 1 >= 0:
			if row[x-1] <= col:
				check = False
		if x + 1 < len(row):
			if row[x+1] <= col:
				check = False
		if y - 1 >= 0:
			if content[y-1][x] <= col:
				check = False
		if y + 1 < len(content):
			if content[y+1][x] <= col:
				check = False
		if check:
			total += 1 + col
# Part 1
print(total)
count = [len(x) for x in watersheds]
total_basins = 1
count.sort()
for x in count[len(count) - 3:]:
	total_basins *= x
# Part 2
print(total_basins)


