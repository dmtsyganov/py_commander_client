# swagger_client.ConfigurationApi

All URIs are relative to *http://localhost:8577*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_partitions_get**](ConfigurationApi.md#config_partitions_get) | **GET** /config/partitions | Retrieve FIX Gateway configuration
[**config_partitions_post**](ConfigurationApi.md#config_partitions_post) | **POST** /config/partitions | Update FIX Gateway configuration

# **config_partitions_get**
> GateConfiguration config_partitions_get()

Retrieve FIX Gateway configuration

This API allows users to retrieve FIX Gateway partitions configuration. Partitions configuration is used by CLIENT FIX Gateway agents for outgoing (to Exchange) FIX connections. Partitions configuration may be stored in a property file or in a database. This API retrieves configuration from a database. Please note that following partition names are reserved and should be used in describing partition configuration: * C1 - cash (equity) partition one * C2 - cash (equity) partitoin two * D1 - derivatives partition one * D2 - derivatives partition two  Also, it is recommended that Reference Data partitions starts with \"RD\", For example: RD, RDC, RDD                                    

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Retrieve FIX Gateway configuration
    api_response = api_instance.config_partitions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->config_partitions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GateConfiguration**](GateConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_partitions_post**
> InlineResponse2001 config_partitions_post(body=body)

Update FIX Gateway configuration

This API allows users to update FIX Gateway partitions configuration. Partitions configuration is used by CLIENT FIX Gateway agents for outgoing (to Exchange) FIX connections. This API updates configuration strored in a database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
body = [swagger_client.GateConfigurationInner()] # list[GateConfigurationInner] |  (optional)

try:
    # Update FIX Gateway configuration
    api_response = api_instance.config_partitions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->config_partitions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[GateConfigurationInner]**](GateConfigurationInner.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

