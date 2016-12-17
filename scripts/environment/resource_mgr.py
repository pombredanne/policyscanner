# Copyright 2016 Google Inc.
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
"""Wrapper class for Resource Manager API."""

import sys

try:
    from apiclient import discovery
    from oauth2client.client import GoogleCredentials
except ImportError:
    print ('To use this, please import the google-api-python-client library:'
           '\n\n$ pip install google-api-python-client\n')
    sys.exit(1)


class ResourceManager(object):
    """Resource Manager wrapper around service discovery API."""

    def __init__(self, credentials=None):
        if not credentials:
            credentials = GoogleCredentials.get_application_default()
        self.credentials = credentials
        self._service = discovery.build(serviceName='cloudresourcemanager',
                                        version='v1',
                                        credentials=self.credentials)

    @property
    def service(self):
        """Returns the Resource Manager service."""
        return self._service
