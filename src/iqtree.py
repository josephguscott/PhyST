def iqtreeEvaluateTreesCommand(msa_path: str, cores: int) -> str:
        iqtree_path = "./lib/iqtree "
        pass_msa = "-s " + msa_path
        pass_treefile = " -z initial_trees.treefile"
        no_search = " -n 0"
        parallel = " -nt " + cores

        evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + parallel
        evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

        return evaulate_tree_command

def iqtreeLikelihoodAnalysis(msa_path: str, cores: int) -> str:
    likelihood_command = ""
    
    iqtree_path = "./lib/iqtree "
    pass_msa = "-s " + msa_path
    pass_treefile = " -t initial_trees_best.treefile"
    parallel = " -nt " + cores

    likelihood_command = iqtree_path + pass_msa + pass_treefile + parallel
    likelihood_command = likelihood_command + " > /dev/null 2>&1"

    return likelihood_command