import os

from software.iqtree import IqtreeLikelihoodAnalysis

def RefineInitialTrees(msa_path: str, cores: int, iqtree_options: str) -> None:
    treefile = msa_path + ".treefile"
    logfile = msa_path + ".log"

    refine_tree_command = IqtreeLikelihoodAnalysis(msa_path, cores, iqtree_options)
    os.system(refine_tree_command)

    with open(logfile, "r") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.startswith("BEST SCORE FOUND : "):
                output = line

    best_score = output.split(": ")

    print("")
    print("Refined ML tree score: {}Refined ML treefile: {}".format(best_score[-1], treefile))