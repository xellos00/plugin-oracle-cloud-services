import logging

from spaceone.inventory.libs.connector import OCIConnector
from spaceone.inventory.error import *

__all__ = ['DiskConnector']
_LOGGER = logging.getLogger(__name__)


class DiskConnector(OCIConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list_disks(self):
        return self.compute_client.disks.list()

    def get_lock_info(self, subscription):
        return self.resource_client.subscriptions.list(subscription)
