import os

from mpboot import generateMPBootCommand
from multiprocessing.pool import Pool

from utils import readFile
from utils import writeFile

def generateInitialTrees(initial_software: str, msa_path: str, number_initial_trees: int, cores: int) -> list:
    initial_trees = []
    tree_number = 0
    
    parsimony_command = generateMPBootCommand(initial_software, msa_path)

    # generate initial trees in parallel 
    with Pool(processes = cores) as pool:
        items =[(parsimony_command, i) for i in range(number_initial_trees)]
        pool.starmap(parallelGenerateTrees, items)

    # concatenate trees into a single file
    for tree_number in range(number_initial_trees):
        command = "cat tree." + str(tree_number) + ".treefile >> parsimony.treefile"
        os.system(command)
        initial_tree = readFile("tree.{}.treefile".format(tree_number))
        initial_trees.append(initial_tree)

    return initial_trees

def writeInitialTrees(initial_trees: list):
    for i in range(len(initial_trees)):
        writeFile("initial_trees.treefile", initial_trees[i])

def parallelGenerateTrees(parsimony_command: str, tree_number: int):
    loop_parsimony_command = parsimony_command + " -pre tree." + str(tree_number)
    loop_parsimony_command = loop_parsimony_command + " > /dev/null 2>&1"
    os.system(loop_parsimony_command)
