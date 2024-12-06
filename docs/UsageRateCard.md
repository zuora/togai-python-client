# UsageRateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Name your rate card, this will be displayed in the Togai App | [optional] 
**name** | **str** | Unique identifier for the rate card in a price plan. If left null it is auto-generated. | [optional] 
**tag** | **str** | A tag string to group usageRateCards | [optional] 
**usage_meter_id** | **str** |  | 
**rate_plan** | [**RatePlan**](RatePlan.md) |  | 
**rate_values** | [**List[RateValue]**](RateValue.md) |  | 

## Example

```python
from togai_client.models.usage_rate_card import UsageRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRateCard from a JSON string
usage_rate_card_instance = UsageRateCard.from_json(json)
# print the JSON string representation of the object
print(UsageRateCard.to_json())

# convert the object into a dict
usage_rate_card_dict = usage_rate_card_instance.to_dict()
# create an instance of UsageRateCard from a dict
usage_rate_card_from_dict = UsageRateCard.from_dict(usage_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


