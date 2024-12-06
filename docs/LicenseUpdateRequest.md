# LicenseUpdateRequest

License update request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** | The license id for which the update is requested | 
**account_id** | **str** | The account id for which the license is being updated | 
**update_type** | **str** | The type of update to be performed | 
**quantity** | **float** | The quantity to be updated | 
**effective_from** | **datetime** | The effective from date for the update | [optional] 
**idempotency_key** | **str** | The idempotency key for uniqueness of the license update request | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.license_update_request import LicenseUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUpdateRequest from a JSON string
license_update_request_instance = LicenseUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LicenseUpdateRequest.to_json())

# convert the object into a dict
license_update_request_dict = license_update_request_instance.to_dict()
# create an instance of LicenseUpdateRequest from a dict
license_update_request_from_dict = LicenseUpdateRequest.from_dict(license_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


