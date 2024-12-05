# togai_client.InvoicesApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_invoice**](InvoicesApi.md#create_custom_invoice) | **POST** /invoices | Create a custom invoice for an account
[**create_invoice_bill_run**](InvoicesApi.md#create_invoice_bill_run) | **POST** /invoices/bill_runs | Create a bill run job request
[**delete_custom_invoice**](InvoicesApi.md#delete_custom_invoice) | **DELETE** /invoices/{invoice_id} | Delete a custom invoice in DRAFT state
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /invoices/{invoice_id} | Get an invoice
[**list_invoices**](InvoicesApi.md#list_invoices) | **GET** /invoices | List invoices
[**list_invoices_for_bill_run**](InvoicesApi.md#list_invoices_for_bill_run) | **GET** /invoices/bill_runs | List invoices eligible for bill run
[**list_pricing_rule_logs**](InvoicesApi.md#list_pricing_rule_logs) | **GET** /invoice/{invoice_id}/pricing_rules_logs | List pricing rule logs
[**manage_miscellaneous_charges_in_account**](InvoicesApi.md#manage_miscellaneous_charges_in_account) | **PUT** /accounts/{account_id}/miscellaneous_charges | Add or update miscellaneous charges in upcoming Invoice for a account
[**manage_miscellaneous_charges_in_invoice**](InvoicesApi.md#manage_miscellaneous_charges_in_invoice) | **PUT** /invoices/{invoice_id}/miscellaneous_charges | Add or update miscellaneous charges in Invoice
[**update_invoice**](InvoicesApi.md#update_invoice) | **PATCH** /invoices/{invoice_id} | Update an invoice


# **create_custom_invoice**
> Invoice create_custom_invoice(create_custom_invoice_request=create_custom_invoice_request)

Create a custom invoice for an account

Create a custom invoice for an account.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_custom_invoice_request import CreateCustomInvoiceRequest
from togai_client.models.invoice import Invoice
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
    api_instance = togai_client.InvoicesApi(api_client)
    create_custom_invoice_request = togai_client.CreateCustomInvoiceRequest() # CreateCustomInvoiceRequest | Payload to create invoice (optional)

    try:
        # Create a custom invoice for an account
        api_response = api_instance.create_custom_invoice(create_custom_invoice_request=create_custom_invoice_request)
        print("The response of InvoicesApi->create_custom_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_custom_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_invoice_request** | [**CreateCustomInvoiceRequest**](CreateCustomInvoiceRequest.md)| Payload to create invoice | [optional] 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Get invoice requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_bill_run**
> BaseSuccessResponse create_invoice_bill_run(require_confirmation=require_confirmation)

Create a bill run job request

Create a bill run job request

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
    api_instance = togai_client.InvoicesApi(api_client)
    require_confirmation = false # bool | Specifies whether to start a migration only after a confirmation (optional)

    try:
        # Create a bill run job request
        api_response = api_instance.create_invoice_bill_run(require_confirmation=require_confirmation)
        print("The response of InvoicesApi->create_invoice_bill_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_invoice_bill_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **require_confirmation** | **bool**| Specifies whether to start a migration only after a confirmation | [optional] 

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

# **delete_custom_invoice**
> BaseSuccessResponse delete_custom_invoice(invoice_id)

Delete a custom invoice in DRAFT state

Delete a custom invoice in DRAFT state.

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
    api_instance = togai_client.InvoicesApi(api_client)
    invoice_id = 'ACC001' # str | 

    try:
        # Delete a custom invoice in DRAFT state
        api_response = api_instance.delete_custom_invoice(invoice_id)
        print("The response of InvoicesApi->delete_custom_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->delete_custom_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> Invoice get_invoice(invoice_id)

Get an invoice

Get invoice

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.invoice import Invoice
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
    api_instance = togai_client.InvoicesApi(api_client)
    invoice_id = 'ACC001' # str | 

    try:
        # Get an invoice
        api_response = api_instance.get_invoice(invoice_id)
        print("The response of InvoicesApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Get invoice requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> ListInvoicesResponse list_invoices(next_token=next_token, status=status, owner_id=owner_id, customer_id=customer_id, page_size=page_size, start_time=start_time, end_time=end_time)

List invoices

List invoices

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.list_invoices_response import ListInvoicesResponse
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
    api_instance = togai_client.InvoicesApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)
    status = 'PROCESSED' # str | Filter option to filter by status. (optional)
    owner_id = 'ACC001' # str | Filter option to filter based on owner id. (optional)
    customer_id = '1234' # str | Filter option to filter based on customer id. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)
    start_time = 1650110402000 # int | Start time filter in epoch milli seconds (optional)
    end_time = 1650110402000 # int | End time filter in epoch milli seconds (optional)

    try:
        # List invoices
        api_response = api_instance.list_invoices(next_token=next_token, status=status, owner_id=owner_id, customer_id=customer_id, page_size=page_size, start_time=start_time, end_time=end_time)
        print("The response of InvoicesApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 
 **status** | **str**| Filter option to filter by status. | [optional] 
 **owner_id** | **str**| Filter option to filter based on owner id. | [optional] 
 **customer_id** | **str**| Filter option to filter based on customer id. | [optional] 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 
 **start_time** | **int**| Start time filter in epoch milli seconds | [optional] 
 **end_time** | **int**| End time filter in epoch milli seconds | [optional] 

### Return type

[**ListInvoicesResponse**](ListInvoicesResponse.md)

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
**403** | Credential does not have access to this operation. |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices_for_bill_run**
> ListInvoicesResponse list_invoices_for_bill_run(next_token=next_token, status=status, owner_id=owner_id, customer_id=customer_id, page_size=page_size, start_time=start_time, end_time=end_time)

List invoices eligible for bill run

List invoices eligible for bill run

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.list_invoices_response import ListInvoicesResponse
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
    api_instance = togai_client.InvoicesApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)
    status = 'PROCESSED' # str | Filter option to filter by status. (optional)
    owner_id = 'ACC001' # str | Filter option to filter based on owner id. (optional)
    customer_id = '1234' # str | Filter option to filter based on customer id. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)
    start_time = 1650110402000 # int | Start time filter in epoch milli seconds (optional)
    end_time = 1650110402000 # int | End time filter in epoch milli seconds (optional)

    try:
        # List invoices eligible for bill run
        api_response = api_instance.list_invoices_for_bill_run(next_token=next_token, status=status, owner_id=owner_id, customer_id=customer_id, page_size=page_size, start_time=start_time, end_time=end_time)
        print("The response of InvoicesApi->list_invoices_for_bill_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->list_invoices_for_bill_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 
 **status** | **str**| Filter option to filter by status. | [optional] 
 **owner_id** | **str**| Filter option to filter based on owner id. | [optional] 
 **customer_id** | **str**| Filter option to filter based on customer id. | [optional] 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 
 **start_time** | **int**| Start time filter in epoch milli seconds | [optional] 
 **end_time** | **int**| End time filter in epoch milli seconds | [optional] 

### Return type

[**ListInvoicesResponse**](ListInvoicesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Get invoice requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pricing_rule_logs**
> PricingRulesLogsPaginatedResponse list_pricing_rule_logs(invoice_id)

List pricing rule logs

List pricing rule logs

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.pricing_rules_logs_paginated_response import PricingRulesLogsPaginatedResponse
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
    api_instance = togai_client.InvoicesApi(api_client)
    invoice_id = 'ACC001' # str | 

    try:
        # List pricing rule logs
        api_response = api_instance.list_pricing_rule_logs(invoice_id)
        print("The response of InvoicesApi->list_pricing_rule_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->list_pricing_rule_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**PricingRulesLogsPaginatedResponse**](PricingRulesLogsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list Invoice Pricing Rules Logs Request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_miscellaneous_charges_in_account**
> MiscellaneousChargesResponse manage_miscellaneous_charges_in_account(account_id, manage_miscellaneous_charges_request=manage_miscellaneous_charges_request)

Add or update miscellaneous charges in upcoming Invoice for a account

Add or update miscellaneous charges in upcoming Invoice for a account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.manage_miscellaneous_charges_request import ManageMiscellaneousChargesRequest
from togai_client.models.miscellaneous_charges_response import MiscellaneousChargesResponse
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
    api_instance = togai_client.InvoicesApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    manage_miscellaneous_charges_request = togai_client.ManageMiscellaneousChargesRequest() # ManageMiscellaneousChargesRequest | Payload to update custom line items (optional)

    try:
        # Add or update miscellaneous charges in upcoming Invoice for a account
        api_response = api_instance.manage_miscellaneous_charges_in_account(account_id, manage_miscellaneous_charges_request=manage_miscellaneous_charges_request)
        print("The response of InvoicesApi->manage_miscellaneous_charges_in_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->manage_miscellaneous_charges_in_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **manage_miscellaneous_charges_request** | [**ManageMiscellaneousChargesRequest**](ManageMiscellaneousChargesRequest.md)| Payload to update custom line items | [optional] 

### Return type

[**MiscellaneousChargesResponse**](MiscellaneousChargesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Miscellaneous Charges Request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_miscellaneous_charges_in_invoice**
> MiscellaneousChargesResponse manage_miscellaneous_charges_in_invoice(invoice_id, manage_miscellaneous_charges_request=manage_miscellaneous_charges_request)

Add or update miscellaneous charges in Invoice

Add or update miscellaneous charges in Invoice

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.manage_miscellaneous_charges_request import ManageMiscellaneousChargesRequest
from togai_client.models.miscellaneous_charges_response import MiscellaneousChargesResponse
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
    api_instance = togai_client.InvoicesApi(api_client)
    invoice_id = 'ACC001' # str | 
    manage_miscellaneous_charges_request = togai_client.ManageMiscellaneousChargesRequest() # ManageMiscellaneousChargesRequest | Payload to update custom line items (optional)

    try:
        # Add or update miscellaneous charges in Invoice
        api_response = api_instance.manage_miscellaneous_charges_in_invoice(invoice_id, manage_miscellaneous_charges_request=manage_miscellaneous_charges_request)
        print("The response of InvoicesApi->manage_miscellaneous_charges_in_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->manage_miscellaneous_charges_in_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **manage_miscellaneous_charges_request** | [**ManageMiscellaneousChargesRequest**](ManageMiscellaneousChargesRequest.md)| Payload to update custom line items | [optional] 

### Return type

[**MiscellaneousChargesResponse**](MiscellaneousChargesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Miscellaneous Charges Request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> Invoice update_invoice(invoice_id, update_invoice_request=update_invoice_request)

Update an invoice

Update an invoice[Only CUSTOM invoices in DRAFT state support updating of all fields]. Updating status can be done for all invoice.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.invoice import Invoice
from togai_client.models.update_invoice_request import UpdateInvoiceRequest
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
    api_instance = togai_client.InvoicesApi(api_client)
    invoice_id = 'ACC001' # str | 
    update_invoice_request = togai_client.UpdateInvoiceRequest() # UpdateInvoiceRequest | Payload to update an invoice (optional)

    try:
        # Update an invoice
        api_response = api_instance.update_invoice(invoice_id, update_invoice_request=update_invoice_request)
        print("The response of InvoicesApi->update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **update_invoice_request** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)| Payload to update an invoice | [optional] 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Get invoice requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

