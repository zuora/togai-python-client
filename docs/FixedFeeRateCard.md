# FixedFeeRateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the attached AddOn | 
**display_name** | **str** | Name of the attached AddOn | [optional] 
**name** | **str** | Unique identifier for the rate card in a price plan. If left null it is auto-generated. | [optional] 
**tag** | **str** | A tag string to group fixedFeeRateCards | [optional] 
**invoice_timing** | [**InvoiceTiming**](InvoiceTiming.md) |  | [optional] 
**type** | [**FixedFeeType**](FixedFeeType.md) |  | [optional] 
**rate_values** | [**List[CurrencyRateValue]**](CurrencyRateValue.md) |  | 
**enable_proration** | **bool** |  | 
**recurrence_config** | [**RecurrenceConfig**](RecurrenceConfig.md) |  | [optional] 

## Example

```python
from togai_client.models.fixed_fee_rate_card import FixedFeeRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of FixedFeeRateCard from a JSON string
fixed_fee_rate_card_instance = FixedFeeRateCard.from_json(json)
# print the JSON string representation of the object
print(FixedFeeRateCard.to_json())

# convert the object into a dict
fixed_fee_rate_card_dict = fixed_fee_rate_card_instance.to_dict()
# create an instance of FixedFeeRateCard from a dict
fixed_fee_rate_card_from_dict = FixedFeeRateCard.from_dict(fixed_fee_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


