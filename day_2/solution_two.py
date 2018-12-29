from Levenshtein import distance

fn = "input_one.txt"
with open(fn, "r", ) as fo:
	lines = fo.readlines()
	for i, l in enumerate(lines):
		lines[i] = l.strip("\n")

string_set_dict = {u: set(u) for u in lines}
closest = [None, None]
comp = 0


for l1 in lines:
	l1s = string_set_dict[l1]
	
	for l2 in lines:
		l2s = string_set_dict[l2]
		
		if (l1s < l2s) or (l2s > l1s):
			comp += 1
			dist = distance(l1, l2)

			if dist == 1:
				closest[0] = l1
				closest[1] = l2


print(closest)
print(len(lines)**2, comp)