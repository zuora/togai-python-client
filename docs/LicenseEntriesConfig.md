# LicenseEntriesConfig

Configuration for getting the license entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the license entries for the license rate cards - CUSTOM: Use the license entries provided in the request - LOOKUP_RANGE: Use the license entries of a given account for the specified range - LOOKUP_CYCLE: Use the license entries of a given account for the specified cycle  | 
**custom** | [**List[LicenseEntry]**](LicenseEntry.md) | List of license entries, this will be considered if mode is CUSTOM | [optional] 
**lookup_range** | [**LicenseEntriesConfigLookupRange**](LicenseEntriesConfigLookupRange.md) |  | [optional] 
**lookup_cycle** | [**LicenseEntriesConfigLookupCycle**](LicenseEntriesConfigLookupCycle.md) |  | [optional] 

## Example

```python
from togai_client.models.license_entries_config import LicenseEntriesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseEntriesConfig from a JSON string
license_entries_config_instance = LicenseEntriesConfig.from_json(json)
# print the JSON string representation of the object
print(LicenseEntriesConfig.to_json())

# convert the object into a dict
license_entries_config_dict = license_entries_config_instance.to_dict()
# create an instance of LicenseEntriesConfig from a dict
license_entries_config_from_dict = LicenseEntriesConfig.from_dict(license_entries_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


