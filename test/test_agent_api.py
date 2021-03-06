# coding: utf-8

"""
    FIX Gateway Commander API

    # FIX Gateway Commander API REST API to get status and to send control commands to FIX Gateway.  Configuration API allows to view and update FIX Gateway session configuration.                         # noqa: E501

    OpenAPI spec version: 0.1
    Contact: dmtsyganov@devexperts.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.agent_api import AgentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAgentApi(unittest.TestCase):
    """AgentApi unit test stubs"""

    def setUp(self):
        self.api = AgentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_agents_get(self):
        """Test case for agents_get

        Gets a list of active FIX Gateway Agents  # noqa: E501
        """
        pass

    def test_halt_post(self):
        """Test case for halt_post

        Request to halt trading  # noqa: E501
        """
        pass

    def test_logout_post(self):
        """Test case for logout_post

        Request to logout all Agent's sessions  # noqa: E501
        """
        pass

    def test_sessions_get(self):
        """Test case for sessions_get

        Gets a list of active Agents sessions  # noqa: E501
        """
        pass

    def test_shortsale_post(self):
        """Test case for shortsale_post

        Request to prohibit short sale trading  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
