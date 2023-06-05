import os

from tree_scores import TreeScores

class EvaluateTrees:
    def __init__(self,
                 msa_path) -> None:
        
        self.msa_path = msa_path

    def getLikelihoodScores(self):
        evaluate_command = self.generateEvaluateTreesCommand()

        os.system(evaluate_command)

        best_scores = TreeScores.GetBestTreeScores(self, self.msa_path)

        best_trees_number = TreeScores.GetBestTreesNumber(self, self.msa_path, best_scores)

        print("Highest scoring likelihood trees:")

        for i in range(len(best_trees_number)):
            print("  Tree", best_trees_number[i], ":", best_scores[i])

        best_trees =TreeScores.GetBestTrees(self, best_trees_number)


    def generateEvaluateTreesCommand(self):
        iqtree_path = "./lib/iqtree "
        pass_msa = "-s " + self.msa_path
        pass_treefile = " -z initial_trees.treefile"
        no_search = " -n 0"
        redo = " -redo" 

        evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + redo

        evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

        return evaulate_tree_command