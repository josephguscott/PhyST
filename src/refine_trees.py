import os

from iqtree import iqtreeLikelihoodAnalysis

def refineInitialTrees(msa_path:str):
    refine_tree_command = iqtreeLikelihoodAnalysis(msa_path)
    
    print(refine_tree_command)
    os.system(refine_tree_command)
