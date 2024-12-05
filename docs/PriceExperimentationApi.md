# togai_client.PriceExperimentationApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_revenue**](PriceExperimentationApi.md#calculate_revenue) | **POST** /revenue_calculator | (DEPRECATED) Calculate and return the revenue for a existing or new price plan
[**calculate_revenue_v2**](PriceExperimentationApi.md#calculate_revenue_v2) | **POST** /v2/revenue_calculator | Calculate and return the revenue for a existing or new price plan v2


# **calculate_revenue**
> CalculateRevenueResponse calculate_revenue(calculate_revenue_request)

(DEPRECATED) Calculate and return the revenue for a existing or new price plan

Calculate and return the revenue for a existing or new price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.calculate_revenue_request import CalculateRevenueRequest
from togai_client.models.calculate_revenue_response import CalculateRevenueResponse
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
    api_instance = togai_client.PriceExperimentationApi(api_client)
    calculate_revenue_request = togai_client.CalculateRevenueRequest() # CalculateRevenueRequest | Request payload for calculateRevenueAPI

    try:
        # (DEPRECATED) Calculate and return the revenue for a existing or new price plan
        api_response = api_instance.calculate_revenue(calculate_revenue_request)
        print("The response of PriceExperimentationApi->calculate_revenue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceExperimentationApi->calculate_revenue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculate_revenue_request** | [**CalculateRevenueRequest**](CalculateRevenueRequest.md)| Request payload for calculateRevenueAPI | 

### Return type

[**CalculateRevenueResponse**](CalculateRevenueResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response payload for calculateRevenueAPI |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_revenue_v2**
> CalculateRevenueResponseV2 calculate_revenue_v2(calculate_revenue_request)

Calculate and return the revenue for a existing or new price plan v2

Calculate and return the revenue for a existing or new price plan v2

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.calculate_revenue_request import CalculateRevenueRequest
from togai_client.models.calculate_revenue_response_v2 import CalculateRevenueResponseV2
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
    api_instance = togai_client.PriceExperimentationApi(api_client)
    calculate_revenue_request = togai_client.CalculateRevenueRequest() # CalculateRevenueRequest | Request payload for calculateRevenueAPI

    try:
        # Calculate and return the revenue for a existing or new price plan v2
        api_response = api_instance.calculate_revenue_v2(calculate_revenue_request)
        print("The response of PriceExperimentationApi->calculate_revenue_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceExperimentationApi->calculate_revenue_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculate_revenue_request** | [**CalculateRevenueRequest**](CalculateRevenueRequest.md)| Request payload for calculateRevenueAPI | 

### Return type

[**CalculateRevenueResponseV2**](CalculateRevenueResponseV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response payload for calculateRevenueAPI |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

