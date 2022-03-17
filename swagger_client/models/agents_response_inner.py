# coding: utf-8

"""
    FIX Gateway Commander API

    # FIX Gateway Commander API REST API to get status and to send control commands to FIX Gateway.  Configuration API allows to view and update FIX Gateway session configuration.                         # noqa: E501

    OpenAPI spec version: 0.1
    Contact: dmtsyganov@devexperts.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AgentsResponseInner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'agent_type': 'str',
        'name': 'str',
        'time_updated': 'int',
        'sessions_count': 'int',
        'status': 'str'
    }

    attribute_map = {
        'agent_type': 'agentType',
        'name': 'name',
        'time_updated': 'timeUpdated',
        'sessions_count': 'sessionsCount',
        'status': 'status'
    }

    def __init__(self, agent_type=None, name=None, time_updated=None, sessions_count=None, status=None):  # noqa: E501
        """AgentsResponseInner - a model defined in Swagger"""  # noqa: E501
        self._agent_type = None
        self._name = None
        self._time_updated = None
        self._sessions_count = None
        self._status = None
        self.discriminator = None
        if agent_type is not None:
            self.agent_type = agent_type
        if name is not None:
            self.name = name
        if time_updated is not None:
            self.time_updated = time_updated
        if sessions_count is not None:
            self.sessions_count = sessions_count
        if status is not None:
            self.status = status

    @property
    def agent_type(self):
        """Gets the agent_type of this AgentsResponseInner.  # noqa: E501

        Agent type - SERVER or CLIENT  # noqa: E501

        :return: The agent_type of this AgentsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this AgentsResponseInner.

        Agent type - SERVER or CLIENT  # noqa: E501

        :param agent_type: The agent_type of this AgentsResponseInner.  # noqa: E501
        :type: str
        """

        self._agent_type = agent_type

    @property
    def name(self):
        """Gets the name of this AgentsResponseInner.  # noqa: E501

        Agent name  # noqa: E501

        :return: The name of this AgentsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentsResponseInner.

        Agent name  # noqa: E501

        :param name: The name of this AgentsResponseInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def time_updated(self):
        """Gets the time_updated of this AgentsResponseInner.  # noqa: E501

        Unix time since Agent status was updated  # noqa: E501

        :return: The time_updated of this AgentsResponseInner.  # noqa: E501
        :rtype: int
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """Sets the time_updated of this AgentsResponseInner.

        Unix time since Agent status was updated  # noqa: E501

        :param time_updated: The time_updated of this AgentsResponseInner.  # noqa: E501
        :type: int
        """

        self._time_updated = time_updated

    @property
    def sessions_count(self):
        """Gets the sessions_count of this AgentsResponseInner.  # noqa: E501

        Number of active FIX sessions  # noqa: E501

        :return: The sessions_count of this AgentsResponseInner.  # noqa: E501
        :rtype: int
        """
        return self._sessions_count

    @sessions_count.setter
    def sessions_count(self, sessions_count):
        """Sets the sessions_count of this AgentsResponseInner.

        Number of active FIX sessions  # noqa: E501

        :param sessions_count: The sessions_count of this AgentsResponseInner.  # noqa: E501
        :type: int
        """

        self._sessions_count = sessions_count

    @property
    def status(self):
        """Gets the status of this AgentsResponseInner.  # noqa: E501

        Agent status  # noqa: E501

        :return: The status of this AgentsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AgentsResponseInner.

        Agent status  # noqa: E501

        :param status: The status of this AgentsResponseInner.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AgentsResponseInner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgentsResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
