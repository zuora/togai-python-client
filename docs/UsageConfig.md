# UsageConfig

Configuration for getting the usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the usage for the usage meters - CUSTOM: Use the usages provided in the request - LOOKUP_RANGE: Use the usage of a given account for the specified range - LOOKUP_CYCLE: Use the usage of a given account for the specified cycle  | 
**usage_map** | **Dict[str, float]** | Map of usage meter id and usage, this will be considered if mode is CUSTOM | [optional] 
**lookup_range** | [**UsageConfigLookupRange**](UsageConfigLookupRange.md) |  | [optional] 
**lookup_cycle** | [**UsageConfigLookupCycle**](UsageConfigLookupCycle.md) |  | [optional] 

## Example

```python
from togai_client.models.usage_config import UsageConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UsageConfig from a JSON string
usage_config_instance = UsageConfig.from_json(json)
# print the JSON string representation of the object
print(UsageConfig.to_json())

# convert the object into a dict
usage_config_dict = usage_config_instance.to_dict()
# create an instance of UsageConfig from a dict
usage_config_from_dict = UsageConfig.from_dict(usage_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


