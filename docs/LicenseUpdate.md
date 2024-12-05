# LicenseUpdate

License update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** |  | 
**account_id** | **str** |  | 
**quantity** | **float** | Absolute quantity of the license | 
**effective_from** | **datetime** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.license_update import LicenseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUpdate from a JSON string
license_update_instance = LicenseUpdate.from_json(json)
# print the JSON string representation of the object
print(LicenseUpdate.to_json())

# convert the object into a dict
license_update_dict = license_update_instance.to_dict()
# create an instance of LicenseUpdate from a dict
license_update_from_dict = LicenseUpdate.from_dict(license_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


