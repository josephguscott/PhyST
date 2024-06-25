# Constructs command to run all datasets through mpboot-physt

import os
from itertools import product
params = list(product([50,200],[10000,100000],[0.1,1.0],['equal','mammal']))
for set in params:
	taxa = str(set[0])
	seq_length = str(set[1])
	branch_length = str(set[2])
	sub_rate = str(set[3])
	os.system(f"experiment_mpboot/script.sh {taxa} {seq_length} {branch_length} {sub_rate} > experiment_mpboot/mpboot_{taxa}_{seq_length}_{branch_length}_{sub_rate}.out 2>&1")
