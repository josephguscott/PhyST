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

import os
from multiprocessing.pool import Pool

from filter_trees import FilterTrees
from log import LOG
from mpboot import GenerateMPBootCommand
from utils import ReadFile
from utils import WriteFile

class InitialTrees:
    def __init__(self, args) -> None:
        self.NUM_INIT_TREES = args.NUM_INIT_TREES
        self.HARDWARE = args.HARDWARE
        self.MP_SOFTWARE = args.MP_SOFTWARE
        self.MSA_INPUT_PATH = args.MSA_INPUT_PATH
        self.NUM_INIT_TREES = args.NUM_INIT_TREES
        self.NUM_MP_TREES = args.NUM_MP_TREES
        self.GenerateStartingTrees()
        self.FilterStartingTrees()

    def GenerateStartingTrees(self) -> None:
        LOG.info(f'Generating initial {self.NUM_INIT_TREES} initial trees using {self.HARDWARE} cores')
        initial_trees = self.GenerateInitialTrees()
        self.WriteInitialTrees(initial_trees)

    def FilterStartingTrees(self) -> None:
        LOG.info(f'Obtaining the best {self.NUM_MP_TREES} initial trees')
        FilterTrees(self.MSA_INPUT_PATH, self.HARDWARE, self.NUM_MP_TREES)

    def GenerateInitialTrees(self) -> list:
        initial_trees = []
        tree_number = 0

        parsimony_command = GenerateMPBootCommand(self.MP_SOFTWARE, self.MSA_INPUT_PATH)

        with Pool(processes = self.HARDWARE) as pool:
            items =[(parsimony_command, i) for i in range(self.NUM_INIT_TREES)]
            pool.starmap(self.ParallelGenerateTrees, items)

        for tree_number in range(self.NUM_INIT_TREES):
            command = "cat tree." + str(tree_number) + ".treefile >> parsimony.treefile"
            os.system(command)
            initial_tree = ReadFile(f'tree.{tree_number}.treefile')
            initial_trees.append(initial_tree)

        return initial_trees

    def WriteInitialTrees(self, initial_trees: list) -> None:
        for i in range(len(initial_trees)):
            WriteFile("initial_trees.treefile", initial_trees[i])

    def ParallelGenerateTrees(self, parsimony_command: str, tree_number: int) -> None:
        loop_parsimony_command = parsimony_command + " -pre tree." + str(tree_number)
        loop_parsimony_command = loop_parsimony_command + " > /dev/null 2>&1"
        os.system(loop_parsimony_command)
