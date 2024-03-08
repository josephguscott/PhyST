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

import time

class Print:
        physt_version = "1.0"

        def __init__(self, Args):
                self.initial_software = Args.MP_SOFTWARE
                self.msa_path = Args.MSA_INPUT_PATH
                self.number_initial_trees = Args.NUM_MP_TREES
                self.refinement_software = Args.ML_SOFTWARE
                self.time_stamp = Args.TIMESTAMP
                self.cores = Args.HARDWARE

        def PrintStartup(self) -> None:
                self.__PrintHeader()
                self.__PrintSoftwareConfig()

        def __PrintHeader(self) -> None:
                print("===============================")
                print("  PHYST Phylogenetic Pipeline  ")
                print("===============================")

                print(f"PHYST ({self.physt_version})")
                print("Developed by Joseph Guscott,")
                print("Barker Lab,")
                print("School of Biological Science")
                print("University of Edinburgh")
                print("Copyright (c) 2023 Joseph Guscott")

        def __PrintSoftwareConfig(self) -> None:
                print("===============================")
                print("PHYST configuration:")
                print("  Initial Trees")
                print("    Software:", self.initial_software)
                print("    MSA:", self.msa_path)
                print("    Trees evaluated:", self.number_initial_trees)
                print("    Trees retained: 5")
                print("")
                print("  Likelihood Analysis")
                print("    Software:", self.refinement_software)
                print("")
                print("  Resources")
                print("    Cores:", self.cores)
                print("")
                print("Start time: ", self.time_stamp)
                print("")
                print("MPBoot provided by Hoang, et al., 2018; https://doi.org/10.1186/s12862-018-1131-3")
                print("IQ-Tree provided by Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015")
                print("===============================")
                print("")

        @staticmethod
        def PrintDictionary(dictionary: dict) -> None:
                for key in dictionary:
                        print (key,':',dictionary[key])

        @staticmethod
        def PrintRuntime(program_runtime) -> None:
                print("\nWall-clock time : ", time.strftime("%H:%M:%S", time.gmtime(program_runtime))) 