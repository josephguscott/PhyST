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

class Preprocessing:
    def __init__(self, NUM_MP_TREES: int, HARDWARE: int, MP_SOFTWARE: str, MSA_INPUT_PATH: str) -> None:
        self.NUM_MP_TREES = NUM_MP_TREES
        self.HARDWARE = HARDWARE
        self.MP_SOFTWARE = MP_SOFTWARE
        self.MSA_INPUT_PATH = MSA_INPUT_PATH

    def GenerateStartingTrees(self) -> None:
        print("Generating initial {} initial trees using {} cores".format(self.NUM_MP_TREES, self.HARDWARE))
        initial_trees = GenerateInitialTrees(self.MP_SOFTWARE, self.MSA_INPUT_PATH, self.NUM_MP_TREES, self.HARDWARE)
        WriteInitialTrees(initial_trees)

    def FilterStartingTrees(self) -> None:
        print("Obtaining the best {} initial trees".format("5"))
        FilterInitialTrees(self.MSA_INPUT_PATH, self.HARDWARE)