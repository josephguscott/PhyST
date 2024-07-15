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
from src.utils import ReadFile, WriteFile, ReadRandomLine, DetectFileFormat

def test_always_passes():
    assert True

def test_ReadFile():
    result = ReadFile("example_MSAs/test.fasta")
    assert result == "CACCAGGTCACTGCGTAACAGACCT"

def test_WriteFile():
    contents = ["This ","is ","a ","test."]
    WriteFile("write_test.txt",contents)
    with open("write_test.txt") as write_test:
        result = ""
        for line in write_test:
            result += line
    os.remove("write_test.txt")
    assert result == "This is a test."

def test_ReadRandomLine():
    results = []
    for i in range(5):
        results.append(ReadRandomLine("example_MSAs/test.fasta"))
    with open("example_MSAs/test.fasta") as file:
        expected = [line for line in file]
        for line in results:
            assert line in expected
    assert len(set(results)) > 1 #checks all 5 lines aren't the same (will very occasionally fail even when line selection is random)

def test_DetectFileFormat():
    results = []
    for file in ["test.fa", "test.nex", "test.aln", "test.ph", "test.txt"]:
        results.append(DetectFileFormat(file))
    assert results == ["fasta", "nexus", "clustal", "phylip", "phylip"]