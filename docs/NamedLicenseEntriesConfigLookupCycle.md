# NamedLicenseEntriesConfigLookupCycle

Cycle of named license entries to be looked up, this will be considered if mode is LOOKUP_CYCLE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_effective_on** | **datetime** | Effective date of the cycle, will be used to get the named license entries of the cycle | [optional] 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.named_license_entries_config_lookup_cycle import NamedLicenseEntriesConfigLookupCycle

# TODO update the JSON string below
json = "{}"
# create an instance of NamedLicenseEntriesConfigLookupCycle from a JSON string
named_license_entries_config_lookup_cycle_instance = NamedLicenseEntriesConfigLookupCycle.from_json(json)
# print the JSON string representation of the object
print(NamedLicenseEntriesConfigLookupCycle.to_json())

# convert the object into a dict
named_license_entries_config_lookup_cycle_dict = named_license_entries_config_lookup_cycle_instance.to_dict()
# create an instance of NamedLicenseEntriesConfigLookupCycle from a dict
named_license_entries_config_lookup_cycle_from_dict = NamedLicenseEntriesConfigLookupCycle.from_dict(named_license_entries_config_lookup_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


