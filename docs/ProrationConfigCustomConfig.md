# ProrationConfigCustomConfig

Custom proration config, this will be considered if mode is CUSTOM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_start_date** | **datetime** |  | 
**cycle_end_date** | **datetime** |  | 
**current_date** | **datetime** |  | 

## Example

```python
from togai_client.models.proration_config_custom_config import ProrationConfigCustomConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProrationConfigCustomConfig from a JSON string
proration_config_custom_config_instance = ProrationConfigCustomConfig.from_json(json)
# print the JSON string representation of the object
print(ProrationConfigCustomConfig.to_json())

# convert the object into a dict
proration_config_custom_config_dict = proration_config_custom_config_instance.to_dict()
# create an instance of ProrationConfigCustomConfig from a dict
proration_config_custom_config_from_dict = ProrationConfigCustomConfig.from_dict(proration_config_custom_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


