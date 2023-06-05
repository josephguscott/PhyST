import os
import time
import argparse

from print import *

# likelihood_analysis.py functions

def ParseLikelihoodCommandLineOptions():
    parser = argparse.ArgumentParser()

    parser.add_argument("--msa", metavar='<MSA>', type=str, help = 'input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)
    args = parser.parse_args()

    return args

def GenerateLikelihoodCommand(args):
    iqtree_path = "./lib/iqtree "
    pass_msa = "-s " + args.msa
    pass_treefile = " -t initial_trees_best.treefile"
    redo = " -redo" 

    likelihood_command = iqtree_path + pass_msa + pass_treefile + redo

    likelihood_command = likelihood_command + " > /dev/null 2>&1"

    return likelihood_command

# likelihood_analysis.py script

args = ParseLikelihoodCommandLineOptions()

likelihood_command = GenerateLikelihoodCommand(args)

start = time.time()

os.system(likelihood_command)

end = time.time()

runtime = end - start

print("")
print("IQ-Tree complete!")

print("Wall-clock time : ", time.strftime("%H:%M:%S:", time.gmtime(runtime)))