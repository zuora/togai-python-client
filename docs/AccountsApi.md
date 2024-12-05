# togai_client.AccountsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_aliases**](AccountsApi.md#add_aliases) | **POST** /accounts/{account_id}/add_aliases | Add Aliases to account
[**create_account**](AccountsApi.md#create_account) | **POST** /accounts | Create an account
[**create_proposal**](AccountsApi.md#create_proposal) | **POST** /accounts/{account_id}/purchase_proposals | (DEPRECATED) Propose a purchase of a plan
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /accounts/{account_id} | Delete an account
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{account_id} | Get an account
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /accounts | List accounts of customer
[**get_pricing_schedules**](AccountsApi.md#get_pricing_schedules) | **GET** /accounts/{account_id}/pricing_schedules | (DEPRECATED) List pricing schedules of an account
[**get_proposal**](AccountsApi.md#get_proposal) | **GET** /purchase_proposals/{purchase_proposal_id} | (DEPRECATED) Get proposal information
[**get_purchase**](AccountsApi.md#get_purchase) | **GET** /purchases/{purchase_id} | (DEPRECATED) Get a specific purchase of an account
[**initiate_one_time_entitlement_plan**](AccountsApi.md#initiate_one_time_entitlement_plan) | **POST** /accounts/{account_id}/purchases | (DEPRECATED) Initiate a purchase
[**list_account_aliases**](AccountsApi.md#list_account_aliases) | **GET** /accounts/{account_id}/account_aliases | Get all aliases of an account
[**list_account_proposals**](AccountsApi.md#list_account_proposals) | **GET** /accounts/{account_id}/purchase_proposals | (DEPRECATED) List all proposals of an account
[**list_account_purchases**](AccountsApi.md#list_account_purchases) | **GET** /accounts/{account_id}/purchases | (DEPRECATED) Get all purchases for an account
[**remove_aliases**](AccountsApi.md#remove_aliases) | **POST** /accounts/{account_id}/remove_aliases | Remove Aliases to account
[**update_account**](AccountsApi.md#update_account) | **PATCH** /accounts/{account_id} | Update an account
[**update_pricing_schedule**](AccountsApi.md#update_pricing_schedule) | **POST** /accounts/{account_id}/price_plans | (DEPRECATED) Dissociate or associate a price plan with an account
[**update_pricing_schedule_batch**](AccountsApi.md#update_pricing_schedule_batch) | **POST** /accounts/{account_id}/edit_schedules | (DEPRECATED) Edit schedules of an account.
[**update_proposal_status**](AccountsApi.md#update_proposal_status) | **POST** /purchase_proposals/{purchase_proposal_id}/update_status | (DEPRECATED) Approve or decline a purchase of a billing plan


# **add_aliases**
> Account add_aliases(account_id, add_account_aliases_request)

Add Aliases to account

Add aliases to an account using customer_id and account_id.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account import Account
from togai_client.models.add_account_aliases_request import AddAccountAliasesRequest
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    add_account_aliases_request = togai_client.AddAccountAliasesRequest() # AddAccountAliasesRequest | Payload to add aliases to account

    try:
        # Add Aliases to account
        api_response = api_instance.add_aliases(account_id, add_account_aliases_request)
        print("The response of AccountsApi->add_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->add_aliases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **add_account_aliases_request** | [**AddAccountAliasesRequest**](AddAccountAliasesRequest.md)| Payload to add aliases to account | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> Account create_account(create_account_request)

Create an account

This API let’s you to create an account for a customer using customer_id.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account import Account
from togai_client.models.create_account_request import CreateAccountRequest
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
    api_instance = togai_client.AccountsApi(api_client)
    create_account_request = togai_client.CreateAccountRequest() # CreateAccountRequest | Payload to create account

    try:
        # Create an account
        api_response = api_instance.create_account(create_account_request)
        print("The response of AccountsApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)| Payload to create account | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proposal**
> Proposal create_proposal(account_id, create_proposal_request)

(DEPRECATED) Propose a purchase of a plan

This API let’s you to create a proposal of a billing/entitlement plan for an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_proposal_request import CreateProposalRequest
from togai_client.models.proposal import Proposal
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    create_proposal_request = togai_client.CreateProposalRequest() # CreateProposalRequest | Payload to initiate a proposal

    try:
        # (DEPRECATED) Propose a purchase of a plan
        api_response = api_instance.create_proposal(account_id, create_proposal_request)
        print("The response of AccountsApi->create_proposal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_proposal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **create_proposal_request** | [**CreateProposalRequest**](CreateProposalRequest.md)| Payload to initiate a proposal | 

### Return type

[**Proposal**](Proposal.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to create proposal request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> BaseSuccessResponse delete_account(account_id)

Delete an account

This API let’s you to delete a customer using customer_id and account_id.

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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # Delete an account
        api_response = api_instance.delete_account(account_id)
        print("The response of AccountsApi->delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_account: %s\n" % e)
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
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(account_id, effective_on=effective_on, include_group_details=include_group_details)

Get an account

Get account information using customer_id and account_id.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account import Account
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    effective_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    include_group_details = true # bool |  (optional)

    try:
        # Get an account
        api_response = api_instance.get_account(account_id, effective_on=effective_on, include_group_details=include_group_details)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **effective_on** | **datetime**|  | [optional] 
 **include_group_details** | **bool**|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountPaginatedResponse get_accounts(next_token=next_token, page_size=page_size)

List accounts of customer

Returns a list of accounts of a customer with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account_paginated_response import AccountPaginatedResponse
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
    api_instance = togai_client.AccountsApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List accounts of customer
        api_response = api_instance.get_accounts(next_token=next_token, page_size=page_size)
        print("The response of AccountsApi->get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**AccountPaginatedResponse**](AccountPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list customers request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_schedules**
> PricingSchedulePaginatedResponse get_pricing_schedules(account_id, next_token=next_token, page_size=page_size, start_date=start_date, end_date=end_date, include_price_plan_info=include_price_plan_info, compact=compact)

(DEPRECATED) List pricing schedules of an account

Returns a list of pricing schedules of an account with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.pricing_schedule_paginated_response import PricingSchedulePaginatedResponse
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)
    start_date = '2023-03-30T10:41:10.088499' # str |  (optional)
    end_date = '2099-03-30T10:41:10.088499' # str |  (optional)
    include_price_plan_info = true # bool |  (optional)
    compact = false # bool |  (optional)

    try:
        # (DEPRECATED) List pricing schedules of an account
        api_response = api_instance.get_pricing_schedules(account_id, next_token=next_token, page_size=page_size, start_date=start_date, end_date=end_date, include_price_plan_info=include_price_plan_info, compact=compact)
        print("The response of AccountsApi->get_pricing_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_pricing_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **include_price_plan_info** | **bool**|  | [optional] 
 **compact** | **bool**|  | [optional] 

### Return type

[**PricingSchedulePaginatedResponse**](PricingSchedulePaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list pricing schedules request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proposal**
> GetProposalResponse get_proposal(purchase_proposal_id)

(DEPRECATED) Get proposal information

Get proposal information

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_proposal_response import GetProposalResponse
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
    api_instance = togai_client.AccountsApi(api_client)
    purchase_proposal_id = 'purchase.20rqjgFJf2O.ejl25' # str | 

    try:
        # (DEPRECATED) Get proposal information
        api_response = api_instance.get_proposal(purchase_proposal_id)
        print("The response of AccountsApi->get_proposal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_proposal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_proposal_id** | **str**|  | 

### Return type

[**GetProposalResponse**](GetProposalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for getting a specific proposal |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase**
> GetPurchaseResponse get_purchase(purchase_id)

(DEPRECATED) Get a specific purchase of an account

Get purchase information of an account for a specific plan using account_id and price_plan_id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_purchase_response import GetPurchaseResponse
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
    api_instance = togai_client.AccountsApi(api_client)
    purchase_id = 'purchase.1zYnCiM9Bpg.lv25y' # str | 

    try:
        # (DEPRECATED) Get a specific purchase of an account
        api_response = api_instance.get_purchase(purchase_id)
        print("The response of AccountsApi->get_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **str**|  | 

### Return type

[**GetPurchaseResponse**](GetPurchaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for getting a specific purchase detail of an account |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_one_time_entitlement_plan**
> Purchase initiate_one_time_entitlement_plan(account_id, create_purchase_request)

(DEPRECATED) Initiate a purchase

This API let’s you to initiate a purchase for an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_purchase_request import CreatePurchaseRequest
from togai_client.models.purchase import Purchase
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    create_purchase_request = togai_client.CreatePurchaseRequest() # CreatePurchaseRequest | Payload to initiate a purchase

    try:
        # (DEPRECATED) Initiate a purchase
        api_response = api_instance.initiate_one_time_entitlement_plan(account_id, create_purchase_request)
        print("The response of AccountsApi->initiate_one_time_entitlement_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->initiate_one_time_entitlement_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **create_purchase_request** | [**CreatePurchaseRequest**](CreatePurchaseRequest.md)| Payload to initiate a purchase | 

### Return type

[**Purchase**](Purchase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for initiation of a purchase of entitlement plan for an account |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_aliases**
> AccountAliasesPaginatedResponse list_account_aliases(account_id)

Get all aliases of an account

Get all aliases of an account using account_id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account_aliases_paginated_response import AccountAliasesPaginatedResponse
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # Get all aliases of an account
        api_response = api_instance.list_account_aliases(account_id)
        print("The response of AccountsApi->list_account_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_aliases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

### Return type

[**AccountAliasesPaginatedResponse**](AccountAliasesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list account aliases request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_proposals**
> ProposalsPaginatedResponse list_account_proposals(account_id)

(DEPRECATED) List all proposals of an account

List all proposals of an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.proposals_paginated_response import ProposalsPaginatedResponse
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # (DEPRECATED) List all proposals of an account
        api_response = api_instance.list_account_proposals(account_id)
        print("The response of AccountsApi->list_account_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

### Return type

[**ProposalsPaginatedResponse**](ProposalsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list proposals of an account request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_purchases**
> PurchasePaginatedListData list_account_purchases(account_id)

(DEPRECATED) Get all purchases for an account

Get Purchase information for an account using account_id and price_plan_id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.purchase_paginated_list_data import PurchasePaginatedListData
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # (DEPRECATED) Get all purchases for an account
        api_response = api_instance.list_account_purchases(account_id)
        print("The response of AccountsApi->list_account_purchases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_purchases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

### Return type

[**PurchasePaginatedListData**](PurchasePaginatedListData.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list Purchase for an account request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_aliases**
> Account remove_aliases(account_id, remove_account_aliases_request)

Remove Aliases to account

Remove existing aliases tagged to an account using this API

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account import Account
from togai_client.models.remove_account_aliases_request import RemoveAccountAliasesRequest
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    remove_account_aliases_request = togai_client.RemoveAccountAliasesRequest() # RemoveAccountAliasesRequest | Payload to remove aliases from account

    try:
        # Remove Aliases to account
        api_response = api_instance.remove_aliases(account_id, remove_account_aliases_request)
        print("The response of AccountsApi->remove_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->remove_aliases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **remove_account_aliases_request** | [**RemoveAccountAliasesRequest**](RemoveAccountAliasesRequest.md)| Payload to remove aliases from account | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> Account update_account(account_id, update_account_request)

Update an account

This API let’s you to update an account’s information using customer_id and account_id.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.account import Account
from togai_client.models.update_account_request import UpdateAccountRequest
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    update_account_request = togai_client.UpdateAccountRequest() # UpdateAccountRequest | Payload to update account

    try:
        # Update an account
        api_response = api_instance.update_account(account_id, update_account_request)
        print("The response of AccountsApi->update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **update_account_request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)| Payload to update account | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_schedule**
> UpdatePricingScheduleResponse update_pricing_schedule(account_id, update_pricing_schedule_request_with_actions)

(DEPRECATED) Dissociate or associate a price plan with an account

This API let’s you to detach or attach a price plan with an existing account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.update_pricing_schedule_request_with_actions import UpdatePricingScheduleRequestWithActions
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    update_pricing_schedule_request_with_actions = togai_client.UpdatePricingScheduleRequestWithActions() # UpdatePricingScheduleRequestWithActions | Payload to associate or dissociate a price plan to an account with actions

    try:
        # (DEPRECATED) Dissociate or associate a price plan with an account
        api_response = api_instance.update_pricing_schedule(account_id, update_pricing_schedule_request_with_actions)
        print("The response of AccountsApi->update_pricing_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_pricing_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **update_pricing_schedule_request_with_actions** | [**UpdatePricingScheduleRequestWithActions**](UpdatePricingScheduleRequestWithActions.md)| Payload to associate or dissociate a price plan to an account with actions | 

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
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_schedule_batch**
> UpdatePricingScheduleResponse update_pricing_schedule_batch(account_id, edit_pricing_schedule_request, dry_run=dry_run)

(DEPRECATED) Edit schedules of an account.

This API let’s you to detach/attach one or more price plans from/to an existing account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.edit_pricing_schedule_request import EditPricingScheduleRequest
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
    api_instance = togai_client.AccountsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    edit_pricing_schedule_request = togai_client.EditPricingScheduleRequest() # EditPricingScheduleRequest | Payload to dis/associate one or more price plans to an account
    dry_run = false # bool |  (optional)

    try:
        # (DEPRECATED) Edit schedules of an account.
        api_response = api_instance.update_pricing_schedule_batch(account_id, edit_pricing_schedule_request, dry_run=dry_run)
        print("The response of AccountsApi->update_pricing_schedule_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_pricing_schedule_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **edit_pricing_schedule_request** | [**EditPricingScheduleRequest**](EditPricingScheduleRequest.md)| Payload to dis/associate one or more price plans to an account | 
 **dry_run** | **bool**|  | [optional] 

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
**200** | Response for edit pricing schedule request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proposal_status**
> Proposal update_proposal_status(purchase_proposal_id, update_proposal_status)

(DEPRECATED) Approve or decline a purchase of a billing plan

This API let’s you to approve or decline a proposal of a billing plan for an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.proposal import Proposal
from togai_client.models.update_proposal_status import UpdateProposalStatus
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
    api_instance = togai_client.AccountsApi(api_client)
    purchase_proposal_id = 'purchase.20rqjgFJf2O.ejl25' # str | 
    update_proposal_status = togai_client.UpdateProposalStatus() # UpdateProposalStatus | Payload to approve or decline a proposal

    try:
        # (DEPRECATED) Approve or decline a purchase of a billing plan
        api_response = api_instance.update_proposal_status(purchase_proposal_id, update_proposal_status)
        print("The response of AccountsApi->update_proposal_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_proposal_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_proposal_id** | **str**|  | 
 **update_proposal_status** | [**UpdateProposalStatus**](UpdateProposalStatus.md)| Payload to approve or decline a proposal | 

### Return type

[**Proposal**](Proposal.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to update proposal status request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

