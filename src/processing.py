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

from refine_trees import RefineInitialTrees

class Processing:
    def __init__(self, HARDWARE: str, MSA_INPUT_PATH: str, IQ_TREE_OPTIONS) -> None:
        self.HARDWARE = HARDWARE
        self.MSA_INPUT_PATH = MSA_INPUT_PATH
        self.IQ_TREE_OPTIONS = IQ_TREE_OPTIONS

    def RefineStartingTrees(self) -> None:
        RefineInitialTrees(self.MSA_INPUT_PATH, self.HARDWARE, self.IQ_TREE_OPTIONS)