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

from iqtree import IqtreeLikelihoodAnalysis

from log import LOG

def RefineInitialTrees(msa_path: str, cores: int, iqtree_options: str) -> None:
    treefile = msa_path + ".treefile"
    logfile = msa_path + ".log"

    refine_tree_command = IqtreeLikelihoodAnalysis(msa_path, cores, iqtree_options)
    os.system(refine_tree_command)

    with open(logfile, "r") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.startswith("BEST SCORE FOUND : "):
                output = line

    best_score = output.split(": ")

    LOG.info(f'Refined ML tree score: {best_score[-1]}')
    LOG.info(f'Refined ML treefile: {treefile}')