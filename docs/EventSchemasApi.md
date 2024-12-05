# togai_client.EventSchemasApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_event_schema**](EventSchemasApi.md#activate_event_schema) | **POST** /event_schema/{event_schema_name}/activate | Activate an event schema
[**create_event_schema**](EventSchemasApi.md#create_event_schema) | **POST** /event_schema | Create an event schema
[**deactivate_event_schema**](EventSchemasApi.md#deactivate_event_schema) | **POST** /event_schema/{event_schema_name}/deactivate | Deactivate an event schema
[**delete_event_schema**](EventSchemasApi.md#delete_event_schema) | **DELETE** /event_schema/{event_schema_name} | Delete an event schema
[**event_schema_event_schema_name_patch**](EventSchemasApi.md#event_schema_event_schema_name_patch) | **PATCH** /event_schema/{event_schema_name} | Update an event schema
[**get_event_schema**](EventSchemasApi.md#get_event_schema) | **GET** /event_schema/{event_schema_name} | Get an event schema
[**list_event_schema_versions**](EventSchemasApi.md#list_event_schema_versions) | **GET** /event_schema/{event_schema_name}/versions | List all event schema versions
[**list_event_schemas**](EventSchemasApi.md#list_event_schemas) | **GET** /event_schema | List event schemas


# **activate_event_schema**
> EventSchema activate_event_schema(event_schema_name)

Activate an event schema

Activate an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_schema import EventSchema
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
    api_instance = togai_client.EventSchemasApi(api_client)
    event_schema_name = 'rides' # str | 

    try:
        # Activate an event schema
        api_response = api_instance.activate_event_schema(event_schema_name)
        print("The response of EventSchemasApi->activate_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->activate_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  | 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_schema**
> EventSchema create_event_schema(create_event_schema_request)

Create an event schema

Create an event schema with attributes and dimensions to process events.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_event_schema_request import CreateEventSchemaRequest
from togai_client.models.event_schema import EventSchema
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
    api_instance = togai_client.EventSchemasApi(api_client)
    create_event_schema_request = togai_client.CreateEventSchemaRequest() # CreateEventSchemaRequest | Payload to create event schema

    try:
        # Create an event schema
        api_response = api_instance.create_event_schema(create_event_schema_request)
        print("The response of EventSchemasApi->create_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->create_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_schema_request** | [**CreateEventSchemaRequest**](CreateEventSchemaRequest.md)| Payload to create event schema | 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_event_schema**
> EventSchema deactivate_event_schema(event_schema_name)

Deactivate an event schema

You can deactivate an event schema using this API. In case you have an activate usage meter associated with the event schema, you will need to deactivate it first and then try deactivating the event schema. 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_schema import EventSchema
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
    api_instance = togai_client.EventSchemasApi(api_client)
    event_schema_name = 'rides' # str | 

    try:
        # Deactivate an event schema
        api_response = api_instance.deactivate_event_schema(event_schema_name)
        print("The response of EventSchemasApi->deactivate_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->deactivate_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  | 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_schema**
> BaseSuccessResponse delete_event_schema(event_schema_name)

Delete an event schema

To delete(archive) an event schema, you’re required to archive associated active usage meters if any.

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
    api_instance = togai_client.EventSchemasApi(api_client)
    event_schema_name = 'rides' # str | 

    try:
        # Delete an event schema
        api_response = api_instance.delete_event_schema(event_schema_name)
        print("The response of EventSchemasApi->delete_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->delete_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  | 

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

# **event_schema_event_schema_name_patch**
> EventSchema event_schema_event_schema_name_patch(event_schema_name, update_event_schema_request)

Update an event schema

Update an event schema and add new attributes and dimensions  Once an event schema is activated, you cannot update or delete existing attributes and dimensions however you can add new attributes and dimensions and update event schema description.     operationId: updateEventSchema 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_schema import EventSchema
from togai_client.models.update_event_schema_request import UpdateEventSchemaRequest
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
    api_instance = togai_client.EventSchemasApi(api_client)
    event_schema_name = 'rides' # str | 
    update_event_schema_request = togai_client.UpdateEventSchemaRequest() # UpdateEventSchemaRequest | Payload to update event schema

    try:
        # Update an event schema
        api_response = api_instance.event_schema_event_schema_name_patch(event_schema_name, update_event_schema_request)
        print("The response of EventSchemasApi->event_schema_event_schema_name_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->event_schema_event_schema_name_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  | 
 **update_event_schema_request** | [**UpdateEventSchemaRequest**](UpdateEventSchemaRequest.md)| Payload to update event schema | 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_schema**
> EventSchema get_event_schema(event_schema_name, version=version)

Get an event schema

Get an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_schema import EventSchema
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
    api_instance = togai_client.EventSchemasApi(api_client)
    event_schema_name = 'rides' # str | 
    version = 2 # int | Optional version to get a specific version. Gets latest version if it is not provided. (optional)

    try:
        # Get an event schema
        api_response = api_instance.get_event_schema(event_schema_name, version=version)
        print("The response of EventSchemasApi->get_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->get_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  | 
 **version** | **int**| Optional version to get a specific version. Gets latest version if it is not provided. | [optional] 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_schema_versions**
> EventSchemaVersionsResponse list_event_schema_versions(event_schema_name)

List all event schema versions

Get a list of all the versions of an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_schema_versions_response import EventSchemaVersionsResponse
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
    api_instance = togai_client.EventSchemasApi(api_client)
    event_schema_name = 'rides' # str | 

    try:
        # List all event schema versions
        api_response = api_instance.list_event_schema_versions(event_schema_name)
        print("The response of EventSchemasApi->list_event_schema_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->list_event_schema_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  | 

### Return type

[**EventSchemaVersionsResponse**](EventSchemaVersionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list event schema versions request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_schemas**
> EventSchemaListPaginatedResponse list_event_schemas(status=status, next_token=next_token, page_size=page_size)

List event schemas

Returns a list of event schema with pagination.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_schema_list_paginated_response import EventSchemaListPaginatedResponse
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
    api_instance = togai_client.EventSchemasApi(api_client)
    status = 'status_example' # str | Filter by provided status (optional)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List event schemas
        api_response = api_instance.list_event_schemas(status=status, next_token=next_token, page_size=page_size)
        print("The response of EventSchemasApi->list_event_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSchemasApi->list_event_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by provided status | [optional] 
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**EventSchemaListPaginatedResponse**](EventSchemaListPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list events request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

