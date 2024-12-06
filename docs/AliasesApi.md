# togai_client.AliasesApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alias**](AliasesApi.md#create_alias) | **POST** /aliases | Create an alias
[**delete_alias**](AliasesApi.md#delete_alias) | **DELETE** /aliases/{alias} | Delete an alias
[**get_alias**](AliasesApi.md#get_alias) | **GET** /aliases/{alias} | Get an alias
[**list_aliases**](AliasesApi.md#list_aliases) | **GET** /aliases | List all aliases


# **create_alias**
> AliasPaginatedResponse create_alias(create_bulk_alias_request)

Create an alias

This API let’s you to create an alias

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alias_paginated_response import AliasPaginatedResponse
from togai_client.models.create_bulk_alias_request import CreateBulkAliasRequest
from togai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togai_client.AliasesApi(api_client)
    create_bulk_alias_request = togai_client.CreateBulkAliasRequest() # CreateBulkAliasRequest | Payload to create bulk aliases

    try:
        # Create an alias
        api_response = api_instance.create_alias(create_bulk_alias_request)
        print("The response of AliasesApi->create_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->create_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bulk_alias_request** | [**CreateBulkAliasRequest**](CreateBulkAliasRequest.md)| Payload to create bulk aliases | 

### Return type

[**AliasPaginatedResponse**](AliasPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for list aliases request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alias**
> BaseSuccessResponse delete_alias(alias)

Delete an alias

This API let’s you to delete an alias using alias.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togai_client.AliasesApi(api_client)
    alias = 'custom_value' # str | 

    try:
        # Delete an alias
        api_response = api_instance.delete_alias(alias)
        print("The response of AliasesApi->delete_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->delete_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**|  | 

### Return type

[**BaseSuccessResponse**](BaseSuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alias**
> Alias get_alias(alias)

Get an alias

Get alias information using alias.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alias import Alias
from togai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togai_client.AliasesApi(api_client)
    alias = 'custom_value' # str | 

    try:
        # Get an alias
        api_response = api_instance.get_alias(alias)
        print("The response of AliasesApi->get_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->get_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**|  | 

### Return type

[**Alias**](Alias.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for adding or removing aliases |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aliases**
> AliasPaginatedResponse list_aliases(next_token=next_token, page_size=page_size)

List all aliases

Returns a list of aliases with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alias_paginated_response import AliasPaginatedResponse
from togai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togai_client.AliasesApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List all aliases
        api_response = api_instance.list_aliases(next_token=next_token, page_size=page_size)
        print("The response of AliasesApi->list_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->list_aliases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**AliasPaginatedResponse**](AliasPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list aliases request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

