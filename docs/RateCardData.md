# RateCardData

Request to create a rate card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_id** | **str** | Billable identifier | 
**type** | [**RateCardType**](RateCardType.md) |  | 
**display_name** | **str** | Display name of the rate card | [optional] 
**invoice_timing** | [**InvoiceTiming**](InvoiceTiming.md) |  | 
**rate_card_details** | [**RateCardDetails**](RateCardDetails.md) |  | 
**tag** | **str** | Tag for rate card | [optional] 

## Example

```python
from togai_client.models.rate_card_data import RateCardData

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardData from a JSON string
rate_card_data_instance = RateCardData.from_json(json)
# print the JSON string representation of the object
print(RateCardData.to_json())

# convert the object into a dict
rate_card_data_dict = rate_card_data_instance.to_dict()
# create an instance of RateCardData from a dict
rate_card_data_from_dict = RateCardData.from_dict(rate_card_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


