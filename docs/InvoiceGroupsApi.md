# togai_client.InvoiceGroupsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invoice_group_accounts**](InvoiceGroupsApi.md#add_invoice_group_accounts) | **POST** /invoice_groups/{invoice_group_id}/add_accounts | Add accounts to an invoice group
[**create_invoice_group**](InvoiceGroupsApi.md#create_invoice_group) | **POST** /invoice_groups | Create an invoice group
[**get_invoice_group**](InvoiceGroupsApi.md#get_invoice_group) | **GET** /invoice_groups/{invoice_group_id} | Get information of an invoice group
[**list_invoice_groups**](InvoiceGroupsApi.md#list_invoice_groups) | **GET** /invoice_groups | List Invoice Groups
[**remove_invoice_group_accounts**](InvoiceGroupsApi.md#remove_invoice_group_accounts) | **POST** /invoice_groups/{invoice_group_id}/remove_accounts | Remove accounts from an invoice group. Removing all accounts will also delete the invoice group


# **add_invoice_group_accounts**
> InvoiceGroups add_invoice_group_accounts(invoice_group_id, update_invoice_group_accounts)

Add accounts to an invoice group

This API let’s you to add accounts to an invoice group

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.invoice_groups import InvoiceGroups
from togai_client.models.update_invoice_group_accounts import UpdateInvoiceGroupAccounts
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
    api_instance = togai_client.InvoiceGroupsApi(api_client)
    invoice_group_id = 'inv_grp.20rqjgFJf2O.ejl25' # str | 
    update_invoice_group_accounts = togai_client.UpdateInvoiceGroupAccounts() # UpdateInvoiceGroupAccounts | Payload to add or remove accounts to/from an invoice group

    try:
        # Add accounts to an invoice group
        api_response = api_instance.add_invoice_group_accounts(invoice_group_id, update_invoice_group_accounts)
        print("The response of InvoiceGroupsApi->add_invoice_group_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceGroupsApi->add_invoice_group_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_group_id** | **str**|  | 
 **update_invoice_group_accounts** | [**UpdateInvoiceGroupAccounts**](UpdateInvoiceGroupAccounts.md)| Payload to add or remove accounts to/from an invoice group | 

### Return type

[**InvoiceGroups**](InvoiceGroups.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to create invoice group request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_group**
> InvoiceGroups create_invoice_group(create_invoice_group_request)

Create an invoice group

This API let’s you to create an invoice group

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_invoice_group_request import CreateInvoiceGroupRequest
from togai_client.models.invoice_groups import InvoiceGroups
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
    api_instance = togai_client.InvoiceGroupsApi(api_client)
    create_invoice_group_request = togai_client.CreateInvoiceGroupRequest() # CreateInvoiceGroupRequest | Payload to approve or decline a proposal

    try:
        # Create an invoice group
        api_response = api_instance.create_invoice_group(create_invoice_group_request)
        print("The response of InvoiceGroupsApi->create_invoice_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceGroupsApi->create_invoice_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice_group_request** | [**CreateInvoiceGroupRequest**](CreateInvoiceGroupRequest.md)| Payload to approve or decline a proposal | 

### Return type

[**InvoiceGroups**](InvoiceGroups.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to create invoice group request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_group**
> InvoiceGroupAccountsPaginatedResponse get_invoice_group(invoice_group_id)

Get information of an invoice group

This API let’s you to get information of an invoice group

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.invoice_group_accounts_paginated_response import InvoiceGroupAccountsPaginatedResponse
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
    api_instance = togai_client.InvoiceGroupsApi(api_client)
    invoice_group_id = 'inv_grp.20rqjgFJf2O.ejl25' # str | 

    try:
        # Get information of an invoice group
        api_response = api_instance.get_invoice_group(invoice_group_id)
        print("The response of InvoiceGroupsApi->get_invoice_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceGroupsApi->get_invoice_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_group_id** | **str**|  | 

### Return type

[**InvoiceGroupAccountsPaginatedResponse**](InvoiceGroupAccountsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to get invoice group request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoice_groups**
> InvoiceGroupPaginatedResponse list_invoice_groups()

List Invoice Groups

This API let’s you to list invoice groups

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.invoice_group_paginated_response import InvoiceGroupPaginatedResponse
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
    api_instance = togai_client.InvoiceGroupsApi(api_client)

    try:
        # List Invoice Groups
        api_response = api_instance.list_invoice_groups()
        print("The response of InvoiceGroupsApi->list_invoice_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceGroupsApi->list_invoice_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InvoiceGroupPaginatedResponse**](InvoiceGroupPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to get invoice group request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_invoice_group_accounts**
> BaseSuccessResponse remove_invoice_group_accounts(invoice_group_id, update_invoice_group_accounts)

Remove accounts from an invoice group. Removing all accounts will also delete the invoice group

This API let’s you to remove accounts from an invoice group. Removing all accounts will also delete the invoice group

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.models.update_invoice_group_accounts import UpdateInvoiceGroupAccounts
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
    api_instance = togai_client.InvoiceGroupsApi(api_client)
    invoice_group_id = 'inv_grp.20rqjgFJf2O.ejl25' # str | 
    update_invoice_group_accounts = togai_client.UpdateInvoiceGroupAccounts() # UpdateInvoiceGroupAccounts | Payload to add or remove accounts to/from an invoice group

    try:
        # Remove accounts from an invoice group. Removing all accounts will also delete the invoice group
        api_response = api_instance.remove_invoice_group_accounts(invoice_group_id, update_invoice_group_accounts)
        print("The response of InvoiceGroupsApi->remove_invoice_group_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceGroupsApi->remove_invoice_group_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_group_id** | **str**|  | 
 **update_invoice_group_accounts** | [**UpdateInvoiceGroupAccounts**](UpdateInvoiceGroupAccounts.md)| Payload to add or remove accounts to/from an invoice group | 

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
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

