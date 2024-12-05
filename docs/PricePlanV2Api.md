# togai_client.PricePlanV2Api

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_price_plan_rate_card_operations**](PricePlanV2Api.md#bulk_price_plan_rate_card_operations) | **POST** /v2/price_plans/{price_plan_id}/rate_cards | Bulk rate card operations of a price plan
[**create_price_plan_v2**](PricePlanV2Api.md#create_price_plan_v2) | **POST** /v2/price_plans | Create a price plan
[**discard_price_plan**](PricePlanV2Api.md#discard_price_plan) | **DELETE** /v2/price_plans/{price_plan_id}/discard | Discard a price plan
[**finalize_price_plan**](PricePlanV2Api.md#finalize_price_plan) | **POST** /v2/price_plans/{price_plan_id}/finalize | Finalize a price plan
[**get_price_plan_v2**](PricePlanV2Api.md#get_price_plan_v2) | **GET** /v2/price_plans/{price_plan_id} | Get a price plan
[**list_price_plan_errors**](PricePlanV2Api.md#list_price_plan_errors) | **GET** /v2/price_plans/{price_plan_id}/errors | Get list of errors of a price plan
[**list_price_plan_pricing_rules**](PricePlanV2Api.md#list_price_plan_pricing_rules) | **GET** /v2/price_plans/{price_plan_id}/pricing_rules | List pricing rules of a price plan
[**list_price_plan_rate_cards**](PricePlanV2Api.md#list_price_plan_rate_cards) | **GET** /v2/price_plans/{price_plan_id}/rate_cards | List rate cards of a price plan
[**list_price_plan_versions**](PricePlanV2Api.md#list_price_plan_versions) | **GET** /v2/price_plans/{price_plan_id}/versions | List price plan versions
[**list_price_plans_v2**](PricePlanV2Api.md#list_price_plans_v2) | **GET** /v2/price_plans | List price plans
[**price_plan_migration_v2**](PricePlanV2Api.md#price_plan_migration_v2) | **POST** /v2/price_plans/migration | Create a price plan v2 migration
[**update_price_plan_pricing_rules**](PricePlanV2Api.md#update_price_plan_pricing_rules) | **PUT** /v2/price_plans/{price_plan_id}/pricing_rules | Update pricing rules of a price plan
[**update_price_plan_v2**](PricePlanV2Api.md#update_price_plan_v2) | **PATCH** /v2/price_plans/{price_plan_id} | Update a price plan


# **bulk_price_plan_rate_card_operations**
> BulkRateCardOperationsResponse bulk_price_plan_rate_card_operations(price_plan_id, bulk_rate_card_operations_request)

Bulk rate card operations of a price plan

Bulk rate card operations of a price plan

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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    bulk_rate_card_operations_request = togai_client.BulkRateCardOperationsRequest() # BulkRateCardOperationsRequest | Payload to bulk rate card operations

    try:
        # Bulk rate card operations of a price plan
        api_response = api_instance.bulk_price_plan_rate_card_operations(price_plan_id, bulk_rate_card_operations_request)
        print("The response of PricePlanV2Api->bulk_price_plan_rate_card_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->bulk_price_plan_rate_card_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
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

# **create_price_plan_v2**
> PricePlanV2 create_price_plan_v2(create_price_plan_v2_request)

Create a price plan

Create a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_price_plan_v2_request import CreatePricePlanV2Request
from togai_client.models.price_plan_v2 import PricePlanV2
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    create_price_plan_v2_request = togai_client.CreatePricePlanV2Request() # CreatePricePlanV2Request | Payload to create price plan

    try:
        # Create a price plan
        api_response = api_instance.create_price_plan_v2(create_price_plan_v2_request)
        print("The response of PricePlanV2Api->create_price_plan_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->create_price_plan_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_price_plan_v2_request** | [**CreatePricePlanV2Request**](CreatePricePlanV2Request.md)| Payload to create price plan | 

### Return type

[**PricePlanV2**](PricePlanV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discard_price_plan**
> BaseSuccessResponse discard_price_plan(price_plan_id)

Discard a price plan

Discard a price plan

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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 

    try:
        # Discard a price plan
        api_response = api_instance.discard_price_plan(price_plan_id)
        print("The response of PricePlanV2Api->discard_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->discard_price_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 

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

# **finalize_price_plan**
> BaseSuccessResponse finalize_price_plan(price_plan_id, finalize_price_plan_request)

Finalize a price plan

Finalize a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.models.finalize_price_plan_request import FinalizePricePlanRequest
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    finalize_price_plan_request = togai_client.FinalizePricePlanRequest() # FinalizePricePlanRequest | Payload to finalize price plan

    try:
        # Finalize a price plan
        api_response = api_instance.finalize_price_plan(price_plan_id, finalize_price_plan_request)
        print("The response of PricePlanV2Api->finalize_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->finalize_price_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **finalize_price_plan_request** | [**FinalizePricePlanRequest**](FinalizePricePlanRequest.md)| Payload to finalize price plan | 

### Return type

[**BaseSuccessResponse**](BaseSuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_plan_v2**
> PricePlanV2 get_price_plan_v2(price_plan_id, version=version)

Get a price plan

Get a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan_v2 import PricePlanV2
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    version = 'version_example' # str | Optional version to get a specific version. Gets latest version if it is not provided. Possible values: 1. LATEST - Get the latest version of the price plan, can be draft 2. ACTIVE - Get the latest active version of the price plan 3. NUMBER - Get the specific version of the price plans  (optional)

    try:
        # Get a price plan
        api_response = api_instance.get_price_plan_v2(price_plan_id, version=version)
        print("The response of PricePlanV2Api->get_price_plan_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->get_price_plan_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **version** | **str**| Optional version to get a specific version. Gets latest version if it is not provided. Possible values: 1. LATEST - Get the latest version of the price plan, can be draft 2. ACTIVE - Get the latest active version of the price plan 3. NUMBER - Get the specific version of the price plans  | [optional] 

### Return type

[**PricePlanV2**](PricePlanV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_plan_errors**
> ValidatedEntityErrorsPaginatedResponse list_price_plan_errors(price_plan_id)

Get list of errors of a price plan

Get list of errors of a price plan

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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 

    try:
        # Get list of errors of a price plan
        api_response = api_instance.list_price_plan_errors(price_plan_id)
        print("The response of PricePlanV2Api->list_price_plan_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->list_price_plan_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 

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

# **list_price_plan_pricing_rules**
> PricingRulesPaginatedResponse list_price_plan_pricing_rules(price_plan_id, version=version)

List pricing rules of a price plan

List pricing rules of a price plan

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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    version = 'version_example' # str | Optional version to get a specific version. Gets latest version if it is not provided. Possible values: 1. LATEST - Get the latest version of the price plan, can be draft 2. ACTIVE - Get the latest active version of the price plan 3. NUMBER - Get the specific version of the price plans  (optional)

    try:
        # List pricing rules of a price plan
        api_response = api_instance.list_price_plan_pricing_rules(price_plan_id, version=version)
        print("The response of PricePlanV2Api->list_price_plan_pricing_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->list_price_plan_pricing_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **version** | **str**| Optional version to get a specific version. Gets latest version if it is not provided. Possible values: 1. LATEST - Get the latest version of the price plan, can be draft 2. ACTIVE - Get the latest active version of the price plan 3. NUMBER - Get the specific version of the price plans  | [optional] 

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

# **list_price_plan_rate_cards**
> RateCardPaginatedResponse list_price_plan_rate_cards(price_plan_id, next_token=next_token, page_size=page_size)

List rate cards of a price plan

List rate cards of a price plan

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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List rate cards of a price plan
        api_response = api_instance.list_price_plan_rate_cards(price_plan_id, next_token=next_token, page_size=page_size)
        print("The response of PricePlanV2Api->list_price_plan_rate_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->list_price_plan_rate_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
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

# **list_price_plan_versions**
> PricePlanV2PaginatedResponse list_price_plan_versions(price_plan_id, next_token=next_token, page_size=page_size)

List price plan versions

List price plan versions

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan_v2_paginated_response import PricePlanV2PaginatedResponse
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List price plan versions
        api_response = api_instance.list_price_plan_versions(price_plan_id, next_token=next_token, page_size=page_size)
        print("The response of PricePlanV2Api->list_price_plan_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->list_price_plan_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**PricePlanV2PaginatedResponse**](PricePlanV2PaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list price plans request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_plans_v2**
> PricePlanV2PaginatedResponse list_price_plans_v2(next_token=next_token, page_size=page_size)

List price plans

List price plans

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan_v2_paginated_response import PricePlanV2PaginatedResponse
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List price plans
        api_response = api_instance.list_price_plans_v2(next_token=next_token, page_size=page_size)
        print("The response of PricePlanV2Api->list_price_plans_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->list_price_plans_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**PricePlanV2PaginatedResponse**](PricePlanV2PaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list price plans request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_plan_migration_v2**
> BaseSuccessResponse price_plan_migration_v2(create_price_plan_migration_request)

Create a price plan v2 migration

Migrates accounts across price plans. This is an asynchronous process functioning on top of Togai's Jobs  framework. Status of the created migrations can be obtained using the [Jobs APIs](https://docs.togai.com/api-reference/jobs/get-the-status-of-a-job) 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.models.create_price_plan_migration_request import CreatePricePlanMigrationRequest
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    create_price_plan_migration_request = togai_client.CreatePricePlanMigrationRequest() # CreatePricePlanMigrationRequest | Payload to create price plan migration request

    try:
        # Create a price plan v2 migration
        api_response = api_instance.price_plan_migration_v2(create_price_plan_migration_request)
        print("The response of PricePlanV2Api->price_plan_migration_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->price_plan_migration_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_price_plan_migration_request** | [**CreatePricePlanMigrationRequest**](CreatePricePlanMigrationRequest.md)| Payload to create price plan migration request | 

### Return type

[**BaseSuccessResponse**](BaseSuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price_plan_pricing_rules**
> PricingRulesPaginatedResponse update_price_plan_pricing_rules(price_plan_id, update_pricing_rules_request)

Update pricing rules of a price plan

Update pricing rules of a price plan

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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    update_pricing_rules_request = togai_client.UpdatePricingRulesRequest() # UpdatePricingRulesRequest | Payload to update pricing rules

    try:
        # Update pricing rules of a price plan
        api_response = api_instance.update_price_plan_pricing_rules(price_plan_id, update_pricing_rules_request)
        print("The response of PricePlanV2Api->update_price_plan_pricing_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->update_price_plan_pricing_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price_plan_v2**
> PricePlanV2 update_price_plan_v2(price_plan_id, update_price_plan_v2_request)

Update a price plan

Update a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan_v2 import PricePlanV2
from togai_client.models.update_price_plan_v2_request import UpdatePricePlanV2Request
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
    api_instance = togai_client.PricePlanV2Api(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    update_price_plan_v2_request = togai_client.UpdatePricePlanV2Request() # UpdatePricePlanV2Request | Payload to update price plan

    try:
        # Update a price plan
        api_response = api_instance.update_price_plan_v2(price_plan_id, update_price_plan_v2_request)
        print("The response of PricePlanV2Api->update_price_plan_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlanV2Api->update_price_plan_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **update_price_plan_v2_request** | [**UpdatePricePlanV2Request**](UpdatePricePlanV2Request.md)| Payload to update price plan | 

### Return type

[**PricePlanV2**](PricePlanV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

