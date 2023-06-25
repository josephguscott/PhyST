import os

from iqtree import iqtreeLikelihoodAnalysis

def refineInitialTrees(msa_path:str):
    treefile = msa_path + ".treefile"
    refine_tree_command = iqtreeLikelihoodAnalysis(msa_path)
    
    os.system(refine_tree_command)

    print("Refined ML tree written to", treefile)