# Copyright 2024 The PHYST Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import time

from args import Args
from multiprocessing import cpu_count
from preprocessing import Preprocessing
from print import Print
from processing import Processing
from log import LOG

class Physt:
    def __init__(self) -> None:
        self.args = Args()

    def execute(self):
        if self.args.VERBOSE is True:
            LOG.info('Starting in debug mode')

        Print(self.args)
        
        program_start = time.time()
        #PhystPreprocessing = Preprocessing(args.NUM_MP_TREES, args.HARDWARE, args.MP_SOFTWARE, args.MSA_INPUT_PATH)
        #PhystProcessing = Processing(args.HARDWARE, args.MSA_INPUT_PATH, args.IQ_TREE_OPTIONS)

        # generate starting trees, currently only uses MPBoot
        #PhystPreprocessing.GenerateStartingTrees()
        #PhystPreprocessing.FilterStartingTrees()

        # refine initial trees using IQ-Tree
        #PhystProcessing.RefineStartingTrees()

        program_end = time.time()

        runtime = program_end - program_start
        Print.PrintRuntime(runtime)

        # remove old files
        # os.system("rm tree.* initial_trees_* initial_trees.treefile parsimony.treefile")

        if self.args.VERBOSE is True:
            LOG.info('Run completed')