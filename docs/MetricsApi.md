# togai_client.MetricsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **POST** /metrics | Get Togai Metrics


# **get_metrics**
> GetMetricsResponse get_metrics(get_metrics_request=get_metrics_request)

Get Togai Metrics

Togai Metrics API allows you to fetch different metrics from Events, Usage Meters and PricePlans with multiple queryable options. A single request can query up to five metrics.  Single response can contain a maximum of 300 data points. 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_metrics_request import GetMetricsRequest
from togai_client.models.get_metrics_response import GetMetricsResponse
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
    api_instance = togai_client.MetricsApi(api_client)
    get_metrics_request = {"startTime":"2017-07-21T00:00:00Z","endTime":"2017-07-22T00:00:00Z","metricQueries":[{"id":"m1","name":"EVENTS","aggregationPeriod":"DAY","filters":[{"fieldName":"ACCOUNT_ID","fieldValues":["account#1"]},{"fieldName":"CUSTOMER_ID","fieldValues":["customer#1"]},{"fieldName":"EVENT_STATUS","fieldValues":["PROCESSED"]}]},{"id":"m2","name":"USAGE","aggregationPeriod":"MONTH","filters":[{"fieldName":"CUSTOMER_ID","fieldValues":["customer#1"]}]}]} # GetMetricsRequest |  (optional)

    try:
        # Get Togai Metrics
        api_response = api_instance.get_metrics(get_metrics_request=get_metrics_request)
        print("The response of MetricsApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_metrics_request** | [**GetMetricsRequest**](GetMetricsRequest.md)|  | [optional] 

### Return type

[**GetMetricsResponse**](GetMetricsResponse.md)

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
**403** | Credential does not have access to get metrics. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

