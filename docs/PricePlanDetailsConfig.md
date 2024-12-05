# PricePlanDetailsConfig

Configuration for getting the usage rate card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the usage rate card - CUSTOM: Use the price plan details provided in the request - PRICE_PLAN: Use the usage rate cards of the given price plan - ACCOUNT: Use the usage rate cards of a associated price plan of the given account  | 
**price_plan_details** | [**CreatePricePlanDetails**](CreatePricePlanDetails.md) |  | [optional] 
**price_plan_id** | **str** | Id of the price plan, this will be considered if mode is PRICE_PLAN | [optional] 
**account_id** | **str** | Id of the account, this will be considered if mode is ACCOUNT | [optional] 
**effective_on** | **datetime** | Will be used for getting the usage rate card, only used if mode is ACCOUNT or PRICE_PLAN | [optional] 
**pricing_cycle_ordinal** | **int** | nth cycle, will be used to calculate revenue for the particular cycle, only used if mode is CUSTOM or PRICE_PLAN | [optional] 

## Example

```python
from togai_client.models.price_plan_details_config import PricePlanDetailsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanDetailsConfig from a JSON string
price_plan_details_config_instance = PricePlanDetailsConfig.from_json(json)
# print the JSON string representation of the object
print(PricePlanDetailsConfig.to_json())

# convert the object into a dict
price_plan_details_config_dict = price_plan_details_config_instance.to_dict()
# create an instance of PricePlanDetailsConfig from a dict
price_plan_details_config_from_dict = PricePlanDetailsConfig.from_dict(price_plan_details_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


