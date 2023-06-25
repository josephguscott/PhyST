import os

from iqtree import iqtreeLikelihoodAnalysis
from iqtree import iqtreeEvaluateTreesCommand

def refineInitialTrees(msa_path:str, number_initial_trees: int):
    refine_tree_command = iqtreeLikelihoodAnalysis(msa_path)
    
    for i in range(0, number_initial_trees):
        os.system(refine_tree_command[i])


    
    # print("Likelihood tree printed to {}.treefile".format(msa_path))
