# UpdatePricingScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Identifier of the account | 
**account_name** | **str** | Name of the Account | 
**pricing_schedules** | [**List[PlanOverride]**](PlanOverride.md) |  | 

## Example

```python
from togai_client.models.update_pricing_schedule_response import UpdatePricingScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricingScheduleResponse from a JSON string
update_pricing_schedule_response_instance = UpdatePricingScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePricingScheduleResponse.to_json())

# convert the object into a dict
update_pricing_schedule_response_dict = update_pricing_schedule_response_instance.to_dict()
# create an instance of UpdatePricingScheduleResponse from a dict
update_pricing_schedule_response_from_dict = UpdatePricingScheduleResponse.from_dict(update_pricing_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


