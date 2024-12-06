# LicenseRateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the attached AddOn | 
**type** | [**AddOnType**](AddOnType.md) |  | [optional] 
**display_name** | **str** | Name of the attached AddOn | [optional] 
**name** | **str** | Unique identifier for the rate card in a price plan. If left null it is auto-generated. | [optional] 
**tag** | **str** | A tag string to group licenseRateCards | [optional] 
**invoice_timing** | [**InvoiceTiming**](InvoiceTiming.md) |  | [optional] 
**usage_cycle** | [**UsageCycleInterval**](UsageCycleInterval.md) |  | [optional] 
**enable_proration** | **bool** |  | 
**config** | [**LicenseRateCardConfig**](LicenseRateCardConfig.md) |  | [optional] 
**rate_plan** | [**RatePlan**](RatePlan.md) |  | 
**rate_values** | [**List[RateValue]**](RateValue.md) |  | 
**prorated_refund_mode** | [**ProratedRefundMode**](ProratedRefundMode.md) |  | [optional] 

## Example

```python
from togai_client.models.license_rate_card import LicenseRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRateCard from a JSON string
license_rate_card_instance = LicenseRateCard.from_json(json)
# print the JSON string representation of the object
print(LicenseRateCard.to_json())

# convert the object into a dict
license_rate_card_dict = license_rate_card_instance.to_dict()
# create an instance of LicenseRateCard from a dict
license_rate_card_from_dict = LicenseRateCard.from_dict(license_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


