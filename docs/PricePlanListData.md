# PricePlanListData

Data of price plan list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of price plan | 
**name** | **str** | Name of the price plan | 
**version** | **int** | Version of the price plan | 
**description** | **str** | Description of price plan | [optional] 
**status** | **str** | Status of Price plan | 
**usage_meters** | **List[str]** | Usage meters id linked to the price plan | 
**price_plan_details** | [**PricePlanDetails**](PricePlanDetails.md) |  | 
**pricing_rules** | [**List[PricingRule]**](PricingRule.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**type** | [**PricePlanType**](PricePlanType.md) |  | 

## Example

```python
from togai_client.models.price_plan_list_data import PricePlanListData

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanListData from a JSON string
price_plan_list_data_instance = PricePlanListData.from_json(json)
# print the JSON string representation of the object
print(PricePlanListData.to_json())

# convert the object into a dict
price_plan_list_data_dict = price_plan_list_data_instance.to_dict()
# create an instance of PricePlanListData from a dict
price_plan_list_data_from_dict = PricePlanListData.from_dict(price_plan_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


