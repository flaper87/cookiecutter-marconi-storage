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

"""Put something here"""

#from marconi.openstack.common.gettextutils import _
import marconi.openstack.common.log as logging
from marconi.queues import storage
#from marconi.queues.storage import errors


LOG = logging.getLogger(__name__)


class QueueController(storage.Queue):
    """Yet another storage driver."""

    def list(self, project=None, marker=None,
             limit=10, detailed=False):
        """Base method for listing queues.

        :param project: Project id
        :param marker: The last queue name
        :param limit: (Default 10) Max number of queues to return
        :param detailed: Whether metadata is included

        :returns: An iterator giving a sequence of queues
            and the marker of the next page.
        """
        raise NotImplementedError

    def get_metadata(self, name, project=None):
        """Base method for queue metadata retrieval.

        :param name: The queue name
        :param project: Project id

        :returns: Dictionary containing queue metadata
        :raises: DoesNotExist
        """
        raise NotImplementedError

    def create(self, name, project=None):
        """Base method for queue creation.

        :param name: The queue name
        :param project: Project id
        :returns: True if a queue was created and False
            if it was updated.
        """
        raise NotImplementedError

    def exists(self, name, project=None):
        """Base method for testing queue existence.

        :param name: The queue name
        :param project: Project id
        :returns: True if a queue exists and False
            if it does not.
        """
        raise NotImplementedError

    def set_metadata(self, name, metadata, project=None):
        """Base method for updating a queue metadata.

        :param name: The queue name
        :param metadata: Queue metadata as a dict
        :param project: Project id
        :raises: DoesNotExist
        """
        raise NotImplementedError

    def delete(self, name, project=None):
        """Base method for deleting a queue.

        :param name: The queue name
        :param project: Project id
        """
        raise NotImplementedError

    def stats(self, name, project=None):
        """Base method for queue stats.

        :param name: The queue name
        :param project: Project id
        :returns: Dictionary with the
            queue stats
        """
        raise NotImplementedError
