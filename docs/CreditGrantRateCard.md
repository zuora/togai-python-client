# CreditGrantRateCard

Credit grant rate card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | [optional] 
**name** | **str** | Unique identifier for the rate card in a price plan. If left null it is auto-generated. | [optional] 
**tag** | **str** | A tag string to group creditGrantRateCard | [optional] 
**grant_details** | [**GrantDetails**](GrantDetails.md) |  | 
**rate_details** | [**CreditRateDetails**](CreditRateDetails.md) |  | 
**invoice_timing** | [**InvoiceTiming**](InvoiceTiming.md) |  | [optional] 
**type** | [**CreditGrantType**](CreditGrantType.md) |  | [optional] 
**recurrence_config** | [**RecurrenceConfig**](RecurrenceConfig.md) |  | [optional] 

## Example

```python
from togai_client.models.credit_grant_rate_card import CreditGrantRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of CreditGrantRateCard from a JSON string
credit_grant_rate_card_instance = CreditGrantRateCard.from_json(json)
# print the JSON string representation of the object
print(CreditGrantRateCard.to_json())

# convert the object into a dict
credit_grant_rate_card_dict = credit_grant_rate_card_instance.to_dict()
# create an instance of CreditGrantRateCard from a dict
credit_grant_rate_card_from_dict = CreditGrantRateCard.from_dict(credit_grant_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


