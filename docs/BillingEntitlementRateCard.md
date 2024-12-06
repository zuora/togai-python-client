# BillingEntitlementRateCard

Billing Entitlement rate card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** |  | 
**feature_configs** | [**List[FeatureConfig]**](FeatureConfig.md) |  | 
**tag** | **str** | A tag string to group rate cards | [optional] 
**invoice_timing** | [**InvoiceTiming**](InvoiceTiming.md) |  | 
**display_name** | **str** | Name your rate card, this will be used in invoice | [optional] 
**name** | **str** | Unique identifier for the rate card in a price plan. If left null it is auto-generated. | [optional] 
**rate_plan** | [**RatePlan**](RatePlan.md) |  | 
**rate_values** | [**List[RateValue]**](RateValue.md) |  | 
**recurrence_config** | [**RecurrenceConfig**](RecurrenceConfig.md) |  | [optional] 

## Example

```python
from togai_client.models.billing_entitlement_rate_card import BillingEntitlementRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of BillingEntitlementRateCard from a JSON string
billing_entitlement_rate_card_instance = BillingEntitlementRateCard.from_json(json)
# print the JSON string representation of the object
print(BillingEntitlementRateCard.to_json())

# convert the object into a dict
billing_entitlement_rate_card_dict = billing_entitlement_rate_card_instance.to_dict()
# create an instance of BillingEntitlementRateCard from a dict
billing_entitlement_rate_card_from_dict = BillingEntitlementRateCard.from_dict(billing_entitlement_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


