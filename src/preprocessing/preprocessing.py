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

from preprocessing.generate_initial_trees import GenerateInitialTrees, WriteInitialTrees
from preprocessing.filter_initial_trees import FilterInitialTrees

class Preprocessing:
    def __init__(self, INIT_TREE_SIZE: int, HARDWARE: int, INIT_SOFTWARE: str, MSA_PATH: str) -> None:
        self.INIT_TREE_SIZE = INIT_TREE_SIZE
        self.HARDWARE = HARDWARE
        self.INIT_SOFTWARE = INIT_SOFTWARE
        self.MSA_PATH = MSA_PATH

    def GenerateStartingTrees(self) -> None:
        print("Generating initial {} initial trees using {} cores".format(self.INIT_TREE_SIZE, self.HARDWARE))
        initial_trees = GenerateInitialTrees(self.INIT_SOFTWARE, self.MSA_PATH, self.INIT_TREE_SIZE, self.HARDWARE)
        WriteInitialTrees(initial_trees)

    def FilterStartingTrees(self) -> None:
        print("Obtaining the best {} initial trees".format("5"))
        FilterInitialTrees(self.MSA_PATH, self.HARDWARE)