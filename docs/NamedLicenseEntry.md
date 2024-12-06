# NamedLicenseEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** |  | 
**name** | **int** |  | 
**effective_from** | **datetime** |  | 
**effective_until** | **datetime** |  | [optional] 

## Example

```python
from togai_client.models.named_license_entry import NamedLicenseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NamedLicenseEntry from a JSON string
named_license_entry_instance = NamedLicenseEntry.from_json(json)
# print the JSON string representation of the object
print(NamedLicenseEntry.to_json())

# convert the object into a dict
named_license_entry_dict = named_license_entry_instance.to_dict()
# create an instance of NamedLicenseEntry from a dict
named_license_entry_from_dict = NamedLicenseEntry.from_dict(named_license_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


