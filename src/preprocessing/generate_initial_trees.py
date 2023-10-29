import os

from software.mpboot import GenerateMPBootCommand
from multiprocessing.pool import Pool

from utils.utils import ReadFile
from utils.utils import WriteFile

def GenerateInitialTrees(initial_software: str, msa_path: str, number_initial_trees: int, cores: int) -> list:
    initial_trees = []
    tree_number = 0
    
    parsimony_command = GenerateMPBootCommand(initial_software, msa_path)

    # generate initial trees in parallel 
    with Pool(processes = cores) as pool:
        items =[(parsimony_command, i) for i in range(number_initial_trees)]
        pool.starmap(ParallelGenerateTrees, items)

    # concatenate trees into a single file
    for tree_number in range(number_initial_trees):
        command = "cat tree." + str(tree_number) + ".treefile >> parsimony.treefile"
        os.system(command)
        initial_tree = ReadFile("tree.{}.treefile".format(tree_number))
        initial_trees.append(initial_tree)

    return initial_trees

def WriteInitialTrees(initial_trees: list) -> None:
    for i in range(len(initial_trees)):
        WriteFile("initial_trees.treefile", initial_trees[i])

def ParallelGenerateTrees(parsimony_command: str, tree_number: int) -> None:
    loop_parsimony_command = parsimony_command + " -pre tree." + str(tree_number)
    loop_parsimony_command = loop_parsimony_command + " > /dev/null 2>&1"
    os.system(loop_parsimony_command)
