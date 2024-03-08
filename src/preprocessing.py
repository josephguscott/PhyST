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

from generate_initial_trees import GenerateInitialTrees, WriteInitialTrees
from filter_initial_trees import FilterInitialTrees
from log import LOG

class Preprocessing:
    def __init__(self, args) -> None:
        self.NUM_MP_TREES = args.NUM_MP_TREES
        self.HARDWARE = args.HARDWARE
        self.MP_SOFTWARE = args.MP_SOFTWARE
        self.MSA_INPUT_PATH = args.MSA_INPUT_PATH
        self.GenerateStartingTrees()
        self.FilterStartingTrees()

    def GenerateStartingTrees(self) -> None:
        LOG.info(f'Generating initial {self.NUM_MP_TREES} initial trees using {self.HARDWARE} cores')
        initial_trees = GenerateInitialTrees(self.MP_SOFTWARE, self.MSA_INPUT_PATH, self.NUM_MP_TREES, self.HARDWARE)
        WriteInitialTrees(initial_trees)

    def FilterStartingTrees(self) -> None:
        LOG.info(f'Obtaining the best 5 initial trees')
        FilterInitialTrees(self.MSA_INPUT_PATH, self.HARDWARE)