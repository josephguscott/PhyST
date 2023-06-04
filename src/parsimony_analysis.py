import os

class ParsimonyAnalysis:
    def __init__(self) -> None:
        pass

    def generateParsimonyCommand(self, msa_path):
        software_path = "./lib/mpboot "
        pass_msa_path = "-s " + msa_path       
        parsimony_command = software_path + pass_msa_path
        parsimony_command = parsimony_command + " > /dev/null 2>&1"

        return parsimony_command
    
    def getTree(self, parsimony_command):
        os.system(parsimony_command)

        with open(self.msa_path + ".treefile") as treefile:
            for line in treefile:
                initial_tree = line

        return initial_tree