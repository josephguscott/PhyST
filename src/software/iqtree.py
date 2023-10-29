def IqtreeEvaluateTreesCommand(msa_path: str, cores: int) -> str:
        iqtree_path = "./lib/iqtree "
        pass_msa = "-s " + msa_path
        pass_treefile = " -z initial_trees.treefile"
        no_search = " -n 0"
        parallel = " -nt " + str(cores)

        evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + parallel
        evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

        return evaulate_tree_command

def IqtreeLikelihoodAnalysis(msa_path: str, cores: int, iqtree_options: str) -> str:
    likelihood_command = ""
    
    iqtree_path = "./lib/iqtree "
    pass_msa = "-s " + msa_path
    pass_treefile = " -t initial_trees_best.treefile"
    parallel = " -nt " + str(cores)
    user_options = " " + iqtree_options

    likelihood_command = iqtree_path + pass_msa + pass_treefile + parallel + user_options       
    likelihood_command = likelihood_command + " > /dev/null 2>&1"

    print(likelihood_command)

    return likelihood_command