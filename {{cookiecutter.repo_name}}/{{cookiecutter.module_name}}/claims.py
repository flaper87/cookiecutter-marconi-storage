# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#from marconi.openstack.common.gettextutils import _
import marconi.openstack.common.log as logging
from marconi.queues import storage
#from marconi.queues.storage import errors


LOG = logging.getLogger(__name__)


class ClaimController(storage.Claim):

    def get(self, queue, claim_id, project=None):
        """Base method for getting a claim.

        :param queue: Name of the queue this
            claim belongs to.
        :param claim_id: The claim id
        :param project: Project id

        :returns: (Claim's metadata, claimed messages)
        :raises: DoesNotExist
        """
        raise NotImplementedError

    def create(self, queue, metadata, project=None, limit=10):
        """Base method for creating a claim.

        :param queue: Name of the queue this
            claim belongs to.
        :param metadata: Claim's parameters
            to be stored.
        :param project: Project id
        :param limit: (Default 10) Max number
            of messages to claim.

        :returns: (Claim ID, claimed messages)
        """
        raise NotImplementedError

    def update(self, queue, claim_id, metadata, project=None):
        """Base method for updating a claim.

        :param queue: Name of the queue this
            claim belongs to.
        :param claim_id: Claim to be updated
        :param metadata: Claim's parameters
            to be updated.
        :param project: Project id
        """
        raise NotImplementedError

    def delete(self, queue, claim_id, project=None):
        """Base method for deleting a claim.

        :param queue: Name of the queue this
            claim belongs to.
        :param claim_id: Claim to be deleted
        :param project: Project id
        """
        raise NotImplementedError

