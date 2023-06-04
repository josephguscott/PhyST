#!/usr/bin/env python3

import argparse
import time
import traceback

from evaluate_trees import EvaluateTrees
from generate_trees import GenerateTrees
from print import PhystPrint
from utils import writeFile

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--msa', type=str, help='input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)
PARSER.add_argument('--init-trees', type=int, help='the number of initial trees generated', default=100)
PARSER.add_argument('--init-software', type=str, help='software used to generate initial trees', default='mpboot')
PARSER.add_argument('--ml-software', type=str, help='software used to generate ML trees', default='iqtree')

args = vars(PARSER.parse_args())
MSA_PATH = args['msa']
INIT_TREE_SIZE = args['init_trees']
INIT_SOFTWARE = args['init_software']
ML_SOFTWARE = args['ml_software']

def main():
    try:
        initial_trees = []
        best_initial_trees = []

        program_start = time.time()

        PhystPrint.printHeader()

        PhystPrint.printSoftwareConfig(INIT_SOFTWARE, MSA_PATH, INIT_TREE_SIZE, ML_SOFTWARE)

        print("Generating initial trees...")

        init_trees = GenerateTrees(INIT_SOFTWARE, MSA_PATH, INIT_TREE_SIZE)
        initial_trees = init_trees.generateInitialTrees()

        for i in range(len(initial_trees)):
            writeFile("parsimony.treefile", initial_trees[i])
            print(initial_trees[i])

        evaluate_initial_trees = EvaluateTrees(MSA_PATH)
        evaluate_initial_trees.getLikelihoodScores()

        program_end = time.time()

        runtime = program_end - program_start
        print("")
        print("Wall-clock time : ", time.strftime("%H:%M:%S:", time.gmtime(runtime)))
            
    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")
        traceback.print_tb(err.__traceback__)
        exit(1)

if __name__ == "__main__":
    main()