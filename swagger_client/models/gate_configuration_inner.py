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

class GateConfigurationInner(object):
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
        'application_name': 'str',
        'partitions': 'list[object]'
    }

    attribute_map = {
        'application_name': 'applicationName',
        'partitions': 'partitions'
    }

    def __init__(self, application_name=None, partitions=None):  # noqa: E501
        """GateConfigurationInner - a model defined in Swagger"""  # noqa: E501
        self._application_name = None
        self._partitions = None
        self.discriminator = None
        if application_name is not None:
            self.application_name = application_name
        if partitions is not None:
            self.partitions = partitions

    @property
    def application_name(self):
        """Gets the application_name of this GateConfigurationInner.  # noqa: E501

        FIX Gateway application name  # noqa: E501

        :return: The application_name of this GateConfigurationInner.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this GateConfigurationInner.

        FIX Gateway application name  # noqa: E501

        :param application_name: The application_name of this GateConfigurationInner.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def partitions(self):
        """Gets the partitions of this GateConfigurationInner.  # noqa: E501


        :return: The partitions of this GateConfigurationInner.  # noqa: E501
        :rtype: list[object]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this GateConfigurationInner.


        :param partitions: The partitions of this GateConfigurationInner.  # noqa: E501
        :type: list[object]
        """

        self._partitions = partitions

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
        if issubclass(GateConfigurationInner, dict):
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
        if not isinstance(other, GateConfigurationInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other