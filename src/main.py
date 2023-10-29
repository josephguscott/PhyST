#!/usr/bin/env python3

import argparse
import os
import time
import traceback

from datetime import datetime
from multiprocessing import cpu_count

from refine_trees import RefineInitialTrees
from log import Log, LOG
from print import Print
from preprocessing.preprocessing import Preprocessing

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--msa', type=str, help='input MSA in Phylp/Fasta/Nexus/Clustal format', required=True)
PARSER.add_argument('--init-trees', type=int, help='the number of initial trees generated', default=100)
PARSER.add_argument('--init-software', type=str, help='software used to generate initial trees', default='mpboot')
PARSER.add_argument('--ml-software', type=str, help='software used to generate ML trees', default='iqtree')
PARSER.add_argument('--parallel', type=int, help='number of cores to be used', default=1)
PARSER.add_argument('--max-parallel', type=bool, help='run PHYST using maximum resources', action=argparse.BooleanOptionalAction, default=False)
PARSER.add_argument('--iqtree-options', type=str, help='give iq-tree any user specified options', default='')

args = vars(PARSER.parse_args())
MSA_PATH = args['msa']
INIT_TREE_SIZE = args['init_trees']
INIT_SOFTWARE = args['init_software']
ML_SOFTWARE = args['ml_software']
TIMESTAMP = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
IQ_TREE_OPTIONS = args['iqtree_options']

if args['max_parallel'] is True:
    HARDWARE = cpu_count()
else:
    HARDWARE = args['parallel']

def main():
    try:
        program_start = time.time()

        PhystPrint = Print(INIT_SOFTWARE, MSA_PATH, INIT_TREE_SIZE, ML_SOFTWARE, TIMESTAMP, HARDWARE)
        PhystPreprocessing = Preprocessing(INIT_TREE_SIZE, HARDWARE, INIT_SOFTWARE, MSA_PATH)

        PhystPrint.PrintStartup()

        # generate starting trees, currently only uses MPBoot
        PhystPreprocessing.GenerateStartingTrees()
        PhystPreprocessing.FilterStartingTrees()

        # refine initial trees using maximum likelihood
        RefineInitialTrees(MSA_PATH, HARDWARE, IQ_TREE_OPTIONS)

        program_end = time.time()

        runtime = program_end - program_start
        Print.PrintRuntime(runtime)

        # remove old files
        os.system("rm tree.* initial_trees_* initial_trees.treefile parsimony.treefile")
            
    except Exception as err:
        LOG.critical(f"{type(err).__name__}: {err}")
        traceback.print_tb(err.__traceback__)
        exit(1)

if __name__ == "__main__":
    main()