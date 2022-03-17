# coding: utf-8

"""
    FIX Gateway Commander API

    # FIX Gateway Commander API REST API to get status and to send control commands to FIX Gateway.  Configuration API allows to view and update FIX Gateway session configuration.                         # noqa: E501

    OpenAPI spec version: 0.1
    Contact: dmtsyganov@devexperts.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AgentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def agents_get(self, **kwargs):  # noqa: E501
        """Gets a list of active FIX Gateway Agents  # noqa: E501

        In FIX Gateway, agents are responsible for maintaining FIX sessions and processing FIX messages.   There are two type of agents: * **ClientAgent** - responsible for initiating and maintaining outgoing connection to BIST * **ServerAgent** - responsible for accepting and maintaining incoming connections from Gate clients  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agents_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AgentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agents_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.agents_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def agents_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of active FIX Gateway Agents  # noqa: E501

        In FIX Gateway, agents are responsible for maintaining FIX sessions and processing FIX messages.   There are two type of agents: * **ClientAgent** - responsible for initiating and maintaining outgoing connection to BIST * **ServerAgent** - responsible for accepting and maintaining incoming connections from Gate clients  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agents_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AgentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agents_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/agents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AgentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def halt_post(self, **kwargs):  # noqa: E501
        """Request to halt trading  # noqa: E501

        This request is used to halt or resume trading on agent's session. This request is applicable only to agent's sessions with agent type SERVER. Posting this request to agent's with agent type CLIENT will have no effect. Gateway client session is identified by initiator id. \"halt\" parametere - \"true\" or \"false\" - is used to halt or resume trading.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.halt_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HaltRequest body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.halt_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.halt_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def halt_post_with_http_info(self, **kwargs):  # noqa: E501
        """Request to halt trading  # noqa: E501

        This request is used to halt or resume trading on agent's session. This request is applicable only to agent's sessions with agent type SERVER. Posting this request to agent's with agent type CLIENT will have no effect. Gateway client session is identified by initiator id. \"halt\" parametere - \"true\" or \"false\" - is used to halt or resume trading.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.halt_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HaltRequest body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method halt_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/halt', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout_post(self, **kwargs):  # noqa: E501
        """Request to logout all Agent's sessions  # noqa: E501

        This request is used to instruct an agent to logout all active sessions. In case of CLIENT agent type, Gateway will logout FIX session to an Exchange. In Case of SERVER agent type - all Gateway clients FIX sessions will be logged out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LogoutRequest body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.logout_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def logout_post_with_http_info(self, **kwargs):  # noqa: E501
        """Request to logout all Agent's sessions  # noqa: E501

        This request is used to instruct an agent to logout all active sessions. In case of CLIENT agent type, Gateway will logout FIX session to an Exchange. In Case of SERVER agent type - all Gateway clients FIX sessions will be logged out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LogoutRequest body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sessions_get(self, **kwargs):  # noqa: E501
        """Gets a list of active Agents sessions  # noqa: E501

        Each FIX Gateway Agent may have 0 or few active sessions, which corresponds to FIX connections.   Client agent normally has one outgoing session - from FIX Gateway to an Exchange.   Server agent may have several active sessions - from FIX Gateway clients  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sessions_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SessionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sessions_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sessions_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def sessions_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of active Agents sessions  # noqa: E501

        Each FIX Gateway Agent may have 0 or few active sessions, which corresponds to FIX connections.   Client agent normally has one outgoing session - from FIX Gateway to an Exchange.   Server agent may have several active sessions - from FIX Gateway clients  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sessions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SessionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sessions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SessionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def shortsale_post(self, **kwargs):  # noqa: E501
        """Request to prohibit short sale trading  # noqa: E501

        This request is used to prohibit or allow short sale trading on agent's session. This request is applicable only to agent's sessions with agent type SERVER. Posting this request to agent's with agent type CLIENT will have no effect. Gateway client session is identified by initiator id. \"prohibit\" parametere - \"true\" or \"false\" - is used to prohibit or allow short sale trading.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shortsale_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShortsaleRequest body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.shortsale_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.shortsale_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def shortsale_post_with_http_info(self, **kwargs):  # noqa: E501
        """Request to prohibit short sale trading  # noqa: E501

        This request is used to prohibit or allow short sale trading on agent's session. This request is applicable only to agent's sessions with agent type SERVER. Posting this request to agent's with agent type CLIENT will have no effect. Gateway client session is identified by initiator id. \"prohibit\" parametere - \"true\" or \"false\" - is used to prohibit or allow short sale trading.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shortsale_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShortsaleRequest body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shortsale_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/shortsale', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)