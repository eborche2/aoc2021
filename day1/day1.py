with open('file.in') as f:
	content = f.readlines()
content = [int(x.strip()) for x in content]


def calculate(nums):
	increases = 0
	decreases = 0
	for x, each in enumerate(nums):

		if x > 0:
			if each > nums[x-1]:
				increases += 1
				print(x, nums[x-1], each, 'increases', increases)
			else:
				print(x, nums[x-1], each, 'decreases', decreases)
				decreases += 1
	print('increases', increases)


# Part 1
calculate(content)

sums = []
for x, each in enumerate(content):
	if x > 1:
		sums.append(each + content[x-1] + content[x-2])
# Part 2
calculate(sums)
