# PlanOverride

Represents effectiveness period and config of a price plan. i.e, price plan bound by time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**price_plan_id** | **str** |  | 
**price_plan_name** | **str** |  | 
**price_plan_details_override** | [**PricePlanDetailsOverride**](PricePlanDetailsOverride.md) |  | [optional] 
**pricing_rules_override** | [**List[PricingRule]**](PricingRule.md) |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 

## Example

```python
from togai_client.models.plan_override import PlanOverride

# TODO update the JSON string below
json = "{}"
# create an instance of PlanOverride from a JSON string
plan_override_instance = PlanOverride.from_json(json)
# print the JSON string representation of the object
print(PlanOverride.to_json())

# convert the object into a dict
plan_override_dict = plan_override_instance.to_dict()
# create an instance of PlanOverride from a dict
plan_override_from_dict = PlanOverride.from_dict(plan_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


