# togai_client.EntitlementsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entitlement_value**](EntitlementsApi.md#get_entitlement_value) | **GET** /accounts/{account_id}/entitlements/{feature_id} | Get entitlement value for a account
[**get_entitlements**](EntitlementsApi.md#get_entitlements) | **GET** /accounts/{account_id}/entitlements | Get entitlements for a account
[**get_feature_credits**](EntitlementsApi.md#get_feature_credits) | **GET** /accounts/{account_id}/features/{feature_id} | Get Feature credits balance
[**ingest_entitled_event**](EntitlementsApi.md#ingest_entitled_event) | **POST** /entitled | Ingest event if a user is entitled to a feature
[**list_feature_credit_entries**](EntitlementsApi.md#list_feature_credit_entries) | **GET** /accounts/{account_id}/features/{feature_id}/entries | List feature credits entries of a feature for an account
[**update_feature_credit_entry**](EntitlementsApi.md#update_feature_credit_entry) | **PATCH** /accounts/{account_id}/features/{feature_id}/entries/{entry_id} | Update a feature credits entry
[**validate_entitlement_value**](EntitlementsApi.md#validate_entitlement_value) | **POST** /accounts/{account_id}/entitlements/{feature_id} | Check entitlement value for a account
[**void_feature_credit_entry**](EntitlementsApi.md#void_feature_credit_entry) | **POST** /accounts/{account_id}/features/{feature_id}/entries/{entry_id}/void | Void a feature credits entry of a feature for an account


# **get_entitlement_value**
> GetEntitlementValuesResponse get_entitlement_value(account_id, feature_id)

Get entitlement value for a account

This API let’s you to get the entitlement value for a account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_entitlement_values_response import GetEntitlementValuesResponse
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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature

    try:
        # Get entitlement value for a account
        api_response = api_instance.get_entitlement_value(account_id, feature_id)
        print("The response of EntitlementsApi->get_entitlement_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **feature_id** | **str**| feature_id corresponding to a feature | 

### Return type

[**GetEntitlementValuesResponse**](GetEntitlementValuesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlements**
> GetEntitlementValuesResponse get_entitlements(account_id)

Get entitlements for a account

This API let’s you to get the entitlements for a account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_entitlement_values_response import GetEntitlementValuesResponse
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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # Get entitlements for a account
        api_response = api_instance.get_entitlements(account_id)
        print("The response of EntitlementsApi->get_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

### Return type

[**GetEntitlementValuesResponse**](GetEntitlementValuesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_credits**
> GetFeatureCreditsResponse get_feature_credits(account_id, feature_id)

Get Feature credits balance

This API let’s you to get the feature credits balance

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_feature_credits_response import GetFeatureCreditsResponse
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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature

    try:
        # Get Feature credits balance
        api_response = api_instance.get_feature_credits(account_id, feature_id)
        print("The response of EntitlementsApi->get_feature_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_feature_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **feature_id** | **str**| feature_id corresponding to a feature | 

### Return type

[**GetFeatureCreditsResponse**](GetFeatureCreditsResponse.md)

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
**403** | Credential does not have access to add a license entry. |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_entitled_event**
> BaseSuccessResponse ingest_entitled_event(ingest_event_request=ingest_event_request)

Ingest event if a user is entitled to a feature

This API let’s you to ingest an event if a user is entitled to a feature

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.models.ingest_event_request import IngestEventRequest
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
    api_instance = togai_client.EntitlementsApi(api_client)
    ingest_event_request = togai_client.IngestEventRequest() # IngestEventRequest |  (optional)

    try:
        # Ingest event if a user is entitled to a feature
        api_response = api_instance.ingest_entitled_event(ingest_event_request=ingest_event_request)
        print("The response of EntitlementsApi->ingest_entitled_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->ingest_entitled_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_event_request** | [**IngestEventRequest**](IngestEventRequest.md)|  | [optional] 

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
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to add a license entry. |  -  |
**409** | Duplicate Id |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_feature_credit_entries**
> GetFeatureCreditEntriesPaginatedResponse list_feature_credit_entries(account_id, feature_id, page_size=page_size, next_token=next_token)

List feature credits entries of a feature for an account

This API let’s you to list the feature credits entries of a feature for an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_feature_credit_entries_paginated_response import GetFeatureCreditEntriesPaginatedResponse
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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)

    try:
        # List feature credits entries of a feature for an account
        api_response = api_instance.list_feature_credit_entries(account_id, feature_id, page_size=page_size, next_token=next_token)
        print("The response of EntitlementsApi->list_feature_credit_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_feature_credit_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **feature_id** | **str**| feature_id corresponding to a feature | 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 

### Return type

[**GetFeatureCreditEntriesPaginatedResponse**](GetFeatureCreditEntriesPaginatedResponse.md)

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
**403** | Credential does not have access to add a license entry. |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feature_credit_entry**
> FeatureCreditEntry update_feature_credit_entry(account_id, feature_id, entry_id, update_feature_credits_request=update_feature_credits_request)

Update a feature credits entry

#### This API let's you to update the following attributes: `effectiveUntil` and `granted`  - **effectiveUntil**: must be in future - **granted**: must be greater than the existing usage (previous granted - current balance) 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.feature_credit_entry import FeatureCreditEntry
from togai_client.models.update_feature_credits_request import UpdateFeatureCreditsRequest
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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature
    entry_id = 'purchase.21HbazIT3JQ.D90jC#1$PURCHASE' # str | `entryId` corresponding to a particular entitlement/overage grant entry  Formats: 1. If source of entry is an entitlement grant rate card in price plan: `schedule_id#pricing_cycle_start_date$PRICE_PLAN` 2. If source of entry is an entitlement overage rate card in price plan: `schedule_id#pricing_cycle_start_date$OVERAGE` 3. If source of entry is a purchase: `purchase_id#int_index$PURCHASE` 
    update_feature_credits_request = {"effectiveUntil":"2023-02-23T14:25:10Z","granted":200} # UpdateFeatureCreditsRequest |  (optional)

    try:
        # Update a feature credits entry
        api_response = api_instance.update_feature_credit_entry(account_id, feature_id, entry_id, update_feature_credits_request=update_feature_credits_request)
        print("The response of EntitlementsApi->update_feature_credit_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->update_feature_credit_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **feature_id** | **str**| feature_id corresponding to a feature | 
 **entry_id** | **str**| &#x60;entryId&#x60; corresponding to a particular entitlement/overage grant entry  Formats: 1. If source of entry is an entitlement grant rate card in price plan: &#x60;schedule_id#pricing_cycle_start_date$PRICE_PLAN&#x60; 2. If source of entry is an entitlement overage rate card in price plan: &#x60;schedule_id#pricing_cycle_start_date$OVERAGE&#x60; 3. If source of entry is a purchase: &#x60;purchase_id#int_index$PURCHASE&#x60;  | 
 **update_feature_credits_request** | [**UpdateFeatureCreditsRequest**](UpdateFeatureCreditsRequest.md)|  | [optional] 

### Return type

[**FeatureCreditEntry**](FeatureCreditEntry.md)

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
**403** | Credential does not have access to update a feature credit entry. |  -  |
**404** | Entry not found. Please check the response message for failure details. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_entitlement_value**
> BaseSuccessResponse validate_entitlement_value(account_id, feature_id, validate_entitlement_value_request=validate_entitlement_value_request)

Check entitlement value for a account

This API let’s you to validate the entitlement value for a account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.models.validate_entitlement_value_request import ValidateEntitlementValueRequest
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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature
    validate_entitlement_value_request = {"value":"enum1"} # ValidateEntitlementValueRequest |  (optional)

    try:
        # Check entitlement value for a account
        api_response = api_instance.validate_entitlement_value(account_id, feature_id, validate_entitlement_value_request=validate_entitlement_value_request)
        print("The response of EntitlementsApi->validate_entitlement_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->validate_entitlement_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **feature_id** | **str**| feature_id corresponding to a feature | 
 **validate_entitlement_value_request** | [**ValidateEntitlementValueRequest**](ValidateEntitlementValueRequest.md)|  | [optional] 

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
**200** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_feature_credit_entry**
> BaseSuccessResponse void_feature_credit_entry(account_id, feature_id, entry_id)

Void a feature credits entry of a feature for an account

This API let’s you to void the feature credits entries of a feature for an account

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
    api_instance = togai_client.EntitlementsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature
    entry_id = 'purchase.21HbazIT3JQ.D90jC#1$PURCHASE' # str | `entryId` corresponding to a particular entitlement/overage grant entry  Formats: 1. If source of entry is an entitlement grant rate card in price plan: `schedule_id#pricing_cycle_start_date$PRICE_PLAN` 2. If source of entry is an entitlement overage rate card in price plan: `schedule_id#pricing_cycle_start_date$OVERAGE` 3. If source of entry is a purchase: `purchase_id#int_index$PURCHASE` 

    try:
        # Void a feature credits entry of a feature for an account
        api_response = api_instance.void_feature_credit_entry(account_id, feature_id, entry_id)
        print("The response of EntitlementsApi->void_feature_credit_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->void_feature_credit_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **feature_id** | **str**| feature_id corresponding to a feature | 
 **entry_id** | **str**| &#x60;entryId&#x60; corresponding to a particular entitlement/overage grant entry  Formats: 1. If source of entry is an entitlement grant rate card in price plan: &#x60;schedule_id#pricing_cycle_start_date$PRICE_PLAN&#x60; 2. If source of entry is an entitlement overage rate card in price plan: &#x60;schedule_id#pricing_cycle_start_date$OVERAGE&#x60; 3. If source of entry is a purchase: &#x60;purchase_id#int_index$PURCHASE&#x60;  | 

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
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to void a feature credit entry. |  -  |
**404** | Entry not found. Please check the response message for failure details. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

