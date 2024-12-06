# RateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_id** | **str** | Billable identifier | 
**type** | [**RateCardType**](RateCardType.md) |  | 
**display_name** | **str** | Display name of the rate card | 
**invoice_timing** | [**InvoiceTiming**](InvoiceTiming.md) |  | 
**rate_card_details** | [**RateCardDetails**](RateCardDetails.md) |  | 
**tag** | **str** | Tag for rate card | [optional] 
**name** | **str** |  | 
**reference_id** | **str** |  | 
**reference_type** | **str** |  | 
**currencies** | **List[str]** | List of currencies supported by the rate card | [optional] 
**price_plan_id** | **str** | Price plan identifier | 
**account_id** | **str** | Account identifier | [optional] 

## Example

```python
from togai_client.models.rate_card import RateCard

# TODO update the JSON string below
json = "{}"
# create an instance of RateCard from a JSON string
rate_card_instance = RateCard.from_json(json)
# print the JSON string representation of the object
print(RateCard.to_json())

# convert the object into a dict
rate_card_dict = rate_card_instance.to_dict()
# create an instance of RateCard from a dict
rate_card_from_dict = RateCard.from_dict(rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


