# togai_client.JobsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_job**](JobsApi.md#confirm_job) | **POST** /jobs/{job_id}/confirm | Confirm a job
[**get_job_entries**](JobsApi.md#get_job_entries) | **GET** /jobs/{job_id}/entries | List job entries
[**get_job_status**](JobsApi.md#get_job_status) | **GET** /jobs/{job_id} | Get the status of a job
[**get_jobs**](JobsApi.md#get_jobs) | **GET** /jobs | List jobs
[**reject_job**](JobsApi.md#reject_job) | **POST** /jobs/{job_id}/reject | Reject a job


# **confirm_job**
> GetJobResponse confirm_job(job_id)

Confirm a job

Confirm a job

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_job_response import GetJobResponse
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
    api_instance = togai_client.JobsApi(api_client)
    job_id = 'mig.20aUyEZSuYq.SoGbS' # str | 

    try:
        # Confirm a job
        api_response = api_instance.confirm_job(job_id)
        print("The response of JobsApi->confirm_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->confirm_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**GetJobResponse**](GetJobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for get job status request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_entries**
> JobEntriesPaginatedResponse get_job_entries(job_id)

List job entries

List individual job entries and current state of processing

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.job_entries_paginated_response import JobEntriesPaginatedResponse
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
    api_instance = togai_client.JobsApi(api_client)
    job_id = 'mig.20aUyEZSuYq.SoGbS' # str | 

    try:
        # List job entries
        api_response = api_instance.get_job_entries(job_id)
        print("The response of JobsApi->get_job_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**JobEntriesPaginatedResponse**](JobEntriesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list job entries request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_status**
> GetJobResponse get_job_status(job_id)

Get the status of a job

Get the status of a job

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_job_response import GetJobResponse
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
    api_instance = togai_client.JobsApi(api_client)
    job_id = 'mig.20aUyEZSuYq.SoGbS' # str | 

    try:
        # Get the status of a job
        api_response = api_instance.get_job_status(job_id)
        print("The response of JobsApi->get_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**GetJobResponse**](GetJobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for get job status request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> JobsPaginatedResponse get_jobs(next_token=next_token, page_size=page_size)

List jobs

Returns a list of jobs with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.jobs_paginated_response import JobsPaginatedResponse
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
    api_instance = togai_client.JobsApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List jobs
        api_response = api_instance.get_jobs(next_token=next_token, page_size=page_size)
        print("The response of JobsApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**JobsPaginatedResponse**](JobsPaginatedResponse.md)

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

# **reject_job**
> GetJobResponse reject_job(job_id)

Reject a job

Reject a job

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.get_job_response import GetJobResponse
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
    api_instance = togai_client.JobsApi(api_client)
    job_id = 'mig.20aUyEZSuYq.SoGbS' # str | 

    try:
        # Reject a job
        api_response = api_instance.reject_job(job_id)
        print("The response of JobsApi->reject_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->reject_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**GetJobResponse**](GetJobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for get job status request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

