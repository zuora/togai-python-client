# RecurrenceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | Represents the number of pricing cycles after which the rate card will be charged | [optional] 
**offset** | **int** | Represents the offset for pricing cycles after which the rate card will be charged | [optional] 

## Example

```python
from togai_client.models.recurrence_config import RecurrenceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceConfig from a JSON string
recurrence_config_instance = RecurrenceConfig.from_json(json)
# print the JSON string representation of the object
print(RecurrenceConfig.to_json())

# convert the object into a dict
recurrence_config_dict = recurrence_config_instance.to_dict()
# create an instance of RecurrenceConfig from a dict
recurrence_config_from_dict = RecurrenceConfig.from_dict(recurrence_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


