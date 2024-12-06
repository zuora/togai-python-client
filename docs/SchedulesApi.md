# togai_client.SchedulesApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_edit_schedules**](SchedulesApi.md#bulk_edit_schedules) | **POST** /v2/accounts/{account_id}/edit_schedules | Bulk edit schedules of an account
[**bulk_rate_card_operations_on_schedule**](SchedulesApi.md#bulk_rate_card_operations_on_schedule) | **POST** /v2/schedules/{schedule_id}/rate_cards | Bulk rate card operations on a schedule
[**discard_account_schedules**](SchedulesApi.md#discard_account_schedules) | **DELETE** /v2/accounts/{account_id}/discard_schedules | Discard schedules of an account
[**finalize_account_schedules**](SchedulesApi.md#finalize_account_schedules) | **POST** /v2/accounts/{account_id}/finalize_schedules | Finalize schedules of an account
[**list_pricing_rules**](SchedulesApi.md#list_pricing_rules) | **GET** /v2/schedules/{schedule_id}/pricing_rules | List pricing rules of a account schedule
[**list_schedule_errors**](SchedulesApi.md#list_schedule_errors) | **GET** /v2/schedules/{schedule_id}/errors | Get list of errors of a acc schedule
[**list_schedule_rate_cards**](SchedulesApi.md#list_schedule_rate_cards) | **GET** /v2/schedules/{schedule_id}/rate_cards | List rate cards
[**listaccount_schedules**](SchedulesApi.md#listaccount_schedules) | **GET** /v2/accounts/{account_id}/schedules | List pricing schedules of an account
[**update_pricing_rules**](SchedulesApi.md#update_pricing_rules) | **PUT** /v2/schedules/{schedule_id}/pricing_rules | Update pricing rules of a account schedule


# **bulk_edit_schedules**
> UpdatePricingScheduleResponse bulk_edit_schedules(account_id, edit_account_schedule_request, discard=discard)

Bulk edit schedules of an account

Bulk edit schedules of an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.edit_account_schedule_request import EditAccountScheduleRequest
from togai_client.models.update_pricing_schedule_response import UpdatePricingScheduleResponse
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
    api_instance = togai_client.SchedulesApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    edit_account_schedule_request = togai_client.EditAccountScheduleRequest() # EditAccountScheduleRequest | Payload to edit schedules of an account
    discard = false # bool |  (optional)

    try:
        # Bulk edit schedules of an account
        api_response = api_instance.bulk_edit_schedules(account_id, edit_account_schedule_request, discard=discard)
        print("The response of SchedulesApi->bulk_edit_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->bulk_edit_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **edit_account_schedule_request** | [**EditAccountScheduleRequest**](EditAccountScheduleRequest.md)| Payload to edit schedules of an account | 
 **discard** | **bool**|  | [optional] 

### Return type

[**UpdatePricingScheduleResponse**](UpdatePricingScheduleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for dis/associate price plan request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_rate_card_operations_on_schedule**
> BulkRateCardOperationsResponse bulk_rate_card_operations_on_schedule(schedule_id, bulk_rate_card_operations_request)

Bulk rate card operations on a schedule

Bulk rate card operations on a schedule

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.bulk_rate_card_operations_request import BulkRateCardOperationsRequest
from togai_client.models.bulk_rate_card_operations_response import BulkRateCardOperationsResponse
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
    api_instance = togai_client.SchedulesApi(api_client)
    schedule_id = 'sch.20aUyEZSuYq.SoGbS' # str | 
    bulk_rate_card_operations_request = togai_client.BulkRateCardOperationsRequest() # BulkRateCardOperationsRequest | Payload to bulk rate card operations

    try:
        # Bulk rate card operations on a schedule
        api_response = api_instance.bulk_rate_card_operations_on_schedule(schedule_id, bulk_rate_card_operations_request)
        print("The response of SchedulesApi->bulk_rate_card_operations_on_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->bulk_rate_card_operations_on_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **bulk_rate_card_operations_request** | [**BulkRateCardOperationsRequest**](BulkRateCardOperationsRequest.md)| Payload to bulk rate card operations | 

### Return type

[**BulkRateCardOperationsResponse**](BulkRateCardOperationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for bulk rate card operations of a price plan |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discard_account_schedules**
> BaseSuccessResponse discard_account_schedules(account_id)

Discard schedules of an account

Discard schedules of an account

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
    api_instance = togai_client.SchedulesApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # Discard schedules of an account
        api_response = api_instance.discard_account_schedules(account_id)
        print("The response of SchedulesApi->discard_account_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->discard_account_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

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

# **finalize_account_schedules**
> SchedulesPaginatedResponse finalize_account_schedules(account_id, finalize_account_schedules)

Finalize schedules of an account

Finalize schedules of an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.finalize_account_schedules import FinalizeAccountSchedules
from togai_client.models.schedules_paginated_response import SchedulesPaginatedResponse
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
    api_instance = togai_client.SchedulesApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    finalize_account_schedules = togai_client.FinalizeAccountSchedules() # FinalizeAccountSchedules | Payload to finalize account schedules

    try:
        # Finalize schedules of an account
        api_response = api_instance.finalize_account_schedules(account_id, finalize_account_schedules)
        print("The response of SchedulesApi->finalize_account_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->finalize_account_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **finalize_account_schedules** | [**FinalizeAccountSchedules**](FinalizeAccountSchedules.md)| Payload to finalize account schedules | 

### Return type

[**SchedulesPaginatedResponse**](SchedulesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated response for pricing schedules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pricing_rules**
> PricingRulesPaginatedResponse list_pricing_rules(schedule_id, mode)

List pricing rules of a account schedule

List pricing rules of a account schedule

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
    api_instance = togai_client.SchedulesApi(api_client)
    schedule_id = 'sch.20aUyEZSuYq.SoGbS' # str | 
    mode = 'mode_example' # str | Possible values: 1. ACTIVE - Get the active rate card 2. DRAFT - Get the draft rate card 

    try:
        # List pricing rules of a account schedule
        api_response = api_instance.list_pricing_rules(schedule_id, mode)
        print("The response of SchedulesApi->list_pricing_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->list_pricing_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **mode** | **str**| Possible values: 1. ACTIVE - Get the active rate card 2. DRAFT - Get the draft rate card  | 

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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedule_errors**
> ValidatedEntityErrorsPaginatedResponse list_schedule_errors(schedule_id)

Get list of errors of a acc schedule

Get list of errors of a acc schedule

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.validated_entity_errors_paginated_response import ValidatedEntityErrorsPaginatedResponse
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
    api_instance = togai_client.SchedulesApi(api_client)
    schedule_id = 'sch.20aUyEZSuYq.SoGbS' # str | 

    try:
        # Get list of errors of a acc schedule
        api_response = api_instance.list_schedule_errors(schedule_id)
        print("The response of SchedulesApi->list_schedule_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->list_schedule_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 

### Return type

[**ValidatedEntityErrorsPaginatedResponse**](ValidatedEntityErrorsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated response for draft entities validations |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedule_rate_cards**
> RateCardPaginatedResponse list_schedule_rate_cards(schedule_id, mode, next_token=next_token, page_size=page_size)

List rate cards

List rate cards

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.rate_card_paginated_response import RateCardPaginatedResponse
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
    api_instance = togai_client.SchedulesApi(api_client)
    schedule_id = 'sch.20aUyEZSuYq.SoGbS' # str | 
    mode = 'mode_example' # str | Possible values: 1. ACTIVE - Get the active rate card 2. DRAFT - Get the draft rate card 
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List rate cards
        api_response = api_instance.list_schedule_rate_cards(schedule_id, mode, next_token=next_token, page_size=page_size)
        print("The response of SchedulesApi->list_schedule_rate_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->list_schedule_rate_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **mode** | **str**| Possible values: 1. ACTIVE - Get the active rate card 2. DRAFT - Get the draft rate card  | 
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**RateCardPaginatedResponse**](RateCardPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list rate cards request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listaccount_schedules**
> SchedulesPaginatedResponse listaccount_schedules(account_id, mode, next_token=next_token, page_size=page_size)

List pricing schedules of an account

List pricing schedules of an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.schedules_paginated_response import SchedulesPaginatedResponse
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
    api_instance = togai_client.SchedulesApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    mode = 'mode_example' # str | Possible values: 1. ACTIVE - Get the active rate card 2. DRAFT - Get the draft rate card 
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List pricing schedules of an account
        api_response = api_instance.listaccount_schedules(account_id, mode, next_token=next_token, page_size=page_size)
        print("The response of SchedulesApi->listaccount_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->listaccount_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **mode** | **str**| Possible values: 1. ACTIVE - Get the active rate card 2. DRAFT - Get the draft rate card  | 
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**SchedulesPaginatedResponse**](SchedulesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated response for pricing schedules |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_rules**
> PricingRulesPaginatedResponse update_pricing_rules(schedule_id, update_pricing_rules_request)

Update pricing rules of a account schedule

Update pricing rules of a account schedule

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.pricing_rules_paginated_response import PricingRulesPaginatedResponse
from togai_client.models.update_pricing_rules_request import UpdatePricingRulesRequest
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
    api_instance = togai_client.SchedulesApi(api_client)
    schedule_id = 'sch.20aUyEZSuYq.SoGbS' # str | 
    update_pricing_rules_request = togai_client.UpdatePricingRulesRequest() # UpdatePricingRulesRequest | Payload to update pricing rules

    try:
        # Update pricing rules of a account schedule
        api_response = api_instance.update_pricing_rules(schedule_id, update_pricing_rules_request)
        print("The response of SchedulesApi->update_pricing_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->update_pricing_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **update_pricing_rules_request** | [**UpdatePricingRulesRequest**](UpdatePricingRulesRequest.md)| Payload to update pricing rules | 

### Return type

[**PricingRulesPaginatedResponse**](PricingRulesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for create/list pricing rules request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

