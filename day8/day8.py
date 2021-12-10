with open('file.in') as f:
	content = f.readlines()
content = [x.split(' ') for x in content]
leds = []
map_letters = []
count = 0
for each in content:
	map_letters.append([x.strip() for x in each[0:10]])
	result = [x.strip() for x in each[11:]]
	leds.append(result)
	for val in result:
		if len(val) in [2, 3, 4, 7]:
			count += 1
print(count)


def figure_numbers(vals):
	compute = [0] * 7
	sorted_list = list(sorted(vals, key=len))
	paused = []
	three_found = False
	for letters in sorted_list:
		if len(letters) == 2:
			compute[0] = letters[0]
			compute[1] = letters[1]
		elif len(letters) == 3:
			for let in letters:
				if let not in compute:
					compute[6] = let
					break
		elif len(letters) == 4:
			for let in letters:
				if let not in compute:
					if compute[4] == 0:
						compute[4] = let
					else:
						compute[5] = let
		elif len(letters) == 5:
			found_zero = False
			found_one = False
			possible_two = 0
			flip = False
			if not three_found:
				for let in letters:
					if let == compute[0]:
						found_zero = True
					if let == compute[1]:
						found_one = True
					if let not in compute:
						possible_two = let
					elif let == compute[6]:
						pass
					elif let == compute[5]:
						flip = True
				if found_one and found_zero:
					three_found = True
					compute[2] = possible_two
					if flip:
						hold = compute[4]
						compute[4] = compute[5]
						compute[5] = hold
					if len(paused) > 0:
						for not_computed in paused:
							for let in not_computed:
								if let not in compute:
									compute[3] = let
									if compute[0] not in not_computed:
										hold = compute[0]
										compute[0] = compute[1]
										compute[1] = hold
				else:
					paused.append(letters)
			else:
				for let in letters:
					if let not in compute:
						compute[3] = let
						if compute[0] not in letters:
							hold = compute[0]
							compute[0] = compute[1]
							compute[1] = hold
	return compute


truth = {
	'0':  [0, 1, 2, 3, 5, 6],
	'1':  [0, 1],
	'2': [0, 2, 3, 4, 6],
	'3': [0, 1, 2, 4, 6],
	'4': [0, 1, 4, 5],
	'5': [1, 2, 4, 5, 6],
	'6': [1, 2, 3, 4, 5, 6],
	'7': [0, 1, 6],
	'8': [0, 1, 2, 3, 4, 5, 6],
	'9': [0, 1, 2, 4, 5, 6]
}
total = 0
for x, figure in enumerate(map_letters):
	map_key = figure_numbers(figure)
	led = ''
	for digits in leds[x]:
		key = []
		for letter in digits:
			key.append(map_key.index(letter))
		pos = list(truth.values()).index(sorted(key))
		led += list(truth.keys())[pos]
	total += int(led)
print(total)








