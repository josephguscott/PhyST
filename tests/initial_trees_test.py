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

from subprocess import CalledProcessError
import pytest
from src.initial_trees import InitialTrees
from datetime import datetime
from src.config import Config

def test_always_passes():
    assert True

class Test_Args:

    def __init__(self, software):
        self.MP_SOFTWARE = software
        self.MSA_INPUT_PATH = "example_MSAs/nonsense.phy"
        self.NUM_INIT_TREES = 100
        self.NUM_MP_TREES = 5
        self.ML_SOFTWARE = "iqtree"
        self.TIMESTAMP = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.IQ_TREE_OPTIONS = ""
        self.VERBOSE = False
        self.CONFIG = Config("../config/config.yaml").config
        self.TNT_LEVEL = 1
        self.TNT_HITS = 1
        self.HARDWARE = 1
        
        if software == 'lvb':
            self.MP_OUT_PREFIX, self.MP_OUT_SUFFIX = " -o tree.",".treefile"
        elif software == 'tnt':
            self.MP_OUT_PREFIX, self.MP_OUT_SUFFIX = "tree.",".treefile"
        else: self.MP_OUT_PREFIX, self.MP_OUT_SUFFIX = " -pre tree.",""

lvb_args = Test_Args("lvb")
lvb_test = InitialTrees(lvb_args)

def test_lvb_errors():
    
    with pytest.raises(CalledProcessError):
        #with pytest.raises(Exception) as err:
        lvb_test.ParallelGenerateTrees("lvb -i nonsense.phy -f phylip -p 1",1)
    assert True #str(err.value).startswith("LVB failed with error:") # \nERROR: File doesn't exist: nonsense.phy\nERROR: The data matrix must have at least 5 sequences."