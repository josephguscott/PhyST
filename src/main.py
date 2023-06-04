#!/usr/bin/env python3

import argparse
import traceback

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--msa', type=str, help='input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)
PARSER.add_argument('--init-trees', type=int, help='the number of initial trees generated', default=5)
PARSER.add_argument('--init-software', type=str, help='software used to generate initial trees', default='mpboot')

args = vars(PARSER.parse_args())
MSA_PATH = args['msa']
INIT_TREE_SIZE = args['init_trees']
INIT_SOFTWARE = args['init_software']

# generate init trees

def main():
    try:
        print(MSA_PATH)
        print(INIT_TREE_SIZE)
        print(INIT_SOFTWARE)
    
    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")
        traceback.print_tb(err.__traceback__)
        exit(1)

if __name__ == "__main__":
    main()