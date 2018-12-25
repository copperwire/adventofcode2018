
with open("./input_two.txt", "r") as fo:
	lines = fo.readlines()
	for i, l in enumerate(lines, ):
		lines[i] = int(l)

freq_dict = {}
curr = lines[0]
counter = 1
freq_dict[lines[0]] = 1 
cont_iter = True
num_iter = len(lines)

solution = None

while cont_iter:
	next_var = curr + lines[counter]
	try:
		tmp = freq_dict[next_var]
		cont_iter = False
		solution = next_var
	except KeyError:
		freq_dict[next_var] = 1
		counter += 1
		curr = next_var
		if counter == num_iter:
			counter = 0

print(solution)