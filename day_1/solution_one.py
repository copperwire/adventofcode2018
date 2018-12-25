
with open("./input_one.txt", "r") as fo:
	lines = fo.readlines()
	for i, l in enumerate(lines, ):
		lines[i] = float(l)

print(sum(lines, ))