with open('file.in') as f:
	content = f.readlines()
content = [list(map(int, x.strip().split(','))) for x in content][0]
content.sort()


def align_whales(single=True):
	least = content[0]
	most = content[len(content) - 1] + 1
	total = None
	for x in range(least, most):
		current = 0
		for z, value in enumerate(content):
			if value == 0:
				if single:
					current += x
				else:
					#import pdb; pdb.set_trace()
					current += step_adder(x)
			else:
				if single:
					current += abs(x - value)
				else:
					#import pdb; pdb.set_trace()
					current += step_adder(abs(x - value))
			if total and current > total:
				break
			elif z == len(content) - 1:
				if not total or current < total:
					total = current
	return total


def step_adder(step):
	return sum([x for x in range(1, step + 1)])


# Part 1
print(align_whales())
# Part 2
print(align_whales(False))
