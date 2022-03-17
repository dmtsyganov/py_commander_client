# swagger_client.SessionApi

All URIs are relative to *http://localhost:8577*

Method | HTTP request | Description
------------- | ------------- | -------------
[**halt_post**](SessionApi.md#halt_post) | **POST** /halt | Request to halt trading
[**sessions_get**](SessionApi.md#sessions_get) | **GET** /sessions | Gets a list of active Agents sessions
[**shortsale_post**](SessionApi.md#shortsale_post) | **POST** /shortsale | Request to prohibit short sale trading

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
api_instance = swagger_client.SessionApi()
body = swagger_client.HaltRequest() # HaltRequest |  (optional)

try:
    # Request to halt trading
    api_response = api_instance.halt_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->halt_post: %s\n" % e)
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
api_instance = swagger_client.SessionApi()

try:
    # Gets a list of active Agents sessions
    api_response = api_instance.sessions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->sessions_get: %s\n" % e)
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
api_instance = swagger_client.SessionApi()
body = swagger_client.ShortsaleRequest() # ShortsaleRequest |  (optional)

try:
    # Request to prohibit short sale trading
    api_response = api_instance.shortsale_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->shortsale_post: %s\n" % e)
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

