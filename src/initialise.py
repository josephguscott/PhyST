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

from pathlib import Path
from log import LOG

class InitialisePhyst:
    def __init__(self, Args) -> None:
        self.mp_software = Args.MP_SOFTWARE
        self.ml_software = Args.ML_SOFTWARE
        self._msa_path = Args.MSA_INPUT_PATH
        self.InitialChecks()

    def InitialChecks(self) -> None:
        if Path(self._msa_path).is_file() is False:
            raise Exception(f"Cannot find {self._msa_path}")

        initial_software_path = 'lib/' + self.mp_software
        if Path(initial_software_path).is_file() is False:
            raise Exception(f"Cannot find {self.mp_software} within 'lib/'")
        
        ml_software_path = 'lib/' + self.ml_software
        if Path(ml_software_path).is_file() is False:
            raise Exception(f"Cannot find {self.ml_software} within 'lib/'")