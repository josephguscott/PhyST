import os

import linecache

from iqtree import iqtreeEvaluateTreesCommand

def filterInitialTrees(msa_path: str):
        evaluate_command = iqtreeEvaluateTreesCommand(msa_path)
        os.system(evaluate_command)
        best_trees_dict = getBestTreesDictionary(msa_path)
        best_scores = identifyBestTrees(msa_path)
        best_trees_number = identifyTreeNumber(msa_path, best_scores)
        print("Highest scoring likelihood trees:")

        for i in range(len(best_trees_number)):
            print("  Tree", best_trees_number[i], ":", best_scores[i])

        writeBestInitialTreesFile(best_trees_number)

def getBestTreesDictionary(msa_path: str) -> dict:
    file = msa_path + ".log"
    best_trees_dict = {}

    with open(file, "r") as fp:
        for line in fp:
            if line.startswith("Tree "):
                tree_line = line.split()
                tree = "Tree " + tree_line[1]
                score = tree_line[-1]
                best_trees_dict[tree] = score

    print(best_trees_dict)

    return best_trees_dict

def identifyBestTrees(msa_path: str) -> list:
    # needs refactoring
    file = msa_path
    file = file + ".log"
        
    all_trees = []
    all_scores = []
    best_scores = []

    with open(file, "r") as fp:
        for line in fp:
            if line.startswith("Tree "):
                all_trees.append(line)
                score = line.split()
                all_scores.append(score[-1]) 

    all_scores.sort()

    for i in range(5):
        best_scores.append(all_scores[i])

    return best_scores

def identifyTreeNumber(msa_path: str, best_scores: list) -> list:
    # needs refactoring
    file = msa_path
    file = file + ".log"

    best_trees = []
    best_trees_number = []

    with open(file, "r") as fp:
        lines = fp.readlines()
        for i in range(5):
            for line in lines:
                if line.startswith("Tree "):
                    if best_scores[i] in line:
                        best_trees.append(line)
                        tree_number = line.split()
                        best_trees_number.append(tree_number[1])
                        lines.remove(line) # stops the same tree being repeatedly added
                        break # stops extra trees being assigned on last loop

    return best_trees_number

def writeBestInitialTreesFile(best_trees_number: list):
    # needs refactoring
    file = "initial_trees.treefile"

    line_numbers = []
    lines = []

    for i in range(5):
        line_numbers.append(int(best_trees_number[i]))
        
    for i in line_numbers:
        x = linecache.getline(file, i).strip()
        lines.append(x)

    with open('initial_trees_best.treefile', 'w') as fp:
        for i in lines:
            fp.write("%s\n" % i)

    for i in range(5):
        j = str(i + 1)
        file_name = "initial_trees_best_" + j + ".treefile"

        with open(file_name, 'w') as fp:
            fp.write("%s\n" % lines[i])
