# togai_client.PricePlansApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_price_plan**](PricePlansApi.md#activate_price_plan) | **POST** /price_plans/{price_plan_id}/activate | (DEPRECATED) Activate a price plan
[**archive_price_plan**](PricePlansApi.md#archive_price_plan) | **DELETE** /price_plans/{price_plan_id} | (DEPRECATED) Archive a price plan
[**create_price_plan**](PricePlansApi.md#create_price_plan) | **POST** /price_plans | (DEPRECATED) Create a price plan
[**get_price_plan**](PricePlansApi.md#get_price_plan) | **GET** /price_plans/{price_plan_id} | (DEPRECATED) Get a price plan
[**get_price_plans**](PricePlansApi.md#get_price_plans) | **GET** /price_plans | (DEPRECATED) List price plans
[**price_plan_migration**](PricePlansApi.md#price_plan_migration) | **POST** /price_plans/migration | (DEPRECATED) Create a price plan migration
[**update_price_plan**](PricePlansApi.md#update_price_plan) | **PATCH** /price_plans/{price_plan_id} | (DEPRECATED) Update a price plan


# **activate_price_plan**
> PricePlan activate_price_plan(price_plan_id, activate_price_plan_request)

(DEPRECATED) Activate a price plan

Activate a price plan details using price plan id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.activate_price_plan_request import ActivatePricePlanRequest
from togai_client.models.price_plan import PricePlan
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
    api_instance = togai_client.PricePlansApi(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    activate_price_plan_request = togai_client.ActivatePricePlanRequest() # ActivatePricePlanRequest | Payload to activate price plan

    try:
        # (DEPRECATED) Activate a price plan
        api_response = api_instance.activate_price_plan(price_plan_id, activate_price_plan_request)
        print("The response of PricePlansApi->activate_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->activate_price_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **activate_price_plan_request** | [**ActivatePricePlanRequest**](ActivatePricePlanRequest.md)| Payload to activate price plan | 

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_price_plan**
> BaseSuccessResponse archive_price_plan(price_plan_id)

(DEPRECATED) Archive a price plan

Archive a price plan

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
    api_instance = togai_client.PricePlansApi(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 

    try:
        # (DEPRECATED) Archive a price plan
        api_response = api_instance.archive_price_plan(price_plan_id)
        print("The response of PricePlansApi->archive_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->archive_price_plan: %s\n" % e)
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
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price_plan**
> PricePlan create_price_plan(create_price_plan_request, dry_run=dry_run)

(DEPRECATED) Create a price plan

This API let's you create and price plan Learn more about [Price Plans](https://docs.togai.com/docs/priceplan) 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_price_plan_request import CreatePricePlanRequest
from togai_client.models.price_plan import PricePlan
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
    api_instance = togai_client.PricePlansApi(api_client)
    create_price_plan_request = togai_client.CreatePricePlanRequest() # CreatePricePlanRequest | Payload to create price plan
    dry_run = false # bool |  (optional)

    try:
        # (DEPRECATED) Create a price plan
        api_response = api_instance.create_price_plan(create_price_plan_request, dry_run=dry_run)
        print("The response of PricePlansApi->create_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->create_price_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_price_plan_request** | [**CreatePricePlanRequest**](CreatePricePlanRequest.md)| Payload to create price plan | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_plan**
> PricePlan get_price_plan(price_plan_id, version=version)

(DEPRECATED) Get a price plan

Get a price plan details using price plan id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan import PricePlan
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
    api_instance = togai_client.PricePlansApi(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    version = 2 # int | Optional version to get a specific version. Gets latest version if it is not provided. (optional)

    try:
        # (DEPRECATED) Get a price plan
        api_response = api_instance.get_price_plan(price_plan_id, version=version)
        print("The response of PricePlansApi->get_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->get_price_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **version** | **int**| Optional version to get a specific version. Gets latest version if it is not provided. | [optional] 

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_plans**
> PricePlanPaginatedResponse get_price_plans(next_token=next_token, page_size=page_size)

(DEPRECATED) List price plans

Get a list of price plans

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan_paginated_response import PricePlanPaginatedResponse
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
    api_instance = togai_client.PricePlansApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # (DEPRECATED) List price plans
        api_response = api_instance.get_price_plans(next_token=next_token, page_size=page_size)
        print("The response of PricePlansApi->get_price_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->get_price_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**PricePlanPaginatedResponse**](PricePlanPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list price plans request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_plan_migration**
> BaseSuccessResponse price_plan_migration(create_price_plan_migration_request)

(DEPRECATED) Create a price plan migration

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
    api_instance = togai_client.PricePlansApi(api_client)
    create_price_plan_migration_request = togai_client.CreatePricePlanMigrationRequest() # CreatePricePlanMigrationRequest | Payload to create price plan migration request

    try:
        # (DEPRECATED) Create a price plan migration
        api_response = api_instance.price_plan_migration(create_price_plan_migration_request)
        print("The response of PricePlansApi->price_plan_migration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->price_plan_migration: %s\n" % e)
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

# **update_price_plan**
> PricePlan update_price_plan(price_plan_id, update_price_plan_request)

(DEPRECATED) Update a price plan

Update an existing price plan Price Plans with status as DRAFT alone can be updated . Learn more about [Price plans](https://docs.togai.com/docs/priceplan) from our Guides 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.price_plan import PricePlan
from togai_client.models.update_price_plan_request import UpdatePricePlanRequest
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
    api_instance = togai_client.PricePlansApi(api_client)
    price_plan_id = 'pp.1zYnCiM9Bpg.lv25y' # str | 
    update_price_plan_request = togai_client.UpdatePricePlanRequest() # UpdatePricePlanRequest | Payload to update price plan

    try:
        # (DEPRECATED) Update a price plan
        api_response = api_instance.update_price_plan(price_plan_id, update_price_plan_request)
        print("The response of PricePlansApi->update_price_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricePlansApi->update_price_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_id** | **str**|  | 
 **update_price_plan_request** | [**UpdatePricePlanRequest**](UpdatePricePlanRequest.md)| Payload to update price plan | 

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

