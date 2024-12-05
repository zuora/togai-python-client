# ScheduleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_currencies** | **List[str]** |  | 
**pricing_cycle_config** | [**PricingCycleConfig**](PricingCycleConfig.md) |  | 
**pricing_rules** | [**List[PricingRule]**](PricingRule.md) |  | [optional] 

## Example

```python
from togai_client.models.schedule_info import ScheduleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleInfo from a JSON string
schedule_info_instance = ScheduleInfo.from_json(json)
# print the JSON string representation of the object
print(ScheduleInfo.to_json())

# convert the object into a dict
schedule_info_dict = schedule_info_instance.to_dict()
# create an instance of ScheduleInfo from a dict
schedule_info_from_dict = ScheduleInfo.from_dict(schedule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

