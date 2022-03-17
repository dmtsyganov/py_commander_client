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

class SessionsResponseInner(object):
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
        'session_name': 'str',
        'initiator': 'str',
        'initiator_sub': 'str',
        'acceptor': 'str',
        'acceptor_sub': 'str',
        'time_updated': 'int',
        'last_sent': 'int',
        'last_received': 'int',
        'state': 'str',
        'trading_halted': 'bool',
        'short_sale_prohibited': 'bool'
    }

    attribute_map = {
        'agent_type': 'agentType',
        'name': 'name',
        'session_name': 'sessionName',
        'initiator': 'initiator',
        'initiator_sub': 'initiatorSub',
        'acceptor': 'acceptor',
        'acceptor_sub': 'acceptorSub',
        'time_updated': 'timeUpdated',
        'last_sent': 'lastSent',
        'last_received': 'lastReceived',
        'state': 'state',
        'trading_halted': 'tradingHalted',
        'short_sale_prohibited': 'shortSaleProhibited'
    }

    def __init__(self, agent_type=None, name=None, session_name=None, initiator=None, initiator_sub=None, acceptor=None, acceptor_sub=None, time_updated=None, last_sent=None, last_received=None, state=None, trading_halted=None, short_sale_prohibited=None):  # noqa: E501
        """SessionsResponseInner - a model defined in Swagger"""  # noqa: E501
        self._agent_type = None
        self._name = None
        self._session_name = None
        self._initiator = None
        self._initiator_sub = None
        self._acceptor = None
        self._acceptor_sub = None
        self._time_updated = None
        self._last_sent = None
        self._last_received = None
        self._state = None
        self._trading_halted = None
        self._short_sale_prohibited = None
        self.discriminator = None
        if agent_type is not None:
            self.agent_type = agent_type
        if name is not None:
            self.name = name
        if session_name is not None:
            self.session_name = session_name
        if initiator is not None:
            self.initiator = initiator
        if initiator_sub is not None:
            self.initiator_sub = initiator_sub
        if acceptor is not None:
            self.acceptor = acceptor
        if acceptor_sub is not None:
            self.acceptor_sub = acceptor_sub
        if time_updated is not None:
            self.time_updated = time_updated
        if last_sent is not None:
            self.last_sent = last_sent
        if last_received is not None:
            self.last_received = last_received
        if state is not None:
            self.state = state
        if trading_halted is not None:
            self.trading_halted = trading_halted
        if short_sale_prohibited is not None:
            self.short_sale_prohibited = short_sale_prohibited

    @property
    def agent_type(self):
        """Gets the agent_type of this SessionsResponseInner.  # noqa: E501

        Agent type - SERVER or CLIENT  # noqa: E501

        :return: The agent_type of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this SessionsResponseInner.

        Agent type - SERVER or CLIENT  # noqa: E501

        :param agent_type: The agent_type of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._agent_type = agent_type

    @property
    def name(self):
        """Gets the name of this SessionsResponseInner.  # noqa: E501

        Agent name  # noqa: E501

        :return: The name of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SessionsResponseInner.

        Agent name  # noqa: E501

        :param name: The name of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def session_name(self):
        """Gets the session_name of this SessionsResponseInner.  # noqa: E501

        Mnemonic FIX session name - SenderId:SubId->AcceptorId:SubId  # noqa: E501

        :return: The session_name of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._session_name

    @session_name.setter
    def session_name(self, session_name):
        """Sets the session_name of this SessionsResponseInner.

        Mnemonic FIX session name - SenderId:SubId->AcceptorId:SubId  # noqa: E501

        :param session_name: The session_name of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._session_name = session_name

    @property
    def initiator(self):
        """Gets the initiator of this SessionsResponseInner.  # noqa: E501

        FIX session initiator id  # noqa: E501

        :return: The initiator of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this SessionsResponseInner.

        FIX session initiator id  # noqa: E501

        :param initiator: The initiator of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._initiator = initiator

    @property
    def initiator_sub(self):
        """Gets the initiator_sub of this SessionsResponseInner.  # noqa: E501

        FIX session initiator sub id  # noqa: E501

        :return: The initiator_sub of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._initiator_sub

    @initiator_sub.setter
    def initiator_sub(self, initiator_sub):
        """Sets the initiator_sub of this SessionsResponseInner.

        FIX session initiator sub id  # noqa: E501

        :param initiator_sub: The initiator_sub of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._initiator_sub = initiator_sub

    @property
    def acceptor(self):
        """Gets the acceptor of this SessionsResponseInner.  # noqa: E501

        FIX session acceptor id  # noqa: E501

        :return: The acceptor of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._acceptor

    @acceptor.setter
    def acceptor(self, acceptor):
        """Sets the acceptor of this SessionsResponseInner.

        FIX session acceptor id  # noqa: E501

        :param acceptor: The acceptor of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._acceptor = acceptor

    @property
    def acceptor_sub(self):
        """Gets the acceptor_sub of this SessionsResponseInner.  # noqa: E501

        FIX session acceptor sub id  # noqa: E501

        :return: The acceptor_sub of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._acceptor_sub

    @acceptor_sub.setter
    def acceptor_sub(self, acceptor_sub):
        """Sets the acceptor_sub of this SessionsResponseInner.

        FIX session acceptor sub id  # noqa: E501

        :param acceptor_sub: The acceptor_sub of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._acceptor_sub = acceptor_sub

    @property
    def time_updated(self):
        """Gets the time_updated of this SessionsResponseInner.  # noqa: E501

        Unix time since Session status was updated  # noqa: E501

        :return: The time_updated of this SessionsResponseInner.  # noqa: E501
        :rtype: int
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """Sets the time_updated of this SessionsResponseInner.

        Unix time since Session status was updated  # noqa: E501

        :param time_updated: The time_updated of this SessionsResponseInner.  # noqa: E501
        :type: int
        """

        self._time_updated = time_updated

    @property
    def last_sent(self):
        """Gets the last_sent of this SessionsResponseInner.  # noqa: E501

        FIX session last sent sequence number  # noqa: E501

        :return: The last_sent of this SessionsResponseInner.  # noqa: E501
        :rtype: int
        """
        return self._last_sent

    @last_sent.setter
    def last_sent(self, last_sent):
        """Sets the last_sent of this SessionsResponseInner.

        FIX session last sent sequence number  # noqa: E501

        :param last_sent: The last_sent of this SessionsResponseInner.  # noqa: E501
        :type: int
        """

        self._last_sent = last_sent

    @property
    def last_received(self):
        """Gets the last_received of this SessionsResponseInner.  # noqa: E501

        FIX session last received sequence number  # noqa: E501

        :return: The last_received of this SessionsResponseInner.  # noqa: E501
        :rtype: int
        """
        return self._last_received

    @last_received.setter
    def last_received(self, last_received):
        """Sets the last_received of this SessionsResponseInner.

        FIX session last received sequence number  # noqa: E501

        :param last_received: The last_received of this SessionsResponseInner.  # noqa: E501
        :type: int
        """

        self._last_received = last_received

    @property
    def state(self):
        """Gets the state of this SessionsResponseInner.  # noqa: E501

        FIX session status  # noqa: E501

        :return: The state of this SessionsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SessionsResponseInner.

        FIX session status  # noqa: E501

        :param state: The state of this SessionsResponseInner.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def trading_halted(self):
        """Gets the trading_halted of this SessionsResponseInner.  # noqa: E501

        Session trading status  # noqa: E501

        :return: The trading_halted of this SessionsResponseInner.  # noqa: E501
        :rtype: bool
        """
        return self._trading_halted

    @trading_halted.setter
    def trading_halted(self, trading_halted):
        """Sets the trading_halted of this SessionsResponseInner.

        Session trading status  # noqa: E501

        :param trading_halted: The trading_halted of this SessionsResponseInner.  # noqa: E501
        :type: bool
        """

        self._trading_halted = trading_halted

    @property
    def short_sale_prohibited(self):
        """Gets the short_sale_prohibited of this SessionsResponseInner.  # noqa: E501

        Session short sale status  # noqa: E501

        :return: The short_sale_prohibited of this SessionsResponseInner.  # noqa: E501
        :rtype: bool
        """
        return self._short_sale_prohibited

    @short_sale_prohibited.setter
    def short_sale_prohibited(self, short_sale_prohibited):
        """Sets the short_sale_prohibited of this SessionsResponseInner.

        Session short sale status  # noqa: E501

        :param short_sale_prohibited: The short_sale_prohibited of this SessionsResponseInner.  # noqa: E501
        :type: bool
        """

        self._short_sale_prohibited = short_sale_prohibited

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
        if issubclass(SessionsResponseInner, dict):
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
        if not isinstance(other, SessionsResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other