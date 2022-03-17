# swagger_client.AgentApi

All URIs are relative to *http://localhost:8577*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agents_get**](AgentApi.md#agents_get) | **GET** /agents | Gets a list of active FIX Gateway Agents
[**halt_post**](AgentApi.md#halt_post) | **POST** /halt | Request to halt trading
[**logout_post**](AgentApi.md#logout_post) | **POST** /logout | Request to logout all Agent&#x27;s sessions
[**sessions_get**](AgentApi.md#sessions_get) | **GET** /sessions | Gets a list of active Agents sessions
[**shortsale_post**](AgentApi.md#shortsale_post) | **POST** /shortsale | Request to prohibit short sale trading

# **agents_get**
> AgentsResponse agents_get()

Gets a list of active FIX Gateway Agents

In FIX Gateway, agents are responsible for maintaining FIX sessions and processing FIX messages.   There are two type of agents: * **ClientAgent** - responsible for initiating and maintaining outgoing connection to BIST * **ServerAgent** - responsible for accepting and maintaining incoming connections from Gate clients

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentApi()

try:
    # Gets a list of active FIX Gateway Agents
    api_response = api_instance.agents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agents_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AgentsResponse**](AgentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **halt_post**
> InlineResponse2001 halt_post(body=body)

Request to halt trading

This request is used to halt or resume trading on agent's session. This request is applicable only to agent's sessions with agent type SERVER. Posting this request to agent's with agent type CLIENT will have no effect. Gateway client session is identified by initiator id. \"halt\" parametere - \"true\" or \"false\" - is used to halt or resume trading.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentApi()
body = swagger_client.HaltRequest() # HaltRequest |  (optional)

try:
    # Request to halt trading
    api_response = api_instance.halt_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->halt_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HaltRequest**](HaltRequest.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_post**
> InlineResponse2001 logout_post(body=body)

Request to logout all Agent's sessions

This request is used to instruct an agent to logout all active sessions. In case of CLIENT agent type, Gateway will logout FIX session to an Exchange. In Case of SERVER agent type - all Gateway clients FIX sessions will be logged out.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentApi()
body = swagger_client.LogoutRequest() # LogoutRequest |  (optional)

try:
    # Request to logout all Agent's sessions
    api_response = api_instance.logout_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->logout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogoutRequest**](LogoutRequest.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get**
> SessionsResponse sessions_get()

Gets a list of active Agents sessions

Each FIX Gateway Agent may have 0 or few active sessions, which corresponds to FIX connections.   Client agent normally has one outgoing session - from FIX Gateway to an Exchange.   Server agent may have several active sessions - from FIX Gateway clients

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentApi()

try:
    # Gets a list of active Agents sessions
    api_response = api_instance.sessions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->sessions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionsResponse**](SessionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shortsale_post**
> InlineResponse2001 shortsale_post(body=body)

Request to prohibit short sale trading

This request is used to prohibit or allow short sale trading on agent's session. This request is applicable only to agent's sessions with agent type SERVER. Posting this request to agent's with agent type CLIENT will have no effect. Gateway client session is identified by initiator id. \"prohibit\" parametere - \"true\" or \"false\" - is used to prohibit or allow short sale trading.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentApi()
body = swagger_client.ShortsaleRequest() # ShortsaleRequest |  (optional)

try:
    # Request to prohibit short sale trading
    api_response = api_instance.shortsale_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->shortsale_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShortsaleRequest**](ShortsaleRequest.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

