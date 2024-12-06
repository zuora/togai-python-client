# ProrationConfigLookupCycleConfig

Cycle of proration to be looked up, this will be considered if mode is LOOKUP_CYCLE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_date_time** | **datetime** | Defaults to current date time if not provided | [optional] 
**cycle_effective_on** | **datetime** | Defaults to current date time if not provided | [optional] 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.proration_config_lookup_cycle_config import ProrationConfigLookupCycleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProrationConfigLookupCycleConfig from a JSON string
proration_config_lookup_cycle_config_instance = ProrationConfigLookupCycleConfig.from_json(json)
# print the JSON string representation of the object
print(ProrationConfigLookupCycleConfig.to_json())

# convert the object into a dict
proration_config_lookup_cycle_config_dict = proration_config_lookup_cycle_config_instance.to_dict()
# create an instance of ProrationConfigLookupCycleConfig from a dict
proration_config_lookup_cycle_config_from_dict = ProrationConfigLookupCycleConfig.from_dict(proration_config_lookup_cycle_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


