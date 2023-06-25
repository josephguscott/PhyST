import os

from mpboot import generateMPBootCommand

from utils import readFile
from utils import writeFile

def generateInitialTrees(initial_software: str, msa_path: str, number_initial_trees: int) -> list:
    initial_trees = []
    
    parsimony_command = generateMPBootCommand(initial_software, msa_path)

    for tree in range(number_initial_trees):
        os.system(parsimony_command)
        initial_tree = readFile(msa_path + ".treefile")
        initial_trees.append(initial_tree)

    return initial_trees

def writeInitialTrees(initial_trees: list):
        for i in range(len(initial_trees)):
            writeFile("initial_trees.treefile", initial_trees[i])
