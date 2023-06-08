import os

from utils import readFile

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

        initial_tree = readFile(self.msa_path + ".treefile")

        return initial_tree