# Constructs command to run all datasets through mpboot, lvb and tnt-physt

import os
from itertools import product
params = list(product(['mpboot','lvb','tnt'],[1,2,3],[50,200],[10000,100000],[0.1,1.0],['equal','mammal']))
for set in params:
	program = str(set[0])
	rep = str(set[1])
	taxa = str(set[2])
	seq_length = str(set[3])
	branch_length = str(set[4])
	sub_rate = str(set[5])
	os.system(f"experiment_{program}/script.sh {taxa} {seq_length} {branch_length} {sub_rate} > experiment_{program}/{program}_{taxa}_{seq_length}_{branch_length}_{sub_rate}_rep{rep}.out 2>&1")
