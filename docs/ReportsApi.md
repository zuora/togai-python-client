# togai_client.ReportsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_reports**](ReportsApi.md#list_reports) | **GET** /reports | List reports


# **list_reports**
> ReportsPaginatedResponse list_reports(next_token=next_token, page_size=page_size, fetch_for=fetch_for)

List reports

List reports

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.reports_paginated_response import ReportsPaginatedResponse
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
    api_instance = togai_client.ReportsApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)
    fetch_for = ORGANIZATION # str | Fetch for flag used to get the reports from: 1. ALL: Both the organization and accounts 2. ORGANIZATION: Only the organization 3. ACCOUNTS: Only accounts, works with account_id filter only.  (optional) (default to ORGANIZATION)

    try:
        # List reports
        api_response = api_instance.list_reports(next_token=next_token, page_size=page_size, fetch_for=fetch_for)
        print("The response of ReportsApi->list_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->list_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **fetch_for** | **str**| Fetch for flag used to get the reports from: 1. ALL: Both the organization and accounts 2. ORGANIZATION: Only the organization 3. ACCOUNTS: Only accounts, works with account_id filter only.  | [optional] [default to ORGANIZATION]

### Return type

[**ReportsPaginatedResponse**](ReportsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for List Report requests |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

