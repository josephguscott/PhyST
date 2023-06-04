import os
from multiprocessing import Pool

from parsimony_analysis import ParsimonyAnalysis

class GenerateTrees:
    def __init__(self, 
                 software_name, 
                 msa_path,
                 init_tree_size) -> None:
        
        self.software_name = software_name
        self.msa_path = msa_path
        self.init_tree_size = init_tree_size

    def GenerateInitialTrees(self):
        parsimony_command = ParsimonyAnalysis.MPBootCommand(self, self.msa_path)
    
        init_trees = []
    
        for i in range(0, self.init_tree_size):
            init_trees.append(ParsimonyAnalysis.getTree(self, parsimony_command))

        return init_trees

