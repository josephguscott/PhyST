import os

class EvaluateTrees():
    def __init__(self,
                 msa_path) -> None:
        
        self.msa_path = msa_path

    def getLikelihoodScores(self):
        evaluate_command = self.generateEvaluateTreesCommand()

        os.system(evaluate_command)


    def generateEvaluateTreesCommand(self):
        iqtree_path = "./lib/iqtree "
        pass_msa = "-s " + self.msa_path
        pass_treefile = " -z parsimony.treefile"
        no_search = " -n 0"
        redo = " -redo" 

        evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + redo

        evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

        return evaulate_tree_command