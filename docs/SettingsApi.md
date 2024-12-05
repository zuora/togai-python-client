# togai_client.SettingsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting**](SettingsApi.md#get_setting) | **GET** /settings/{setting_id_str} | Get a setting
[**insert_setting**](SettingsApi.md#insert_setting) | **POST** /settings | Create a setting
[**list_setting**](SettingsApi.md#list_setting) | **GET** /settings | Lists settings
[**update_setting**](SettingsApi.md#update_setting) | **PATCH** /settings/{setting_id_str} | Update a setting


# **get_setting**
> Setting get_setting(setting_id_str)

Get a setting

Get a setting

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.setting import Setting
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
    api_instance = togai_client.SettingsApi(api_client)
    setting_id_str = 'setting.USER.success_threshold.ACCOUNT.G234DZZKBKACATFFGVGEMERFI' # str | 

    try:
        # Get a setting
        api_response = api_instance.get_setting(setting_id_str)
        print("The response of SettingsApi->get_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_id_str** | **str**|  | 

### Return type

[**Setting**](Setting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for insert and update settings request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_setting**
> Setting insert_setting(setting)

Create a setting

Create a setting

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.setting import Setting
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
    api_instance = togai_client.SettingsApi(api_client)
    setting = togai_client.Setting() # Setting | Payload to insert setting

    try:
        # Create a setting
        api_response = api_instance.insert_setting(setting)
        print("The response of SettingsApi->insert_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->insert_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | [**Setting**](Setting.md)| Payload to insert setting | 

### Return type

[**Setting**](Setting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for insert and update settings request |  -  |
**204** | Response for insert and update settings request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_setting**
> SettingPaginatedResponse list_setting(next_token=next_token, page_size=page_size, entity_type=entity_type, entity_id=entity_id, setting_id=setting_id, namespace=namespace)

Lists settings

List settings

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.setting_paginated_response import SettingPaginatedResponse
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
    api_instance = togai_client.SettingsApi(api_client)
    next_token = 'eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEwMCwgInNvcnRPcmRlciI6ICJhc2MifQ==' # str |  (optional)
    page_size = 10 # float |  (optional)
    entity_type = 'ACCOUNT' # str |  (optional)
    entity_id = 'acc_X1Df3sRf3' # str |  (optional)
    setting_id = 'setting_id_example' # str |  (optional)
    namespace = 'USER' # str |  (optional)

    try:
        # Lists settings
        api_response = api_instance.list_setting(next_token=next_token, page_size=page_size, entity_type=entity_type, entity_id=entity_id, setting_id=setting_id, namespace=namespace)
        print("The response of SettingsApi->list_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->list_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **entity_type** | **str**|  | [optional] 
 **entity_id** | **str**|  | [optional] 
 **setting_id** | **str**|  | [optional] 
 **namespace** | **str**|  | [optional] 

### Return type

[**SettingPaginatedResponse**](SettingPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list setting request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting**
> Setting update_setting(setting_id_str, update_setting_request)

Update a setting

Update a setting

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.setting import Setting
from togai_client.models.update_setting_request import UpdateSettingRequest
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
    api_instance = togai_client.SettingsApi(api_client)
    setting_id_str = 'setting.USER.success_threshold.ACCOUNT.G234DZZKBKACATFFGVGEMERFI' # str | 
    update_setting_request = togai_client.UpdateSettingRequest() # UpdateSettingRequest | Payload to update setting

    try:
        # Update a setting
        api_response = api_instance.update_setting(setting_id_str, update_setting_request)
        print("The response of SettingsApi->update_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->update_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_id_str** | **str**|  | 
 **update_setting_request** | [**UpdateSettingRequest**](UpdateSettingRequest.md)| Payload to update setting | 

### Return type

[**Setting**](Setting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for insert and update settings request |  -  |
**204** | Response for insert and update settings request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

