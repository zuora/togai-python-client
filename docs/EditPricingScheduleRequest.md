# EditPricingScheduleRequest

Request to dis/associate one or more schedules to an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edits** | [**List[UpdatePricingScheduleRequest]**](UpdatePricingScheduleRequest.md) |  | 

## Example

```python
from togai_client.models.edit_pricing_schedule_request import EditPricingScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditPricingScheduleRequest from a JSON string
edit_pricing_schedule_request_instance = EditPricingScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(EditPricingScheduleRequest.to_json())

# convert the object into a dict
edit_pricing_schedule_request_dict = edit_pricing_schedule_request_instance.to_dict()
# create an instance of EditPricingScheduleRequest from a dict
edit_pricing_schedule_request_from_dict = EditPricingScheduleRequest.from_dict(edit_pricing_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


