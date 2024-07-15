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
from src.tnt import TNT_input, GenerateTNTCommand
from src.utils import ReadFile

def test_always_passes():
    assert True

def test_TNT_input():
    result = TNT_input("test.extension")
    assert result == "test.tnt"

def test_GenerateTNTCommand():
    result = GenerateTNTCommand("tnt", "example_MSAs/test.fasta", 1, 2)
    assert os.path.isfile("example_MSAs/test.tnt")
    with open("example_MSAs/test.tnt") as file:
        assert len(file.readlines()) == 23
    assert ReadFile("example_MSAs/test.tnt") == "procedure /;"
    os.remove("example_MSAs/test.tnt")
    assert result == "tnt run TNTsearch.run input example_MSAs/test.tnt level 1 hits 2 treefile "