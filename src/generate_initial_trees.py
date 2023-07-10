import os

from mpboot import generateMPBootCommand
from multiprocessing.pool import Pool

from utils import readFile
from utils import writeFile

def generateInitialTrees(initial_software: str, msa_path: str, number_initial_trees: int) -> list:
    initial_trees = []
    tree_number = 0
    
    parsimony_command = generateMPBootCommand(initial_software, msa_path)

    #for tree in range(number_initial_trees):
    #    print("generating parsimony tree {}".format(tree))
    #    os.system(parsimony_command)
    #    initial_tree = readFile(msa_path + ".treefile")
    #    initial_trees.append(initial_tree)

    with Pool() as pool:
        items =[(parsimony_command, msa_path, i) for i in range(number_initial_trees)]
        pool.starmap(parallelGenerateTrees, items)

    for tree_number in range(number_initial_trees):
        command = "cat tree." + str(tree_number) + ".treefile >> parsimony.treefile"
        os.system(command)
        initial_tree = readFile("tree.{}.treefile".format(tree_number))
        initial_trees.append(initial_tree)

    return initial_trees

def writeInitialTrees(initial_trees: list):
    for i in range(len(initial_trees)):
        writeFile("initial_trees.treefile", initial_trees[i])

def parallelGenerateTrees(parsimony_command, msa_path, tree_number):
    loop_parsimony_command = parsimony_command + " -pre tree." + str(tree_number)
    loop_parsimony_command = loop_parsimony_command + " > /dev/null 2>&1"
    os.system(loop_parsimony_command)
