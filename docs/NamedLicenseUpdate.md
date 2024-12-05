# NamedLicenseUpdate

Named License update response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**license_id** | **str** |  | 
**account_id** | **str** |  | 
**name** | **str** |  | 
**effective_from** | **datetime** |  | [optional] 
**effective_until** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from togai_client.models.named_license_update import NamedLicenseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NamedLicenseUpdate from a JSON string
named_license_update_instance = NamedLicenseUpdate.from_json(json)
# print the JSON string representation of the object
print(NamedLicenseUpdate.to_json())

# convert the object into a dict
named_license_update_dict = named_license_update_instance.to_dict()
# create an instance of NamedLicenseUpdate from a dict
named_license_update_from_dict = NamedLicenseUpdate.from_dict(named_license_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


