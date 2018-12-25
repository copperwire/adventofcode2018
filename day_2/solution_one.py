import re

fn = "input_one.txt"
with open(fn, "r", ) as fo:
	lines = fo.readlines()
	for i, l in enumerate(lines):
		lines[i] = l.strip("\n")

two_occ = 0
three_occ = 0
alphabet = "qwertyuiopasdfghjklzxcvbnm"
reg_exps = {u: re.compile(r"("+u+")") for u in alphabet}


def FindPairs(l):
	unique = set(l)
	ret_val = [0, 0]

	for u in unique:
		tmp = len(reg_exps[u].findall(l))
		
		if tmp == 2:
			ret_val[0] = 1
		elif tmp == 3:
			ret_val[1] = 1
		elif sum(ret_val) == 2:
			return ret_val

	return ret_val


for l in lines:
	tw, th = FindPairs(l)
	two_occ += tw
	three_occ += th

print(two_occ * three_occ)