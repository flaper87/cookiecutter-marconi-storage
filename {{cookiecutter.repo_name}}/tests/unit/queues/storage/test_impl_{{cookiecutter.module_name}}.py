# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
import datetime
import time
import uuid

import mock
from testtools import matchers

from marconi.queues import storage
from marconi.queues.storage import errors
from marconi import tests as testing
from marconi.tests.queues.storage import base

import {{cookiecutter.module_name}}
from {{cookiecutter.module_name}} import controllers


class QueueTests(base.QueueControllerTest):

    driver_class = {{cookiecutter.module_name}}.DataDriver
    config_file = 'wsgi_{{cookiecutter.module_name}}.conf'
    controller_class = controllers.QueueController

    def _purge_databases(self):
        # Do something here

    def _prepare_conf(self):
        # Prepare configs
        #self.config(YOUR_CONFIG_GROUP,
        #            database=uuid.uuid4().hex)


class MessageTests(base.MessageControllerTest):

    driver_class = {{cookiecutter.module_name}}.DataDriver
    config_file = 'wsgi_{{cookiecutter.module_name}}.conf'
    controller_class = controllers.MessageController

    def _purge_databases(self):
        # Do something here

    def _prepare_conf(self):
        # Prepare configs
        #self.config(YOUR_CONFIG_GROUP,
        #            database=uuid.uuid4().hex)


class ClaimTests(base.ClaimControllerTest):

    driver_class = {{cookiecutter.module_name}}.DataDriver
    config_file = 'wsgi_{{cookiecutter.module_name}}.conf'
    controller_class = controllers.ClaimController

    def _purge_databases(self):
        # Do something here

    def _prepare_conf(self):
        # Prepare configs
        #self.config(YOUR_CONFIG_GROUP,
        #            database=uuid.uuid4().hex)
