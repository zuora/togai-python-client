# UpdatePricePlanV2Request

Request to update a price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of price plan | [optional] 
**pricing_cycle_config** | [**PricingCycleConfig**](PricingCycleConfig.md) |  | [optional] 
**supported_currencies** | **List[str]** | List of currencies supported by the price plan | [optional] 

## Example

```python
from togai_client.models.update_price_plan_v2_request import UpdatePricePlanV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricePlanV2Request from a JSON string
update_price_plan_v2_request_instance = UpdatePricePlanV2Request.from_json(json)
# print the JSON string representation of the object
print(UpdatePricePlanV2Request.to_json())

# convert the object into a dict
update_price_plan_v2_request_dict = update_price_plan_v2_request_instance.to_dict()
# create an instance of UpdatePricePlanV2Request from a dict
update_price_plan_v2_request_from_dict = UpdatePricePlanV2Request.from_dict(update_price_plan_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


