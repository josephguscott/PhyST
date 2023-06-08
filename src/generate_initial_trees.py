import os

from utils import readFile
from utils import writeFile

class GenerateTrees:
    def __init__(self,
                 software,
                 msa_path,
                 tree_size) -> None:
    
        self.software = software
        self.msa_path = msa_path
        self.tree_size = tree_size

    def generateInitialTrees(self):
        parsimony_command = self.generateParsimonyCommand()
    
        init_trees = []
    
        for i in range(0, self.tree_size):
            os.system(parsimony_command)
            initial_tree = readFile(self.msa_path + ".treefile")
            init_trees.append(initial_tree)

        return init_trees

    def generateParsimonyCommand(self):
        software_path = "./lib/{} ".format(self.software)
        pass_msa_path = "-s " + self.msa_path       
        command = software_path + pass_msa_path
        command = command + " > /dev/null 2>&1"

        return command
    
    @staticmethod
    def writeInitialTrees(initial_trees):
        for i in range(len(initial_trees)):
            writeFile("initial_trees.treefile", initial_trees[i])