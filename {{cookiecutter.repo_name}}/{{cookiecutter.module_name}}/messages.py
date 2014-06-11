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


class MessageController(storage.Message):

    def list(self, queue, project=None, marker=None,
             limit=10, echo=False, client_uuid=None,
             include_claimed=False):
        """Base method for listing messages.

        :param queue: Name of the queue to get the
            message from.
        :param project: Project id
        :param marker: Tail identifier
        :param limit: (Default 10) Max number of messages to return.
        :type limit: Maybe int
        :param echo: (Default False) Boolean expressing whether
            or not this client should receive its own messages.
        :param client_uuid: A UUID object. Required when echo=False.
        :param include_claimed: omit claimed messages from listing?
        :type include_claimed: bool

        :returns: An iterator giving a sequence of messages and
            the marker of the next page.
        """
        raise NotImplementedError

    def first(self, queue, project=None, sort=1):
        """Get first message in the queue (including claimed).

        :param queue: Name of the queue to list
        :param sort: (Default 1) Sort order for the listing. Pass 1 for
            ascending (oldest message first), or -1 for descending (newest
            message first).

        :returns: First message in the queue, or None if the queue is
            empty
        """
        raise NotImplementedError

    def get(self, queue, message_id, project=None):
        """Base method for getting a message.

        :param queue: Name of the queue to get the
            message from.
        :param project: Project id
        :param message_id: Message ID

        :returns: Dictionary containing message data
        :raises: DoesNotExist
        """
        raise NotImplementedError

    def bulk_get(self, queue, message_ids, project=None):
        """Base method for getting multiple messages.

        :param queue: Name of the queue to get the
            message from.
        :param project: Project id
        :param message_ids: A sequence of message IDs.

        :returns: An iterable, yielding dicts containing
            message details
        """
        raise NotImplementedError

    def post(self, queue, messages, client_uuid, project=None):
        """Base method for posting one or more messages.

        Implementations of this method should guarantee
        and preserve the order, in the returned list, of
        incoming messages.

        :param queue: Name of the queue to post message to.
        :param messages: Messages to post to queue, an iterable
            yielding 1 or more elements. An empty iterable
            results in undefined behavior.
        :param client_uuid: A UUID object.
        :param project: Project id

        :returns: List of message ids
        """
        raise NotImplementedError

    def delete(self, queue, message_id, project=None, claim=None):
        """Base method for deleting a single message.

        :param queue: Name of the queue to post
            message to.
        :param message_id: Message to be deleted
        :param project: Project id
        :param claim: Claim this message
            belongs to. When specified, claim must
            be valid and message_id must belong to
            it.
        """
        raise NotImplementedError

    def bulk_delete(self, queue, message_ids, project=None):
        """Base method for deleting multiple messages.

        :param queue: Name of the queue to post
            message to.
        :param message_ids: A sequence of message IDs
            to be deleted.
        :param project: Project id
        """
        raise NotImplementedError
