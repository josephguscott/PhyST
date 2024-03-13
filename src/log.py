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

import logging
import sys

LOGGER_NAME = "PHYST"
LOG = logging.getLogger(LOGGER_NAME)

class Log:
    logger = None
    stream_handler = None

    def __init__(self) -> None:
        if Log.logger is not None:
            return

        formatter = logging.Formatter(
            fmt='%(message)s',
            datefmt='%H:%M:%S')
        Log.stream_handler = logging.StreamHandler(sys.stdout)
        Log.stream_handler.setFormatter(formatter)
        Log.logger = logging.getLogger(LOGGER_NAME)
        Log.logger.addHandler(self.stream_handler)
        Log.logger.setLevel(logging.DEBUG)

        logging.basicConfig(
            filename='physt.log',
            filemode='w',
            level=logging.DEBUG,
            format='%(message)s',
            datefmt='%H:%M:%S'
        )
