import os
import time
import linecache
import argparse

from print import *

# evaluate_trees.py functions

def ParseEvaluateCommandLineOptions():
    parser = argparse.ArgumentParser()

    parser.add_argument("--msa", metavar='<MSA>', type=str, help = 'input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)

    args = parser.parse_args()

    return args

def GenerateTreeEvaluateCommand(args):
    iqtree_path = "./lib/iqtree "
    pass_msa = "-s " + args.msa
    pass_treefile = " -z parsimony.treefile"
    no_search = " -n 0"
    redo = " -redo" 

    evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + redo

    evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

    return evaulate_tree_command

def lines_that_start_with(string, fp):
    return [line for line in fp if line.startswith(string)]

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

def GetBestTreeScores(args):
    file = args.msa
    file = file + ".log"
    
    all_trees = []
    current_score = []
    all_scores = []
    best_scores =[]

    with open(file, "r") as fp:
        for line in lines_that_start_with("Tree ", fp):
            all_trees.append(line)
            score = line.split()
            all_scores.append(score[-1]) 

    all_scores.sort()

    for i in range(5):
        best_scores.append(all_scores[i])

    return best_scores

def GetBestTreesNumber(args, best_scores):
    file = args.msa
    file = file + ".log"

    best_trees = []
    best_trees_number = []

    for i in range(5):
        with open(file, "r") as fp:
            for line in lines_that_contain(best_scores[i], fp):
                best_trees.append(line)
                tree_number = line.split()
                best_trees_number.append(tree_number[1])

    return best_trees_number

def GetBestTrees(args, best_trees_number):
    file = "parsimony.treefile"

    line_numbers = []
    lines = []

    for i in range(5):
        line_numbers.append(int(best_trees_number[i]))
    
    for i in line_numbers:
        x = linecache.getline(file, i).strip()
        lines.append(x)

    with open('parsimony.treefile.best', 'w') as fp:
        for i in lines:
            fp.write("%s\n" % i)

# evaluate_trees.py script

args = ParseEvaluateCommandLineOptions()

evaluate_tree_command = GenerateTreeEvaluateCommand(args)

start = time.time()

os.system(evaluate_tree_command)

best_scores = GetBestTreeScores(args)

best_trees_number = GetBestTreesNumber(args, best_scores)

print("Best likelihood trees:")

for i in range(5):
    print("  Tree", best_trees_number[i], ":", best_scores[i])

print("")
print("Trees printed to 'parsimony.treefile.best'")

best_trees = GetBestTrees(args, best_trees_number)

end = time.time()

runtime = end - start

print("")
print("Tree evaluation complete!")

print("Wall-clock time : ", time.strftime("%H:%M:%S:", time.gmtime(runtime)))