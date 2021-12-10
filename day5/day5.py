with open('file.in') as f:
	content = f.readlines()
content = [list(map(str, x.strip().split(' -> '))) for x in content]
horizontal_vertical = []
diagonal_lines = []
for each in content:
	start = list(map(int, each[0].split(',')))
	end = list(map(int, each[1].split(',')))
	if start[0] == end[0] or start[1] == end[1]:
		horizontal_vertical.append([start, end])
	else:
		diagonal_lines.append([start, end])


def calculate_horizontal_vertical_lines(h_v_lines):
	values = {}
	for each in h_v_lines:
		pos = 0
		static = 1
		if each[0][0] == each[1][0]:
			pos = 1
			static = 0
		start = each[0][pos]
		end = each[1][pos]
		if start > end:
			hold = start
			start = end
			end = hold
		for x in range(start, end + 1):
			if static == 0:
				key = str(each[0][static]) + ',' + str(x)
			else:
				key = str(x) + ',' + str(each[0][static])
			if key not in values:
				values[key] = 0
			values[key] += 1
	return values


def count_intersections(lines):
	intersections = 0
	for x in lines.values():
		if x > 1:
			intersections += 1
	return intersections


def calculate_diagonals(d_lines, c_lines):
	for each in d_lines:
		start = [each[0][0], each[0][1]]
		end = [each[1][0], each[1][1]]
		while start[0] != end[0] or start[1] != end[1]:
			key = str(start[0]) + ',' + str(start[1])
			if key not in c_lines:
				c_lines[key] = 0
			c_lines[key] += 1
			if start[0] < end[0]:
				start[0] += 1
			else:
				start[0] -= 1
			if start[1] < end[1]:
				start[1] += 1
			else:
				start[1] -= 1
		key = str(end[0]) + ',' + str(end[1])
		if key not in c_lines:
			c_lines[key] = 0
		c_lines[key] += 1
	return c_lines


# Part 1
h_v_lines = calculate_horizontal_vertical_lines(horizontal_vertical)
print(count_intersections(h_v_lines))

# Part 2
all_lines = calculate_diagonals(diagonal_lines, h_v_lines)
print(count_intersections(all_lines))
