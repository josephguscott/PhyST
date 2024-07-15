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
from sys import platform
import subprocess
import random
import time
import re
from multiprocessing.pool import Pool
import time

from filter_trees import FilterTrees
from log import LOG
from mpboot import GenerateMPBootCommand
from lvb import GenerateLVBCommand
from tnt import GenerateTNTCommand
from utils import ReadFile
from utils import ReadRandomLine
from utils import WriteFile
from print import Print

class InitialTrees:
    def __init__(self, args) -> None:
        self.NUM_INIT_TREES = args.NUM_INIT_TREES
        self.HARDWARE = args.HARDWARE
        self.MP_SOFTWARE = args.MP_SOFTWARE
        self.MSA_INPUT_PATH = args.MSA_INPUT_PATH
        self.NUM_INIT_TREES = args.NUM_INIT_TREES
        self.NUM_MP_TREES = args.NUM_MP_TREES
        self.MP_OUT_PREFIX = args.MP_OUT_PREFIX
        self.MP_OUT_SUFFIX = args.MP_OUT_SUFFIX
        self.TNT_LEVEL = args.TNT_LEVEL
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

        mp_start = time.time()

        if self.MP_SOFTWARE == 'lvb':
            parsimony_command = GenerateLVBCommand(self.MP_SOFTWARE, self.MSA_INPUT_PATH)
        elif self.MP_SOFTWARE == 'tnt':
            parsimony_command = GenerateTNTCommand(self.MP_SOFTWARE, self.MSA_INPUT_PATH, self.TNT_LEVEL, self.NUM_INIT_TREES)
        else: parsimony_command = GenerateMPBootCommand(self.MP_SOFTWARE, self.MSA_INPUT_PATH)

        if self.MP_SOFTWARE == 'tnt':
            if platform.startswith(('linux','darwin')):
                parsimony_command += ', < quit_tnt.txt 2>&1'
            else: parsimony_command += '; < quit_tnt.txt 2>&1'
            process = os.popen(parsimony_command)
            if re.search("Error",process.read()):
                raise Exception('\n##########################################\nTNT failed. See tnt.log for error message.\n##########################################\n')
        else: 
            with Pool(processes = self.HARDWARE) as pool:
                items =[(parsimony_command, i) for i in range(self.NUM_INIT_TREES)]
                pool.starmap(self.ParallelGenerateTrees, items)

        mp_end = time.time()
        mp_runtime = mp_end - mp_start
        LOG.info(f"###\nMP elapsed time ({self.MP_SOFTWARE}):")
        Print.PrintRuntime(mp_runtime)
        LOG.info("###")

        for tree_number in range(self.NUM_INIT_TREES):
            command = "cat tree." + str(tree_number) + ".treefile >> parsimony.treefile"
            os.system(command)
            if self.MP_SOFTWARE in ['lvb','tnt']:
                initial_tree = ReadRandomLine(f'tree.{tree_number}.treefile')
            else: initial_tree = ReadFile(f'tree.{tree_number}.treefile')
            initial_trees.append(initial_tree)

        return initial_trees

    def WriteInitialTrees(self, initial_trees: list) -> None:
        already_added = []
        for i in range(len(initial_trees)):
            if not initial_trees[i] in already_added:
                WriteFile("initial_trees.treefile", initial_trees[i])
                already_added.append(initial_trees[i])

    def ParallelGenerateTrees(self, parsimony_command: str, tree_number: int) -> None:
        loop_parsimony_command = parsimony_command + self.MP_OUT_PREFIX + str(tree_number) + self.MP_OUT_SUFFIX
        if self.MP_SOFTWARE == 'lvb':
            random_seed = time.time()%1*100000 + random.randint(1,100000)
            loop_parsimony_command += " -s " + str(random_seed)
        try:
            subprocess.run(loop_parsimony_command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            error_msg = re.findall("ERROR: .*\n",e.stdout.decode())
            message = f"{self.MP_SOFTWARE.upper()} failed with error:\n"
            for msg in error_msg:
                message += msg
            raise Exception(message)
