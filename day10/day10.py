values = {
	')': 3,
	']':57,
	'}': 1197,
	'>': 25137
}
opens = ['(', '[', '{', '<']
matches = {
	'{': '}',
	'(': ')',
	'[': ']',
	'<': '>'
}
syntax_values = {
	'(': 1,
	'[': 2,
	'{': 3,
	'<': 4
}
with open('file.in') as f:
	content = f.readlines()
content = [list(map(str, x.strip())) for x in content]
tally = 0
syntax_scores = []
for row in content:
	popped = []
	broken = False
	for bracket in row:
		if bracket in opens:
			popped.append(bracket)
		else:
			matched = popped.pop()
			if matches[matched] != bracket:
				tally += values[bracket]
				broken = True
				break
	if not broken:
		syntax = 0
		while len(popped) > 0:
			syntax = (syntax * 5) + syntax_values[popped.pop()]
		syntax_scores.append(syntax)
# Part 1
print(tally)
# Part 2
syntax_scores.sort()
print(syntax_scores[int(len(syntax_scores) / 2)])
