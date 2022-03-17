# swagger-client
# FIX Gateway Commander API REST API to get status and to send control commands to FIX Gateway.  Configuration API allows to view and update FIX Gateway session configuration.                       

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of active FIX Gateway Agents
    api_response = api_instance.agents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agents_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AgentApi(swagger_client.ApiClient(configuration))
body = swagger_client.HaltRequest() # HaltRequest |  (optional)

try:
    # Request to halt trading
    api_response = api_instance.halt_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->halt_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AgentApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogoutRequest() # LogoutRequest |  (optional)

try:
    # Request to logout all Agent's sessions
    api_response = api_instance.logout_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->logout_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AgentApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of active Agents sessions
    api_response = api_instance.sessions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->sessions_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AgentApi(swagger_client.ApiClient(configuration))
body = swagger_client.ShortsaleRequest() # ShortsaleRequest |  (optional)

try:
    # Request to prohibit short sale trading
    api_response = api_instance.shortsale_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->shortsale_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8577*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentApi* | [**agents_get**](docs/AgentApi.md#agents_get) | **GET** /agents | Gets a list of active FIX Gateway Agents
*AgentApi* | [**halt_post**](docs/AgentApi.md#halt_post) | **POST** /halt | Request to halt trading
*AgentApi* | [**logout_post**](docs/AgentApi.md#logout_post) | **POST** /logout | Request to logout all Agent&#x27;s sessions
*AgentApi* | [**sessions_get**](docs/AgentApi.md#sessions_get) | **GET** /sessions | Gets a list of active Agents sessions
*AgentApi* | [**shortsale_post**](docs/AgentApi.md#shortsale_post) | **POST** /shortsale | Request to prohibit short sale trading
*ConfigurationApi* | [**config_partitions_get**](docs/ConfigurationApi.md#config_partitions_get) | **GET** /config/partitions | Retrieve FIX Gateway configuration
*ConfigurationApi* | [**config_partitions_post**](docs/ConfigurationApi.md#config_partitions_post) | **POST** /config/partitions | Update FIX Gateway configuration
*DiscoveryApi* | [**discovery_agents_get**](docs/DiscoveryApi.md#discovery_agents_get) | **GET** /discovery/agents | Gets an agents data object
*DiscoveryApi* | [**discovery_sessions_get**](docs/DiscoveryApi.md#discovery_sessions_get) | **GET** /discovery/sessions | Gets sessions data object
*SessionApi* | [**halt_post**](docs/SessionApi.md#halt_post) | **POST** /halt | Request to halt trading
*SessionApi* | [**sessions_get**](docs/SessionApi.md#sessions_get) | **GET** /sessions | Gets a list of active Agents sessions
*SessionApi* | [**shortsale_post**](docs/SessionApi.md#shortsale_post) | **POST** /shortsale | Request to prohibit short sale trading

## Documentation For Models

 - [AgentsResponse](docs/AgentsResponse.md)
 - [AgentsResponseInner](docs/AgentsResponseInner.md)
 - [GateConfiguration](docs/GateConfiguration.md)
 - [GateConfigurationInner](docs/GateConfigurationInner.md)
 - [HaltRequest](docs/HaltRequest.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2002Data](docs/InlineResponse2002Data.md)
 - [InlineResponse200Data](docs/InlineResponse200Data.md)
 - [LogoutRequest](docs/LogoutRequest.md)
 - [SessionsResponse](docs/SessionsResponse.md)
 - [SessionsResponseInner](docs/SessionsResponseInner.md)
 - [ShortsaleRequest](docs/ShortsaleRequest.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

dmtsyganov@devexperts.com
