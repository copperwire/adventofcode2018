import numpy as np
import matplotlib.pyplot as plt

fn = "input_one.txt"

with open(fn, "r", ) as fo:
	lines = fo.readlines()
	relative_coord = []
	ids = []

	for i, l in enumerate(lines):
		tmp = l.strip("\n")
		id_val, coord = tmp.split("@")
		dist, size = coord.split(":")
		dist = [int(i) for i in dist.split(",")]
		size = [int(i) for i in size.split("x")]
		id_val = int(id_val.strip("#"))

		ids.append(id_val)
		relative_coord.append([dist, size])

point_sets = []
max_val_x = 1000
max_val_y = 1000
fabric = np.zeros((max_val_x, max_val_y, 1))
id_map = np.zeros((max_val_x, max_val_y, 1))
spoiled_ids = set()

for i, obj in enumerate(relative_coord):
	dist, size = obj 

	x_start = dist[0] 
	y_start = dist[1]
	
	x_end = dist[0] + size[0]
	y_end = dist[1] + size[1] 

	for x in range(x_start, x_end):
		for y in range(y_start, y_end):
			fabric[x, y] += 1
			if fabric[x, y] > 1:
				spoiled_ids.add(ids[i])
				spoiled_ids.add(int(id_map[x, y]))
			id_map[x, y] = ids[i]

#fabric = fabric.reshape((max_val_x, max_val_y))
#bool_mask = np.nonzero(fabric > 1,)
print(len(spoiled_ids), len(ids))
print([x for x in ids if x not in spoiled_ids])

# plt.imshow(fabric)
# plt.show()
