# togai_client.CustomerPortalApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_portal_delegate_token**](CustomerPortalApi.md#get_customer_portal_delegate_token) | **POST** /portal/token | Get delegate token for customer portal


# **get_customer_portal_delegate_token**
> TokenResponse get_customer_portal_delegate_token(get_customer_portal_delegate_token_request)

Get delegate token for customer portal

Get delegate token for customer portal

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_customer_portal_delegate_token_request import GetCustomerPortalDelegateTokenRequest
from togai_client.models.token_response import TokenResponse
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
    api_instance = togai_client.CustomerPortalApi(api_client)
    get_customer_portal_delegate_token_request = togai_client.GetCustomerPortalDelegateTokenRequest() # GetCustomerPortalDelegateTokenRequest | Payload to get delegate token for customer portal

    try:
        # Get delegate token for customer portal
        api_response = api_instance.get_customer_portal_delegate_token(get_customer_portal_delegate_token_request)
        print("The response of CustomerPortalApi->get_customer_portal_delegate_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerPortalApi->get_customer_portal_delegate_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_customer_portal_delegate_token_request** | [**GetCustomerPortalDelegateTokenRequest**](GetCustomerPortalDelegateTokenRequest.md)| Payload to get delegate token for customer portal | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

