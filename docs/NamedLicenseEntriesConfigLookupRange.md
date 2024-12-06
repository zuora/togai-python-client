# NamedLicenseEntriesConfigLookupRange

Range of named license entries to be looked up, this will be considered if mode is LOOKUP_RANGE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.named_license_entries_config_lookup_range import NamedLicenseEntriesConfigLookupRange

# TODO update the JSON string below
json = "{}"
# create an instance of NamedLicenseEntriesConfigLookupRange from a JSON string
named_license_entries_config_lookup_range_instance = NamedLicenseEntriesConfigLookupRange.from_json(json)
# print the JSON string representation of the object
print(NamedLicenseEntriesConfigLookupRange.to_json())

# convert the object into a dict
named_license_entries_config_lookup_range_dict = named_license_entries_config_lookup_range_instance.to_dict()
# create an instance of NamedLicenseEntriesConfigLookupRange from a dict
named_license_entries_config_lookup_range_from_dict = NamedLicenseEntriesConfigLookupRange.from_dict(named_license_entries_config_lookup_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


