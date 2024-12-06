# togai_client.EventIngestionApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest**](EventIngestionApi.md#ingest) | **POST** /ingest | Ingest events to Togai
[**ingest_batch**](EventIngestionApi.md#ingest_batch) | **POST** /ingestBatch | Ingest events to Togai in batch


# **ingest**
> IngestEventResponse ingest(ingest_event_request)

Ingest events to Togai

This API let’s you to ingest events to your Togai account. Events ingested using this API will be processed via associated usage meters and further via associated price plans to generate final billable value to invoice the customer Read more about [Event Ingestion](https://docs.togai.com/docs/event-ingestion) 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.ingest_event_request import IngestEventRequest
from togai_client.models.ingest_event_response import IngestEventResponse
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
    api_instance = togai_client.EventIngestionApi(api_client)
    ingest_event_request = togai_client.IngestEventRequest() # IngestEventRequest | Request body to ingest events to Togai usage and billing management service.

    try:
        # Ingest events to Togai
        api_response = api_instance.ingest(ingest_event_request)
        print("The response of EventIngestionApi->ingest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventIngestionApi->ingest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_event_request** | [**IngestEventRequest**](IngestEventRequest.md)| Request body to ingest events to Togai usage and billing management service. | 

### Return type

[**IngestEventResponse**](IngestEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully accepted to process all the events from payload. |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential \&quot;x-api-key\&quot; is not valid. Please check the response message for failure details. |  -  |
**422** | Unable to process the events as the size of the event payload is above the supported limit. Please check our docs for the api limits - https://togai.com/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**503** | Service is currently unavailable to process the request. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_batch**
> IngestEventResponse ingest_batch(ingest_batch_event_request)

Ingest events to Togai in batch

This API let’s you to ingest events in batch upto 500 events. Ingest large amounts of events up to 500 in batches in an array using this API.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.ingest_batch_event_request import IngestBatchEventRequest
from togai_client.models.ingest_event_response import IngestEventResponse
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
    api_instance = togai_client.EventIngestionApi(api_client)
    ingest_batch_event_request = togai_client.IngestBatchEventRequest() # IngestBatchEventRequest | Request body to ingest events in batch to Togai usage and billing management service.

    try:
        # Ingest events to Togai in batch
        api_response = api_instance.ingest_batch(ingest_batch_event_request)
        print("The response of EventIngestionApi->ingest_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventIngestionApi->ingest_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_batch_event_request** | [**IngestBatchEventRequest**](IngestBatchEventRequest.md)| Request body to ingest events in batch to Togai usage and billing management service. | 

### Return type

[**IngestEventResponse**](IngestEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully accepted to process all the events from payload. |  -  |
**207** | Partial failure. Few events from request were not accepted |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential \&quot;x-api-key\&quot; is not valid. Please check the response message for failure details. |  -  |
**422** | Unable to process the events as the size of the event payload is above the supported limit. Please check our docs for the api limits - https://togai.com/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**503** | Service is currently unavailable to process the request. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

