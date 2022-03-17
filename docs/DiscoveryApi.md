# swagger_client.DiscoveryApi

All URIs are relative to *http://localhost:8577*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery_agents_get**](DiscoveryApi.md#discovery_agents_get) | **GET** /discovery/agents | Gets an agents data object
[**discovery_sessions_get**](DiscoveryApi.md#discovery_sessions_get) | **GET** /discovery/sessions | Gets sessions data object

# **discovery_agents_get**
> InlineResponse200 discovery_agents_get()

Gets an agents data object

This request is used in Zabbix discovery. Response object contains names of active FIX Gateway Agents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()

try:
    # Gets an agents data object
    api_response = api_instance.discovery_agents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->discovery_agents_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_sessions_get**
> InlineResponse2002 discovery_sessions_get()

Gets sessions data object

This request is used in Zabbix discovery. Response data object contains FIX Gateway activer session names (FIX sessions) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()

try:
    # Gets sessions data object
    api_response = api_instance.discovery_sessions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->discovery_sessions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

