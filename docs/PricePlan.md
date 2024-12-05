# PricePlan

Price plan entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Price plan id | 
**name** | **str** | Name of the price plan | 
**type** | [**PricePlanType**](PricePlanType.md) |  | 
**description** | **str** | Description of price plan | [optional] 
**status** | **str** | Status of Price plan | 
**pricing_schedule** | [**List[PricingSchedule]**](PricingSchedule.md) |  | 

## Example

```python
from togai_client.models.price_plan import PricePlan

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlan from a JSON string
price_plan_instance = PricePlan.from_json(json)
# print the JSON string representation of the object
print(PricePlan.to_json())

# convert the object into a dict
price_plan_dict = price_plan_instance.to_dict()
# create an instance of PricePlan from a dict
price_plan_from_dict = PricePlan.from_dict(price_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


