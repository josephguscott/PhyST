def iqtreeEvaluateTreesCommand(msa_path: str) -> str:
        iqtree_path = "./lib/iqtree "
        pass_msa = "-s " + msa_path
        pass_treefile = " -z initial_trees.treefile"
        no_search = " -n 0"
        redo = " -redo" 

        evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + redo
        evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

        return evaulate_tree_command

def iqtreeLikelihoodAnalysis(msa_path: str) -> str:
    likelihood_command = ""
    
    iqtree_path = "./lib/iqtree "
    pass_msa = "-s " + msa_path
    pass_treefile = " -t initial_trees_best.treefile"
    prefix = " = pre best_tree.treefile"
    redo = " -redo" 

    likelihood_command = iqtree_path + pass_msa + pass_treefile + prefix + redo
    likelihood_command = likelihood_command + " > /dev/null 2>&1"

    return likelihood_command