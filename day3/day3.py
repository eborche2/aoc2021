import functools

with open('file.in') as f:
	content = f.readlines()
content = [list(map(int, x.strip())) for x in content]


def most_common(value_list, length):
	return ['1' if x >= length/2 else '0' for x in value_list]


def least_common(value_list):
	print(value_list)
	return ''.join(['0' if x == '1' else '1' for x in value_list])


def reduce_by_position(lis, pos, incdec):
	return [x for x in lis if x[pos] == incdec]


def add_values(value_list):
	added_values = [0] * len(content[0])
	for value in value_list:
		for z in range(len(content[0])):
			added_values[z] += value[z]
	return added_values


added_list = add_values(content)
mc = most_common(added_list, len(content))
lc = least_common(mc)
mc = ''.join(mc)
# Part 1
print(mc, lc, int(mc, 2) * int(lc, 2))
mc_second = content
lc_second = content

for x in range(len(content[0])):
	if len(mc_second) > 1:
		mc_second = reduce_by_position(mc_second, x, int(mc[x]))
		print('most_common', mc_second)
		mc = most_common(add_values(mc_second), len(mc_second))
	if len(lc_second) > 1:
		lc_second = reduce_by_position(lc_second, x, int(lc[x]))
		print('least_common', lc_second)
		lc = least_common(most_common(add_values(lc_second), len(lc_second)))
	mc = ''.join(mc)
# Part 2
print(mc_second, lc_second, int(''.join([str(x) for x in mc_second[0]]), 2) * int(''.join([str(x) for x in lc_second[0]]), 2))
