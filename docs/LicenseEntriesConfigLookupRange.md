# LicenseEntriesConfigLookupRange

Range of license entries to be looked up, this will be considered if mode is LOOKUP_RANGE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.license_entries_config_lookup_range import LicenseEntriesConfigLookupRange

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseEntriesConfigLookupRange from a JSON string
license_entries_config_lookup_range_instance = LicenseEntriesConfigLookupRange.from_json(json)
# print the JSON string representation of the object
print(LicenseEntriesConfigLookupRange.to_json())

# convert the object into a dict
license_entries_config_lookup_range_dict = license_entries_config_lookup_range_instance.to_dict()
# create an instance of LicenseEntriesConfigLookupRange from a dict
license_entries_config_lookup_range_from_dict = LicenseEntriesConfigLookupRange.from_dict(license_entries_config_lookup_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


