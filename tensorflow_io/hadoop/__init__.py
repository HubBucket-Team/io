# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Sequence File Dataset.

@@SequenceFileDataset
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings

from tensorflow_io.hadoop.python.ops.hadoop_dataset_ops import SequenceFileDataset

from tensorflow.python.util.all_util import remove_undocumented

warnings.warn(
    "SequenceFileDataset is deprecated and will be removed in the next release",
    DeprecationWarning)

_allowed_symbols = [
    "SequenceFileDataset",
]

remove_undocumented(__name__, allowed_exception_list=_allowed_symbols)
