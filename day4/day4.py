with open('file.in') as f:
	content = f.readlines()
number = list(map(int, content[0].strip().split(',')))
for x in range(1, len(content)):
	content[x] = content[x].strip().split(' ')
for x in range(1, len(content)):
	content[x] = [int(z) for z in content[x] if z != '']


def figure_smallest_winner_matrices(start, end):
	matrix = []
	verticals = [[] for i in range(5)]
	for x in range(start, end):
		matrix.append(content[x])
		for z, spot in enumerate(content[x]):
			verticals[z].append(spot)
	matrix += verticals
	for da_count, each in enumerate(number):
		for i, value in enumerate(matrix):
			for z, num in enumerate(value):
				if num == each:
					matrix[i][z] = -1
					if matrix[i].count(matrix[i][0]) == len(matrix[i]):
						return da_count, each, matrix


smallest = None
largest = None
last_number = None
last_matrix = None
last_large_number = None
last_large_matrix = None
for x in range(2, len(content), 6):
	nums, winning_number, matrix = figure_smallest_winner_matrices(x, x + 5)
	if not smallest or nums < smallest:
		smallest = nums
		last_number = winning_number
		last_matrix = matrix
	if not largest or nums > largest:
		largest = nums
		last_large_number = winning_number
		last_large_matrix = matrix
not_marked = 0
not_marked_largest = 0
for x in range(5):
	for value in last_matrix[x]:
		if value != -1:
			not_marked += value
for x in range(5):
	for value in last_large_matrix[x]:
		if value != -1:
			not_marked_largest += value
# Part 1
print(last_number * not_marked)
# Part 2
print(largest)
print(last_large_number * not_marked_largest)

