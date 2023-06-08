def GenerateLikelihoodCommand(msa_path):
    likelihood_commands = []

    for i in range(1,6):
        iqtree_path = "./lib/iqtree "
        pass_msa = "-s " + msa_path
        pass_treefile = " -t initial_trees_best_{}.treefile".format(i)
        prefix = " = pre best_tree_{}.treefile".format(i)
        redo = " -redo" 

        likelihood_command = iqtree_path + pass_msa + pass_treefile + prefix + redo

        likelihood_command = likelihood_command + " > /dev/null 2>&1"

        likelihood_commands.append(likelihood_command)

    return likelihood_commands