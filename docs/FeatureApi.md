# togai_client.FeatureApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feature**](FeatureApi.md#create_feature) | **POST** /features | Create a Feature and optionally associate with one or more event_schemas
[**get_feature**](FeatureApi.md#get_feature) | **GET** /features/{feature_id} | Get a Feature
[**get_features**](FeatureApi.md#get_features) | **GET** /features | List Feature
[**update_feature**](FeatureApi.md#update_feature) | **PATCH** /features/{feature_id} | Update a Feature


# **create_feature**
> Feature create_feature(create_feature_request)

Create a Feature and optionally associate with one or more event_schemas

Create a Feature optionally associate with one or more event_schemas

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.create_feature_request import CreateFeatureRequest
from togai_client.models.feature import Feature
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
    api_instance = togai_client.FeatureApi(api_client)
    create_feature_request = togai_client.CreateFeatureRequest() # CreateFeatureRequest | Payload to create a Feature along the association with event_schemas

    try:
        # Create a Feature and optionally associate with one or more event_schemas
        api_response = api_instance.create_feature(create_feature_request)
        print("The response of FeatureApi->create_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->create_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_feature_request** | [**CreateFeatureRequest**](CreateFeatureRequest.md)| Payload to create a Feature along the association with event_schemas | 

### Return type

[**Feature**](Feature.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get Feature requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature**
> Feature get_feature(feature_id)

Get a Feature

Get details of a Feature

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.feature import Feature
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
    api_instance = togai_client.FeatureApi(api_client)
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature

    try:
        # Get a Feature
        api_response = api_instance.get_feature(feature_id)
        print("The response of FeatureApi->get_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->get_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| feature_id corresponding to a feature | 

### Return type

[**Feature**](Feature.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get Feature requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_features**
> FeaturePaginatedListData get_features(next_token=next_token, page_size=page_size)

List Feature

Get a list of features along with its associations

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.feature_paginated_list_data import FeaturePaginatedListData
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
    api_instance = togai_client.FeatureApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)

    try:
        # List Feature
        api_response = api_instance.get_features(next_token=next_token, page_size=page_size)
        print("The response of FeatureApi->get_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->get_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**FeaturePaginatedListData**](FeaturePaginatedListData.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list Feature request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feature**
> Feature update_feature(feature_id, update_feature_request)

Update a Feature

Update an existing feature and its eventSchema associations 

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.feature import Feature
from togai_client.models.update_feature_request import UpdateFeatureRequest
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
    api_instance = togai_client.FeatureApi(api_client)
    feature_id = 'feat.fdjskl.sdkjl' # str | feature_id corresponding to a feature
    update_feature_request = togai_client.UpdateFeatureRequest() # UpdateFeatureRequest | Payload to update a Feature along the associations with event_schemas

    try:
        # Update a Feature
        api_response = api_instance.update_feature(feature_id, update_feature_request)
        print("The response of FeatureApi->update_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->update_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| feature_id corresponding to a feature | 
 **update_feature_request** | [**UpdateFeatureRequest**](UpdateFeatureRequest.md)| Payload to update a Feature along the associations with event_schemas | 

### Return type

[**Feature**](Feature.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get Feature requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

