# togai_client.UsageMetersApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_usage_meter**](UsageMetersApi.md#activate_usage_meter) | **POST** /usage_meters/{usage_meter_id}/activate | Activate usage meter
[**create_usage_meter**](UsageMetersApi.md#create_usage_meter) | **POST** /usage_meters | Create an usage meter
[**deactivate_usage_meter**](UsageMetersApi.md#deactivate_usage_meter) | **POST** /usage_meters/{usage_meter_id}/deactivate | Deactivate usage meter
[**delete_usage_meter**](UsageMetersApi.md#delete_usage_meter) | **DELETE** /usage_meters/{usage_meter_id} | Delete an Usage Meter
[**get_usage_meter**](UsageMetersApi.md#get_usage_meter) | **GET** /usage_meters/{usage_meter_id} | Get usage meter
[**get_usage_meters_for_event_schema**](UsageMetersApi.md#get_usage_meters_for_event_schema) | **GET** /usage_meters | List usage meters for event schema
[**update_usage_meter**](UsageMetersApi.md#update_usage_meter) | **PATCH** /usage_meters/{usage_meter_id} | Update an usage meter


# **activate_usage_meter**
> UsageMeter activate_usage_meter(usage_meter_id)

Activate usage meter

Activate usage meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.usage_meter import UsageMeter
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
    api_instance = togai_client.UsageMetersApi(api_client)
    usage_meter_id = 'um.1zYnCiM9Bpg.1zYn' # str | 

    try:
        # Activate usage meter
        api_response = api_instance.activate_usage_meter(usage_meter_id)
        print("The response of UsageMetersApi->activate_usage_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->activate_usage_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_meter_id** | **str**|  | 

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_usage_meter**
> UsageMeter create_usage_meter(create_usage_meter_request)

Create an usage meter

Create an usage meter and associate with an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_usage_meter_request import CreateUsageMeterRequest
from togai_client.models.usage_meter import UsageMeter
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
    api_instance = togai_client.UsageMetersApi(api_client)
    create_usage_meter_request = togai_client.CreateUsageMeterRequest() # CreateUsageMeterRequest | Payload to create usage meter

    try:
        # Create an usage meter
        api_response = api_instance.create_usage_meter(create_usage_meter_request)
        print("The response of UsageMetersApi->create_usage_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->create_usage_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_usage_meter_request** | [**CreateUsageMeterRequest**](CreateUsageMeterRequest.md)| Payload to create usage meter | 

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_usage_meter**
> UsageMeter deactivate_usage_meter(usage_meter_id)

Deactivate usage meter

Make an existing active usage meter to be inactive Active Usage Meters with active Pricing Plan attached can also be deactivated. 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.usage_meter import UsageMeter
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
    api_instance = togai_client.UsageMetersApi(api_client)
    usage_meter_id = 'um.1zYnCiM9Bpg.1zYn' # str | 

    try:
        # Deactivate usage meter
        api_response = api_instance.deactivate_usage_meter(usage_meter_id)
        print("The response of UsageMetersApi->deactivate_usage_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->deactivate_usage_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_meter_id** | **str**|  | 

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage_meter**
> BaseSuccessResponse delete_usage_meter(usage_meter_id)

Delete an Usage Meter

Delete an Usage Meter

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
    api_instance = togai_client.UsageMetersApi(api_client)
    usage_meter_id = 'um.1zYnCiM9Bpg.1zYn' # str | 

    try:
        # Delete an Usage Meter
        api_response = api_instance.delete_usage_meter(usage_meter_id)
        print("The response of UsageMetersApi->delete_usage_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->delete_usage_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_meter_id** | **str**|  | 

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
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_meter**
> UsageMeter get_usage_meter(usage_meter_id, include_schema=include_schema)

Get usage meter

Get an usage meter using event schema name and usage meter id.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.usage_meter import UsageMeter
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
    api_instance = togai_client.UsageMetersApi(api_client)
    usage_meter_id = 'um.1zYnCiM9Bpg.1zYn' # str | 
    include_schema = true # bool |  (optional)

    try:
        # Get usage meter
        api_response = api_instance.get_usage_meter(usage_meter_id, include_schema=include_schema)
        print("The response of UsageMetersApi->get_usage_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->get_usage_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_meter_id** | **str**|  | 
 **include_schema** | **bool**|  | [optional] 

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_meters_for_event_schema**
> UsageMeterPaginatedResponse get_usage_meters_for_event_schema(status=status, aggregations=aggregations, next_token=next_token, page_size=page_size)

List usage meters for event schema

Get a list of usage meters associated with an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.usage_meter_paginated_response import UsageMeterPaginatedResponse
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
    api_instance = togai_client.UsageMetersApi(api_client)
    status = 'status_example' # str | Filter by status  (optional)
    aggregations = 'aggregations_example' # str | Filter by aggregations  (optional)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List usage meters for event schema
        api_response = api_instance.get_usage_meters_for_event_schema(status=status, aggregations=aggregations, next_token=next_token, page_size=page_size)
        print("The response of UsageMetersApi->get_usage_meters_for_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->get_usage_meters_for_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by status  | [optional] 
 **aggregations** | **str**| Filter by aggregations  | [optional] 
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**UsageMeterPaginatedResponse**](UsageMeterPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list usage_meters request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_meter**
> UsageMeter update_usage_meter(usage_meter_id, update_usage_meter_request)

Update an usage meter

This API lets you update an existing usage meter.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.update_usage_meter_request import UpdateUsageMeterRequest
from togai_client.models.usage_meter import UsageMeter
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
    api_instance = togai_client.UsageMetersApi(api_client)
    usage_meter_id = 'um.1zYnCiM9Bpg.1zYn' # str | 
    update_usage_meter_request = togai_client.UpdateUsageMeterRequest() # UpdateUsageMeterRequest | Payload to create usage meter

    try:
        # Update an usage meter
        api_response = api_instance.update_usage_meter(usage_meter_id, update_usage_meter_request)
        print("The response of UsageMetersApi->update_usage_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageMetersApi->update_usage_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_meter_id** | **str**|  | 
 **update_usage_meter_request** | [**UpdateUsageMeterRequest**](UpdateUsageMeterRequest.md)| Payload to create usage meter | 

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

