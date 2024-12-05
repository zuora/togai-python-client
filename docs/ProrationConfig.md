# ProrationConfig

Configuration for getting the proration, if not provided no proration will be applied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the proration - CUSTOM: Use the proration provided in the request - LOOKUP_CYCLE: Use the proration of a given account for the specified cycle  | 
**custom_config** | [**ProrationConfigCustomConfig**](ProrationConfigCustomConfig.md) |  | [optional] 
**lookup_cycle_config** | [**ProrationConfigLookupCycleConfig**](ProrationConfigLookupCycleConfig.md) |  | [optional] 

## Example

```python
from togai_client.models.proration_config import ProrationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProrationConfig from a JSON string
proration_config_instance = ProrationConfig.from_json(json)
# print the JSON string representation of the object
print(ProrationConfig.to_json())

# convert the object into a dict
proration_config_dict = proration_config_instance.to_dict()
# create an instance of ProrationConfig from a dict
proration_config_from_dict = ProrationConfig.from_dict(proration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


