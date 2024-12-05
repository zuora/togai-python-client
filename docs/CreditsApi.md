# togai_client.CreditsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit**](CreditsApi.md#create_credit) | **POST** /credits | Grant credit
[**credit_balance_for_account**](CreditsApi.md#credit_balance_for_account) | **GET** /accounts/{account_id}/credit_balance | Credit balance for Account
[**get_credit_details**](CreditsApi.md#get_credit_details) | **GET** /credits/{credit_id} | Get credit details
[**list_credits**](CreditsApi.md#list_credits) | **GET** /credits | List credits
[**void_credit**](CreditsApi.md#void_credit) | **POST** /credits/{credit_id}/void | Void credit


# **create_credit**
> CreateCreditResponse create_credit(create_credit_request=create_credit_request)

Grant credit

Grant credit

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_credit_request import CreateCreditRequest
from togai_client.models.create_credit_response import CreateCreditResponse
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
    api_instance = togai_client.CreditsApi(api_client)
    create_credit_request = togai_client.CreateCreditRequest() # CreateCreditRequest | Payload to grant credits (optional)

    try:
        # Grant credit
        api_response = api_instance.create_credit(create_credit_request=create_credit_request)
        print("The response of CreditsApi->create_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->create_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_request** | [**CreateCreditRequest**](CreateCreditRequest.md)| Payload to grant credits | [optional] 

### Return type

[**CreateCreditResponse**](CreateCreditResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for List credits request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_balance_for_account**
> CreditBalanceResponse credit_balance_for_account(account_id)

Credit balance for Account

Credit balance for Account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.credit_balance_response import CreditBalanceResponse
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
    api_instance = togai_client.CreditsApi(api_client)
    account_id = 'ACC00001' # str | account_id corresponding to an account

    try:
        # Credit balance for Account
        api_response = api_instance.credit_balance_for_account(account_id)
        print("The response of CreditsApi->credit_balance_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->credit_balance_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account_id corresponding to an account | 

### Return type

[**CreditBalanceResponse**](CreditBalanceResponse.md)

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

# **get_credit_details**
> CreditDetailsResponse get_credit_details(credit_id)

Get credit details

Get credit details

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.credit_details_response import CreditDetailsResponse
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
    api_instance = togai_client.CreditsApi(api_client)
    credit_id = 'creds.1znQx9jiIXw.r44fc' # str | 

    try:
        # Get credit details
        api_response = api_instance.get_credit_details(credit_id)
        print("The response of CreditsApi->get_credit_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_credit_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | **str**|  | 

### Return type

[**CreditDetailsResponse**](CreditDetailsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Fetch Credit Details request. This contains Credit Transactions |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credits**
> ListCreditsResponse list_credits(next_token=next_token, status=status, account_id=account_id, id=id, page_size=page_size)

List credits

Get all credits

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.list_credits_response import ListCreditsResponse
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
    api_instance = togai_client.CreditsApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==' # str | Pagination token used as a marker to get records from next page. (optional)
    status = 'PROCESSED' # str | Filter option to filter by status. (optional)
    account_id = '1234' # str | Filter option to filter based on account id. (optional)
    id = 'cred.1znpoFlsI3U.zmg85' # str | Filter option to filter based on credit id. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)

    try:
        # List credits
        api_response = api_instance.list_credits(next_token=next_token, status=status, account_id=account_id, id=id, page_size=page_size)
        print("The response of CreditsApi->list_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->list_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional] 
 **status** | **str**| Filter option to filter by status. | [optional] 
 **account_id** | **str**| Filter option to filter based on account id. | [optional] 
 **id** | **str**| Filter option to filter based on credit id. | [optional] 
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional] 

### Return type

[**ListCreditsResponse**](ListCreditsResponse.md)

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

# **void_credit**
> Credit void_credit(credit_id)

Void credit

Void credit

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.credit import Credit
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
    api_instance = togai_client.CreditsApi(api_client)
    credit_id = 'creds.1znQx9jiIXw.r44fc' # str | 

    try:
        # Void credit
        api_response = api_instance.void_credit(credit_id)
        print("The response of CreditsApi->void_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->void_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | **str**|  | 

### Return type

[**Credit**](Credit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Void credit request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

