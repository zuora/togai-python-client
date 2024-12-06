# CreatePricePlanRequest

Request to create a price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the price plan | 
**description** | **str** | Description of price plan | [optional] 
**type** | [**PricePlanType**](PricePlanType.md) |  | [optional] 
**price_plan_details** | [**CreatePricePlanDetails**](CreatePricePlanDetails.md) |  | 
**pricing_rules** | [**List[CreatePricingRule]**](CreatePricingRule.md) |  | [optional] 

## Example

```python
from togai_client.models.create_price_plan_request import CreatePricePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePricePlanRequest from a JSON string
create_price_plan_request_instance = CreatePricePlanRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePricePlanRequest.to_json())

# convert the object into a dict
create_price_plan_request_dict = create_price_plan_request_instance.to_dict()
# create an instance of CreatePricePlanRequest from a dict
create_price_plan_request_from_dict = CreatePricePlanRequest.from_dict(create_price_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


