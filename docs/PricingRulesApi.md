# togai_client.PricingRulesApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_pricing_rules_by_schedule_id**](PricingRulesApi.md#list_pricing_rules_by_schedule_id) | **GET** /price_plans/{price_plan_id}/pricing_schedules/{pricing_schedule_id}/pricing_rules | (DEPRECATED) List pricing rules by price plan id and pricing schedule id


# **list_pricing_rules_by_schedule_id**
> PricingRulesPaginatedResponse list_pricing_rules_by_schedule_id(price_plan_id, pricing_schedule_id, invoice_timing=invoice_timing)

(DEPRECATED) List pricing rules by price plan id and pricing schedule id

Get a list of pricing rules using price plan id and pricing schedule id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.pricing_rules_paginated_response import PricingRulesPaginatedResponse
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
    api_instance = togai_client.PricingRulesApi(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    pricing_schedule_id = 'sch.1zYnCiM9Bpg.lv25y' # str | 
    invoice_timing = 'invoice_timing_example' # str | Optional field to filter pricing rules based on invoice timing (optional)

    try:
        # (DEPRECATED) List pricing rules by price plan id and pricing schedule id
        api_response = api_instance.list_pricing_rules_by_schedule_id(price_plan_id, pricing_schedule_id, invoice_timing=invoice_timing)
        print("The response of PricingRulesApi->list_pricing_rules_by_schedule_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingRulesApi->list_pricing_rules_by_schedule_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **pricing_schedule_id** | **str**|  | 
 **invoice_timing** | **str**| Optional field to filter pricing rules based on invoice timing | [optional] 

### Return type

[**PricingRulesPaginatedResponse**](PricingRulesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for create/list pricing rules request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

