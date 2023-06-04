import os
import time
import argparse
import linecache

from multiprocessing import Pool
from multiprocessing import cpu_count
from print import *

# parsimony_analysis.py functions

def ParseParsimonyCommandLineOptions():
    parser = argparse.ArgumentParser()

    parser.add_argument("--msa", metavar='<MSA>', type=str, help = 'input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)
    args = parser.parse_args()

    return args

def GenerateParsimonyTreesCommand(args):
    mpBootTreePath = "./lib/mpboot "
    passMSA = "-s " + args.msa        
    mpBootCommand = mpBootTreePath + passMSA
    mpBootCommand = mpBootCommand + " > /dev/null 2>&1"

    return mpBootCommand

def GenerateParsimonyTree(i):
        print("  Generating parsimony tree")
        os.system(mpBootCommand)
        push_treefile = "cat " + args.msa + ".treefile >> parsimony.treefile"
        os.system(push_treefile)

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
        best_scores.append(all_scores[i]) # throws error if trees left from old parsimony file

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

    for i in range(5):
        j = str(i + 1)
        file_name = "parsimony.treefile.best_"
        file_name = file_name + j

        with open(file_name, 'w') as fp:
            fp.write("%s\n" % lines[i])

def GenerateLikelihoodCommand(args, i):
    j = str(i + 1)
    iqtree_path = "./lib/iqtree "
    pass_msa = "-s " + args.msa
    pass_treefile = " -t parsimony.treefile.best_"
    redo = " -redo"
    pre = " -pre likelihood_analysis."

    likelihood_command = iqtree_path + pass_msa + pass_treefile + j + " " + redo + pre + j

    likelihood_command = likelihood_command + " > /dev/null 2>&1"

    print(likelihood_command)

    return likelihood_command

def RunLikelihoodAnalysis(i):
        likelihood_command = GenerateLikelihoodCommand(args, i)
        os.system(likelihood_command)

# parsimony_analysis.py script

printPHYSTHeader()

args = ParseParsimonyCommandLineOptions()

defaultMPTrees = 100

print("PHYST configuration:")
print("  Parsimony software: MPBoot ")
print("  Alignment file:", args.msa)
print("  Replicates: 100 (default)")
print("")
print("  Evaluation software: IQ-Tree ")
print("  High scoring trees: 5 (default)")
print("")
print("  Likelihood software: IQ-Tree ")
print("")
print("MPBoot provided by Hoang, et al., 2018; https://doi.org/10.1186/s12862-018-1131-3")
print("IQ-Tree provided by Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015")
print("")

mpBootCommand = GenerateParsimonyTreesCommand(args)

available_processors = cpu_count()

print("Running MPBoot in parallel on", available_processors, "processors for", defaultMPTrees, "replicates...")

start = time.time()

with Pool() as pool:
    pool.map(GenerateParsimonyTree, range(defaultMPTrees))

print("")
print("Parsimony tree generation complete!")
print("Evaluating likelihood scores of all trees")

evaluate_tree_command = GenerateTreeEvaluateCommand(args)

os.system(evaluate_tree_command)

best_scores = GetBestTreeScores(args)

best_trees_number = GetBestTreesNumber(args, best_scores)

print("Highest scoring likelihood trees:")

for i in range(5):
    print("  Tree", best_trees_number[i], ":", best_scores[i])

print("")
print("Evaluation results: ")
print("  Highest scoring tree: Tree", best_trees_number[0], ":", best_scores[0])
print("  All parsimony trees: parsimony.treefile")
print("  Highest scoring trees: parsimony.treefile.best")
print("")
print("Running likelihood analysis")

best_trees = GetBestTrees(args, best_trees_number)

with Pool() as pool:
    if cpu_count() > 5:
        pool = Pool(processes=5)
        
    pool.map(RunLikelihoodAnalysis, range(5))

end = time.time()

runtime = end - start
print("")
print("  Wall-clock time : ", time.strftime("%H:%M:%S:", time.gmtime(runtime)))