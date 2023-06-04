#!/usr/bin/env python3

import argparse
import traceback

from generate_trees import GenerateTrees

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--msa', type=str, help='input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)
PARSER.add_argument('--init-trees', type=int, help='the number of initial trees generated', default=100)
PARSER.add_argument('--init-software', type=str, help='software used to generate initial trees', default='mpboot')

args = vars(PARSER.parse_args())
MSA_PATH = args['msa']
INIT_TREE_SIZE = args['init_trees']
INIT_SOFTWARE = args['init_software']

def main():
    try:
        initial_trees = []
        best_initial_trees = []

        init_trees = GenerateTrees(INIT_SOFTWARE, MSA_PATH, INIT_TREE_SIZE)
        initial_trees = init_trees.GenerateInitialTrees()

        for i in range(len(initial_trees)):
            print(initial_trees[i])
    
    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")
        traceback.print_tb(err.__traceback__)
        exit(1)

if __name__ == "__main__":
    main()