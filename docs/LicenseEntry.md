# LicenseEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** |  | 
**quantity** | **int** |  | 
**effective_from** | **datetime** |  | 

## Example

```python
from togai_client.models.license_entry import LicenseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseEntry from a JSON string
license_entry_instance = LicenseEntry.from_json(json)
# print the JSON string representation of the object
print(LicenseEntry.to_json())

# convert the object into a dict
license_entry_dict = license_entry_instance.to_dict()
# create an instance of LicenseEntry from a dict
license_entry_from_dict = LicenseEntry.from_dict(license_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


