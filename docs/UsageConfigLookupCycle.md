# UsageConfigLookupCycle

Cycle of usage to be looked up, this will be considered if mode is LOOKUP_CYCLE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_effective_on** | **datetime** |  | [optional] 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.usage_config_lookup_cycle import UsageConfigLookupCycle

# TODO update the JSON string below
json = "{}"
# create an instance of UsageConfigLookupCycle from a JSON string
usage_config_lookup_cycle_instance = UsageConfigLookupCycle.from_json(json)
# print the JSON string representation of the object
print(UsageConfigLookupCycle.to_json())

# convert the object into a dict
usage_config_lookup_cycle_dict = usage_config_lookup_cycle_instance.to_dict()
# create an instance of UsageConfigLookupCycle from a dict
usage_config_lookup_cycle_from_dict = UsageConfigLookupCycle.from_dict(usage_config_lookup_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


