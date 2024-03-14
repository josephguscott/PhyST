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
import itertools
import linecache

from iqtree import IqtreeEvaluateTreesCommand
from print import Print

from log import LOG

import re

class FilterTrees:
    def __init__(self, MSA_INPUT_PATH, HARDWARE, NUM_MP_TREES) -> None:
        self.MSA_INPUT_PATH = MSA_INPUT_PATH
        self.HARDWARE = HARDWARE
        self.NUM_MP_TREES = NUM_MP_TREES
        self.FilterInitialTrees()

    def FilterInitialTrees(self) -> None:
        evaluate_command = IqtreeEvaluateTreesCommand(self.MSA_INPUT_PATH, self.HARDWARE)
        os.system(evaluate_command)
        best_trees_dict = self.GetBestTreesDictionary()

        best_tree_numbers = dict(itertools.islice(best_trees_dict.items(), self.NUM_MP_TREES))

        LOG.info('Highest scoring likelihood trees:')

        Print.PrintDictionary(best_tree_numbers)

        self.WriteBestInitialTreesFile(best_tree_numbers)

    def GetBestTreesDictionary(self) -> dict:
        file = self.MSA_INPUT_PATH + ".log"
        best_trees_dict = {}
        iqtree_regex = '^(Tree \d+) \/ (LogL:) (-\d*.\d*)$'

        with open(file, "r") as fp:
            for line in fp:
                tree_search = re.search(iqtree_regex, line)
                if tree_search is not None:
                    best_trees_dict[str(tree_search.group(1))] = float(tree_search.group(3))

        best_trees_dict = {k: v for k, v in sorted(best_trees_dict.items(), key=lambda item: item[1], reverse=True)}

        return best_trees_dict

    def WriteBestInitialTreesFile(self, best_trees_number: dict) -> None:
        file = "initial_trees.treefile"
        line_numbers = []
        lines = []
        dict_list = []

        for key in best_trees_number:
            dict_list.append(key[-1])

        for i in range(self.NUM_MP_TREES):
            line_numbers.append(int(dict_list[i]))

        for i in line_numbers:
            x = linecache.getline(file, i).strip()
            lines.append(x)

        with open('initial_trees_best.treefile', 'w') as fp:
            for i in lines:
                fp.write("%s\n" % i)

        for i in range(self.NUM_MP_TREES):
            j = str(i + 1)
            file_name = "initial_trees_best_" + j + ".treefile"

            with open(file_name, 'w') as fp:
                fp.write("%s\n" % lines[i])
