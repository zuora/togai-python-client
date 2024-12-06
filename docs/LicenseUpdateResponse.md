# LicenseUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** |  | 
**account_id** | **str** |  | 
**quantity** | **float** | Absolute quantity of the license | 
**effective_from** | **datetime** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from togai_client.models.license_update_response import LicenseUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUpdateResponse from a JSON string
license_update_response_instance = LicenseUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(LicenseUpdateResponse.to_json())

# convert the object into a dict
license_update_response_dict = license_update_response_instance.to_dict()
# create an instance of LicenseUpdateResponse from a dict
license_update_response_from_dict = LicenseUpdateResponse.from_dict(license_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


