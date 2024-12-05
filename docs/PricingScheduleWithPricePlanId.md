# PricingScheduleWithPricePlanId


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
**price_plan_id** | **str** |  | 
**price_plan_name** | **str** |  | [optional] 
**price_plan_info** | [**PricePlanInfo**](PricePlanInfo.md) |  | [optional] 

## Example

```python
from togai_client.models.pricing_schedule_with_price_plan_id import PricingScheduleWithPricePlanId

# TODO update the JSON string below
json = "{}"
# create an instance of PricingScheduleWithPricePlanId from a JSON string
pricing_schedule_with_price_plan_id_instance = PricingScheduleWithPricePlanId.from_json(json)
# print the JSON string representation of the object
print(PricingScheduleWithPricePlanId.to_json())

# convert the object into a dict
pricing_schedule_with_price_plan_id_dict = pricing_schedule_with_price_plan_id_instance.to_dict()
# create an instance of PricingScheduleWithPricePlanId from a dict
pricing_schedule_with_price_plan_id_from_dict = PricingScheduleWithPricePlanId.from_dict(pricing_schedule_with_price_plan_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


