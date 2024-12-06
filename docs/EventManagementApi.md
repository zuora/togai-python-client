# togai_client.EventManagementApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_correction**](EventManagementApi.md#event_correction) | **POST** /events/correction | Correct an ingested event
[**get_events**](EventManagementApi.md#get_events) | **GET** /events | Get a list of usage events with multiple query options
[**get_single_event**](EventManagementApi.md#get_single_event) | **GET** /events/{event_id} | Get an event using event id


# **event_correction**
> EventsCorrectionResponse event_correction(action, require_confirmation=require_confirmation, event_correction_request=event_correction_request)

Correct an ingested event

#### This API lets you to correct events. Available in both synchronous and asynchronous mode - **Usages**: Reduction of all usages associated with this event - **Revenue**: Reduction of all revenues associated with this event - **Entitlements**: Entitlements(Feature Credits) consumed by this event are granted back to the account.  ### Possible Actions: - UNDO: Undo all usages, revenue and entitlements associated with an event - REDO: Performs UNDO and re-ingests the same event - REDO_EVENT: Performs UNDO and re-ingests the correction payload of the event 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.event_correction_request import EventCorrectionRequest
from togai_client.models.events_correction_response import EventsCorrectionResponse
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
    api_instance = togai_client.EventManagementApi(api_client)
    action = 'UNDO' # str | Action to perform in event correction
    require_confirmation = false # bool | Specifies whether to start a migration only after a confirmation (optional)
    event_correction_request = togai_client.EventCorrectionRequest() # EventCorrectionRequest |  (optional)

    try:
        # Correct an ingested event
        api_response = api_instance.event_correction(action, require_confirmation=require_confirmation, event_correction_request=event_correction_request)
        print("The response of EventManagementApi->event_correction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagementApi->event_correction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Action to perform in event correction | 
 **require_confirmation** | **bool**| Specifies whether to start a migration only after a confirmation | [optional] 
 **event_correction_request** | [**EventCorrectionRequest**](EventCorrectionRequest.md)|  | [optional] 

### Return type

[**EventsCorrectionResponse**](EventsCorrectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to get events. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> GetEventsResponse get_events(next_token=next_token, status=status, account_id=account_id, schema_name=schema_name, page_size=page_size)

Get a list of usage events with multiple query options

This API let’s you to fetch a list of events with multiple query parameters

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_events_response import GetEventsResponse
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
    api_instance = togai_client.EventManagementApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)
    status = 'PROCESSED' # str | Filter option to filter by status. (optional)
    account_id = '1234' # str | Filter option to filter based on account id. (optional)
    schema_name = 'Rides' # str | Filter option to filter the events based on schema name. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)

    try:
        # Get a list of usage events with multiple query options
        api_response = api_instance.get_events(next_token=next_token, status=status, account_id=account_id, schema_name=schema_name, page_size=page_size)
        print("The response of EventManagementApi->get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagementApi->get_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 
 **status** | **str**| Filter option to filter by status. | [optional] 
 **account_id** | **str**| Filter option to filter based on account id. | [optional] 
 **schema_name** | **str**| Filter option to filter the events based on schema name. | [optional] 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 

### Return type

[**GetEventsResponse**](GetEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to list events. |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_event**
> GetEventResponse get_single_event(event_id)

Get an event using event id

Fetch details of a particular event using the event ID.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_event_response import GetEventResponse
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
    api_instance = togai_client.EventManagementApi(api_client)
    event_id = 'f4a52f2d-b798-4e08-8b24-db0a5a468ba3' # str | 

    try:
        # Get an event using event id
        api_response = api_instance.get_single_event(event_id)
        print("The response of EventManagementApi->get_single_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagementApi->get_single_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**GetEventResponse**](GetEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to get events. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

