# NamedLicenseEntriesConfig

Configuration for getting the named license entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the named license entries for the license rate cards - CUSTOM: Use the named license entries provided in the request - LOOKUP_RANGE: Use the named license entries of a given account for the specified range - LOOKUP_CYCLE: Use the named license entries of a given account for the specified cycle  | 
**custom** | [**List[NamedLicenseEntry]**](NamedLicenseEntry.md) | List of named license entries, this will be considered if mode is CUSTOM | [optional] 
**lookup_range** | [**NamedLicenseEntriesConfigLookupRange**](NamedLicenseEntriesConfigLookupRange.md) |  | [optional] 
**lookup_cycle** | [**NamedLicenseEntriesConfigLookupCycle**](NamedLicenseEntriesConfigLookupCycle.md) |  | [optional] 

## Example

```python
from togai_client.models.named_license_entries_config import NamedLicenseEntriesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NamedLicenseEntriesConfig from a JSON string
named_license_entries_config_instance = NamedLicenseEntriesConfig.from_json(json)
# print the JSON string representation of the object
print(NamedLicenseEntriesConfig.to_json())

# convert the object into a dict
named_license_entries_config_dict = named_license_entries_config_instance.to_dict()
# create an instance of NamedLicenseEntriesConfig from a dict
named_license_entries_config_from_dict = NamedLicenseEntriesConfig.from_dict(named_license_entries_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


