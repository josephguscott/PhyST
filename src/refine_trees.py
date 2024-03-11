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
import re
from iqtree import IqtreeLikelihoodAnalysis

from log import LOG

class RefineTrees:
    def __init__(self, args) -> None:
        self.MSA_INPUT_PATH = args.MSA_INPUT_PATH
        self.HARDWARE = args.HARDWARE
        self.IQ_TREE_OPTIONS = args.IQ_TREE_OPTIONS
        self.RefineInitialTrees()

    def RefineInitialTrees(self) -> None:
        treefile = self.MSA_INPUT_PATH + ".treefile"
        logfile = self.MSA_INPUT_PATH + ".log"
        best_score_regex = '^(BEST SCORE FOUND) (:) (-\d*.\d*)$'

        refine_tree_command = IqtreeLikelihoodAnalysis(self.MSA_INPUT_PATH, self.HARDWARE, self.IQ_TREE_OPTIONS)
        os.system(refine_tree_command)

        with open(logfile, "r") as fp:
            lines = fp.readlines()
            for line in lines:
                tree_search = re.search(best_score_regex, line)
                if tree_search is not None:
                    LOG.info(f'Refined ML tree score: {tree_search.group(3)}')
                    LOG.info(f'Refined ML treefile: {treefile}')
