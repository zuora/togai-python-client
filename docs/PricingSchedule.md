# PricingSchedule

Represents effectiveness period and config of a price plan. i.e, price plan bound by time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**price_plan_details** | [**PricePlanDetails**](PricePlanDetails.md) |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**version** | **int** |  | 
**pricing_rules** | [**List[PricingRule]**](PricingRule.md) |  | [optional] 
**is_overriden** | **bool** |  | 

## Example

```python
from togai_client.models.pricing_schedule import PricingSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of PricingSchedule from a JSON string
pricing_schedule_instance = PricingSchedule.from_json(json)
# print the JSON string representation of the object
print(PricingSchedule.to_json())

# convert the object into a dict
pricing_schedule_dict = pricing_schedule_instance.to_dict()
# create an instance of PricingSchedule from a dict
pricing_schedule_from_dict = PricingSchedule.from_dict(pricing_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


