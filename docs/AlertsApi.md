# togai_client.AlertsApi

All URIs are relative to *https://api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert**](AlertsApi.md#create_alert) | **POST** /alerts | Create an alert
[**get_alert_template**](AlertsApi.md#get_alert_template) | **GET** /alert_templates/{alert_template_id} | Get an alert template
[**get_alert_templates**](AlertsApi.md#get_alert_templates) | **GET** /alert_templates | List alert templates
[**get_incident**](AlertsApi.md#get_incident) | **GET** /incidents/{incident_id} | Get an incident
[**get_incidents**](AlertsApi.md#get_incidents) | **GET** /incidents | List incidents
[**list_alerts**](AlertsApi.md#list_alerts) | **GET** /alerts | List alerts
[**update_alert**](AlertsApi.md#update_alert) | **PATCH** /alerts/{alert_id} | Update an alert
[**update_incident_status**](AlertsApi.md#update_incident_status) | **PUT** /incidents/{incident_id}/status | Update an incident status


# **create_alert**
> Alert create_alert(create_alert_request)

Create an alert

Create an alert

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alert import Alert
from togai_client.models.create_alert_request import CreateAlertRequest
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
    api_instance = togai_client.AlertsApi(api_client)
    create_alert_request = togai_client.CreateAlertRequest() # CreateAlertRequest | Payload to install an alert

    try:
        # Create an alert
        api_response = api_instance.create_alert(create_alert_request)
        print("The response of AlertsApi->create_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert_request** | [**CreateAlertRequest**](CreateAlertRequest.md)| Payload to install an alert | 

### Return type

[**Alert**](Alert.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for install alert request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_template**
> AlertTemplate get_alert_template(alert_template_id)

Get an alert template

Get an alert template

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alert_template import AlertTemplate
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
    api_instance = togai_client.AlertsApi(api_client)
    alert_template_id = 'abcd-efgh-ijkl-mnop' # str | 

    try:
        # Get an alert template
        api_response = api_instance.get_alert_template(alert_template_id)
        print("The response of AlertsApi->get_alert_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_template_id** | **str**|  | 

### Return type

[**AlertTemplate**](AlertTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for getting alert template |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_templates**
> AlertTemplatesPaginatedResponse get_alert_templates()

List alert templates

Returns a list of alert templates with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alert_templates_paginated_response import AlertTemplatesPaginatedResponse
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
    api_instance = togai_client.AlertsApi(api_client)

    try:
        # List alert templates
        api_response = api_instance.get_alert_templates()
        print("The response of AlertsApi->get_alert_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertTemplatesPaginatedResponse**](AlertTemplatesPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list Alert request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incident**
> Incident get_incident(incident_id)

Get an incident

Get an incident

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.incident import Incident
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
    api_instance = togai_client.AlertsApi(api_client)
    incident_id = 'inc.20aUyEZSuYq.SoGbS' # str | 

    try:
        # Get an incident
        api_response = api_instance.get_incident(incident_id)
        print("The response of AlertsApi->get_incident:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_incident: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**|  | 

### Return type

[**Incident**](Incident.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for getting incident |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incidents**
> IncidentsPaginatedResponse get_incidents()

List incidents

Returns a list of incidents with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.incidents_paginated_response import IncidentsPaginatedResponse
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
    api_instance = togai_client.AlertsApi(api_client)

    try:
        # List incidents
        api_response = api_instance.get_incidents()
        print("The response of AlertsApi->get_incidents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_incidents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IncidentsPaginatedResponse**](IncidentsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list incidents request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alerts**
> AlertsPaginatedResponse list_alerts()

List alerts

Returns a list of alerts with pagination and sort.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alerts_paginated_response import AlertsPaginatedResponse
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
    api_instance = togai_client.AlertsApi(api_client)

    try:
        # List alerts
        api_response = api_instance.list_alerts()
        print("The response of AlertsApi->list_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alerts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertsPaginatedResponse**](AlertsPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list Alert request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> Alert update_alert(alert_id, update_alert_request=update_alert_request)

Update an alert

Update an alert

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.alert import Alert
from togai_client.models.update_alert_request import UpdateAlertRequest
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
    api_instance = togai_client.AlertsApi(api_client)
    alert_id = 'alert.20aUyEZSuYq.SoGbS' # str | 
    update_alert_request = togai_client.UpdateAlertRequest() # UpdateAlertRequest | Payload to update alert (optional)

    try:
        # Update an alert
        api_response = api_instance.update_alert(alert_id, update_alert_request=update_alert_request)
        print("The response of AlertsApi->update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 
 **update_alert_request** | [**UpdateAlertRequest**](UpdateAlertRequest.md)| Payload to update alert | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for install alert request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_incident_status**
> Incident update_incident_status(incident_id, update_incident_status_request=update_incident_status_request)

Update an incident status

Update an incident status

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import togai_client
from togai_client.models.incident import Incident
from togai_client.models.update_incident_status_request import UpdateIncidentStatusRequest
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
    api_instance = togai_client.AlertsApi(api_client)
    incident_id = 'inc.20aUyEZSuYq.SoGbS' # str | 
    update_incident_status_request = togai_client.UpdateIncidentStatusRequest() # UpdateIncidentStatusRequest | Payload to update incident status (optional)

    try:
        # Update an incident status
        api_response = api_instance.update_incident_status(incident_id, update_incident_status_request=update_incident_status_request)
        print("The response of AlertsApi->update_incident_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_incident_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**|  | 
 **update_incident_status_request** | [**UpdateIncidentStatusRequest**](UpdateIncidentStatusRequest.md)| Payload to update incident status | [optional] 

### Return type

[**Incident**](Incident.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for getting incident |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

