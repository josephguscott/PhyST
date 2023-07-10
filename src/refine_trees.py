import os

from iqtree import iqtreeLikelihoodAnalysis

def refineInitialTrees(msa_path:str):
    treefile = msa_path + ".treefile"
    logfile = msa_path + ".log"

    refine_tree_command = iqtreeLikelihoodAnalysis(msa_path)
    os.system(refine_tree_command)

    with open(logfile, "r") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.startswith("BEST SCORE FOUND : "):
                output = line

    best_score = output.split(": ")

    print("")
    print("Refined ML tree score: {}Refined ML treefile: {}".format(best_score[-1], treefile))