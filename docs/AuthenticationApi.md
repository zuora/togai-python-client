# togai_client.AuthenticationApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /authenticate | Generate short lived bearer token


# **authenticate**
> TokenResponse authenticate()

Generate short lived bearer token

Generates and returns a bearer token. Behavior of this API differs on the basis of the auth mechanism used to make the request.   - For API key auth, this API generates a JWT token whcih is valid for 24 hours and returns it.   - For JWT bearer auth, returns the same JWT token in response For information on how to generate API token, refer [Generating New API Keys](https://docs.togai.com/api-reference/authentication#generating-new-api-keys) section of docs. 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
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
    api_instance = togai_client.AuthenticationApi(api_client)

    try:
        # Generate short lived bearer token
        api_response = api_instance.authenticate()
        print("The response of AuthenticationApi->authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenResponse**](TokenResponse.md)

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

