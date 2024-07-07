from ete3 import Tree
from itertools import product
import subprocess
import re

def CompareTrees(prediction, ground_truth):
	pred = Tree(prediction)
	truth = Tree(ground_truth)
	comparison = pred.robinson_foulds(truth,unrooted_trees=True)
	rf = comparison[0]
	rf_max = comparison[1]
	return rf, rf_max

params = list(product([50,200],[10000,100000],[0.1,1.0],['equal','mammal']))
with open("RF_mpboot_rep1.txt",'w') as f:
	for set in params:
		taxa = str(set[0])
		seq_length = str(set[1])
		branch_length = str(set[2])
		sub_rate = str(set[3])
		prediction = f"alignment_{taxa}_{seq_length}_{branch_length}_{sub_rate}.phy.treefile"
		truth = f"../../../sim_trees/alignment_{taxa}_{seq_length}_{branch_length}_{sub_rate}.treefile"
		result = subprocess.run(['find','.','-name',prediction],capture_output=True,text=True)
		prediction = result.stdout.strip()
		rf, rf_max = CompareTrees(prediction,truth)
		f.write(f"MPBoot rep1. Taxa = {taxa}, Seq. length = {seq_length}, Branch length = {branch_length}, Sub. rate = {sub_rate}.\n")
		f.write(f"RF distance is {rf} over a total of {rf_max}\n")
		physt_output = f"mpboot_{taxa}_{seq_length}_{branch_length}_{sub_rate}_rep1.out"
		with open(physt_output) as f2:
			file = f2.read()
			times = re.findall("(\d*\.\d*)(user|system)",file)
			result = re.findall("Wall-clock time : (.*)\n",file)
			usage = re.search("(\d*)%CPU", file)
			f.write(f"MP time: {result[0]}\n")
			f.write(f"Total time: {result[1]}\n")
			f.write(f"CPU time: {float(times[0][0])+float(times[1][0])}\n")
			f.write(f"CPU usage: {usage[1]}%\n###\n")
			
