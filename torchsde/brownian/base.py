# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc


class Brownian(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def to(self, *args):
        pass

    @property
    @abc.abstractmethod
    def dtype(self):
        pass

    @property
    @abc.abstractmethod
    def device(self):
        pass

    @property
    @abc.abstractmethod
    def shape(self):
        pass

    @abc.abstractmethod
    def size(self):
        pass
