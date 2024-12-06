# togai_client.LicensesApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_license_update_entry**](LicensesApi.md#add_license_update_entry) | **POST** /license_updates | Update a license entry
[**get_license_updates**](LicensesApi.md#get_license_updates) | **GET** /license_updates | Get a list of licenses updates
[**get_named_license_updates**](LicensesApi.md#get_named_license_updates) | **GET** /named_license_updates | Get a list of named licenses updates
[**update_license_entry_details**](LicensesApi.md#update_license_entry_details) | **PATCH** /license_updates/{license_id} | Update a license entry details


# **add_license_update_entry**
> LicenseUpdateResponse add_license_update_entry(license_update_request=license_update_request)

Update a license entry

This API let’s you to add a license entry

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.license_update_request import LicenseUpdateRequest
from togai_client.models.license_update_response import LicenseUpdateResponse
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
    api_instance = togai_client.LicensesApi(api_client)
    license_update_request = {"licenseId":"addon.21LdC76myzw.uiSWm","accountId":"account#1","updateType":"ABSOLUTE","quantity":10} # LicenseUpdateRequest |  (optional)

    try:
        # Update a license entry
        api_response = api_instance.add_license_update_entry(license_update_request=license_update_request)
        print("The response of LicensesApi->add_license_update_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->add_license_update_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_update_request** | [**LicenseUpdateRequest**](LicenseUpdateRequest.md)|  | [optional] 

### Return type

[**LicenseUpdateResponse**](LicenseUpdateResponse.md)

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
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_updates**
> GetLicenseUpdatesResponse get_license_updates(next_token=next_token, account_id=account_id, page_size=page_size, license_id=license_id, effective_from=effective_from)

Get a list of licenses updates

This API let’s you to fetch a list of licenses updates with multiple query parameters

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_license_updates_response import GetLicenseUpdatesResponse
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
    api_instance = togai_client.LicensesApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)
    account_id = '1234' # str | Filter option to filter based on account id. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)
    license_id = 'addon.1zYnCiM9Bpg.1zYn' # str | License Id to filter (optional)
    effective_from = '2021-03-04T14:25:10Z' # datetime | effectiveFrom to filter (optional)

    try:
        # Get a list of licenses updates
        api_response = api_instance.get_license_updates(next_token=next_token, account_id=account_id, page_size=page_size, license_id=license_id, effective_from=effective_from)
        print("The response of LicensesApi->get_license_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->get_license_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 
 **account_id** | **str**| Filter option to filter based on account id. | [optional] 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 
 **license_id** | **str**| License Id to filter | [optional] 
 **effective_from** | **datetime**| effectiveFrom to filter | [optional] 

### Return type

[**GetLicenseUpdatesResponse**](GetLicenseUpdatesResponse.md)

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
**403** | Credential does not have access to list licenses updates. |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_license_updates**
> NamedLicenseUpdatesPaginatedResponse get_named_license_updates()

Get a list of named licenses updates

This API let’s you to fetch a list of named licenses updates with multiple query parameters

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.named_license_updates_paginated_response import NamedLicenseUpdatesPaginatedResponse
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
    api_instance = togai_client.LicensesApi(api_client)

    try:
        # Get a list of named licenses updates
        api_response = api_instance.get_named_license_updates()
        print("The response of LicensesApi->get_named_license_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->get_named_license_updates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NamedLicenseUpdatesPaginatedResponse**](NamedLicenseUpdatesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license_entry_details**
> LicenseUpdateResponse update_license_entry_details(license_id=license_id, license_entry_details_update_request=license_entry_details_update_request)

Update a license entry details

This API let’s you to update metadata of a license entry

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.license_entry_details_update_request import LicenseEntryDetailsUpdateRequest
from togai_client.models.license_update_response import LicenseUpdateResponse
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
    api_instance = togai_client.LicensesApi(api_client)
    license_id = 'addon.1zYnCiM9Bpg.1zYn' # str | License Id to filter (optional)
    license_entry_details_update_request = {"accountId":"account#1","effectiveFrom":"2020-01-01T00:00:00Z","metadata":{"PO Number":"PO.432t5kbj.43tdsv"}} # LicenseEntryDetailsUpdateRequest |  (optional)

    try:
        # Update a license entry details
        api_response = api_instance.update_license_entry_details(license_id=license_id, license_entry_details_update_request=license_entry_details_update_request)
        print("The response of LicensesApi->update_license_entry_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->update_license_entry_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| License Id to filter | [optional] 
 **license_entry_details_update_request** | [**LicenseEntryDetailsUpdateRequest**](LicenseEntryDetailsUpdateRequest.md)|  | [optional] 

### Return type

[**LicenseUpdateResponse**](LicenseUpdateResponse.md)

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
**403** | Credential does not have access to update a license entry. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

