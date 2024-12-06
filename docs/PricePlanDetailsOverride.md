# PricePlanDetailsOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_cycle_config** | [**PricingCycleConfig**](PricingCycleConfig.md) |  | [optional] 
**supported_currencies** | **List[str]** |  | [optional] 
**usage_rate_cards** | [**List[UsageRateCard]**](UsageRateCard.md) |  | [optional] 
**billing_entitlement_rate_cards** | [**List[BillingEntitlementRateCard]**](BillingEntitlementRateCard.md) |  | [optional] 
**entitlement_overage_rate_cards** | [**List[EntitlementOverageRateCard]**](EntitlementOverageRateCard.md) |  | [optional] 
**fixed_fee_rate_cards** | [**List[FixedFeeRateCard]**](FixedFeeRateCard.md) |  | [optional] 
**license_rate_cards** | [**List[LicenseRateCard]**](LicenseRateCard.md) |  | [optional] 
**minimum_commitment** | [**MinimumCommitment**](MinimumCommitment.md) |  | [optional] 
**credit_grant_rate_cards** | [**List[CreditGrantRateCard]**](CreditGrantRateCard.md) |  | [optional] 

## Example

```python
from togai_client.models.price_plan_details_override import PricePlanDetailsOverride

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanDetailsOverride from a JSON string
price_plan_details_override_instance = PricePlanDetailsOverride.from_json(json)
# print the JSON string representation of the object
print(PricePlanDetailsOverride.to_json())

# convert the object into a dict
price_plan_details_override_dict = price_plan_details_override_instance.to_dict()
# create an instance of PricePlanDetailsOverride from a dict
price_plan_details_override_from_dict = PricePlanDetailsOverride.from_dict(price_plan_details_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


