# togai_client.WalletApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**top_up_wallet_for_account**](WalletApi.md#top_up_wallet_for_account) | **POST** /accounts/{account_id}/wallet_topup | Top-up wallet for an account
[**update_wallet_for_account**](WalletApi.md#update_wallet_for_account) | **PATCH** /accounts/{account_id}/wallet | Update wallet details for an account
[**wallet_balance_for_account**](WalletApi.md#wallet_balance_for_account) | **GET** /accounts/{account_id}/wallet | Wallet balance for Account
[**wallet_entries_for_account**](WalletApi.md#wallet_entries_for_account) | **GET** /accounts/{account_id}/wallet/entries | Wallet entries for Account


# **top_up_wallet_for_account**
> WalletBalanceResponse top_up_wallet_for_account(account_id, topup_wallet_request=topup_wallet_request)

Top-up wallet for an account

Top-up wallet for an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.topup_wallet_request import TopupWalletRequest
from togai_client.models.wallet_balance_response import WalletBalanceResponse
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
    api_instance = togai_client.WalletApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    topup_wallet_request = togai_client.TopupWalletRequest() # TopupWalletRequest | Payload to topup wallet of an account (optional)

    try:
        # Top-up wallet for an account
        api_response = api_instance.top_up_wallet_for_account(account_id, topup_wallet_request=topup_wallet_request)
        print("The response of WalletApi->top_up_wallet_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->top_up_wallet_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **topup_wallet_request** | [**TopupWalletRequest**](TopupWalletRequest.md)| Payload to topup wallet of an account | [optional] 

### Return type

[**WalletBalanceResponse**](WalletBalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Credit Balance Request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wallet_for_account**
> WalletBalanceResponse update_wallet_for_account(account_id, update_wallet_request=update_wallet_request)

Update wallet details for an account

Update wallet details for an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.update_wallet_request import UpdateWalletRequest
from togai_client.models.wallet_balance_response import WalletBalanceResponse
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
    api_instance = togai_client.WalletApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    update_wallet_request = togai_client.UpdateWalletRequest() # UpdateWalletRequest | Payload to update wallet of an account (optional)

    try:
        # Update wallet details for an account
        api_response = api_instance.update_wallet_for_account(account_id, update_wallet_request=update_wallet_request)
        print("The response of WalletApi->update_wallet_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->update_wallet_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **update_wallet_request** | [**UpdateWalletRequest**](UpdateWalletRequest.md)| Payload to update wallet of an account | [optional] 

### Return type

[**WalletBalanceResponse**](WalletBalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Credit Balance Request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_balance_for_account**
> WalletBalanceResponse wallet_balance_for_account(account_id)

Wallet balance for Account

Wallet balance for Account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.wallet_balance_response import WalletBalanceResponse
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
    api_instance = togai_client.WalletApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # Wallet balance for Account
        api_response = api_instance.wallet_balance_for_account(account_id)
        print("The response of WalletApi->wallet_balance_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_balance_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

### Return type

[**WalletBalanceResponse**](WalletBalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Credit Balance Request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_entries_for_account**
> WalletEntriesPaginatedResponse wallet_entries_for_account(account_id, next_token=next_token, page_size=page_size)

Wallet entries for Account

Wallet entries for Account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.wallet_entries_paginated_response import WalletEntriesPaginatedResponse
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
    api_instance = togai_client.WalletApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)

    try:
        # Wallet entries for Account
        api_response = api_instance.wallet_entries_for_account(account_id, next_token=next_token, page_size=page_size)
        print("The response of WalletApi->wallet_entries_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_entries_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 

### Return type

[**WalletEntriesPaginatedResponse**](WalletEntriesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Credit Balance Request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

