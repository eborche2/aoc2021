with open('file.in') as f:
	content = f.readlines()
content = [x.split(' ') for x in content]
content = [[x[0], int(x[1])] for x in content]

forward = 0
depth = 0
depthAdded = 0
for pair in content:
	if 'forward' == pair[0]:
		forward += pair[1]
		depthAdded += pair[1] * depth
	elif 'up' == pair[0]:
		depth -= pair[1]
	elif 'down' == pair[0]:
		depth += pair[1]

print(forward, depth, depthAdded, forward * depth, depthAdded * forward)