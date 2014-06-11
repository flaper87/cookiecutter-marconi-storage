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


import marconi.openstack.common.log as logging
from marconi.queues import storage


_OPTIONS = []
_OPTIONS_GROUP = 'drivers:storage:{{ cookiecutter.module_name }}'

LOG = logging.getLogger(__name__)


class DataDriver(storage.DataDriverBase):

    def __init__(self, conf, cache):
        super(Driver, self).__init__(conf, storage)

        self._conf.register_opts(_OPTIONS, group=_OPTIONS_GROUP)
        self._storage_conf = self._conf[_OPTIONS_GROUP]

    def is_alive(self):
        raise NotImplementedError

    @decorators.lazy_property(write=False)
    def connection(self):
        """Store client onnection instance."""
        raise NotImplementedError

    @decorators.lazy_property(write=False)
    def queue_controller(self):
        return controllers.QueueController(self)

    @decorators.lazy_property(write=False)
    def message_controller(self):
        return controllers.MessageController(self)

    @decorators.lazy_property(write=False)
    def claim_controller(self):
        return controllers.ClaimController(self)


class ControlDriver(storage.ControlDriverBase):

    def __init__(self, conf, cache):
        super(ControlDriver, self).__init__(conf, cache)

        self._conf.register_opts(_OPTIONS, group=_OPTIONS_GROUP)
        self._storage_conf = self._conf[_OPTIONS_GROUP]

    @decorators.lazy_property(write=False)
    def connection(self):
        """Store client onnection instance."""
        raise NotImplementedError

    @property
    def shards_controller(self):
        return controllers.ShardsController(self)

    @property
    def catalogue_controller(self):
        return controllers.CatalogueController(self)
