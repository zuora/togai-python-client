# PricePlanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_currencies** | **List[str]** |  | 
**active_currencies** | **List[str]** |  | [readonly] 
**pricing_cycle_config** | [**PricingCycleConfig**](PricingCycleConfig.md) |  | [optional] 
**usage_rate_cards** | [**List[UsageRateCard]**](UsageRateCard.md) |  | [optional] 
**fixed_fee_rate_cards** | [**List[FixedFeeRateCard]**](FixedFeeRateCard.md) |  | [optional] 
**license_rate_cards** | [**List[LicenseRateCard]**](LicenseRateCard.md) |  | [optional] 
**billing_entitlement_rate_cards** | [**List[BillingEntitlementRateCard]**](BillingEntitlementRateCard.md) |  | [optional] 
**entitlement_overage_rate_cards** | [**List[EntitlementOverageRateCard]**](EntitlementOverageRateCard.md) |  | [optional] 
**minimum_commitment** | [**MinimumCommitment**](MinimumCommitment.md) |  | [optional] 
**credit_grant_rate_cards** | [**List[CreditGrantRateCard]**](CreditGrantRateCard.md) |  | [optional] 
**type** | [**PricePlanType**](PricePlanType.md) |  | [optional] 
**deferred_revenue** | **bool** |  | [optional] 
**allow_ongoing_cycle_updates** | **object** | Allow changes to price plan from the beginning of the ongoing cycle. type: boolean  | [optional] 

## Example

```python
from togai_client.models.price_plan_details import PricePlanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanDetails from a JSON string
price_plan_details_instance = PricePlanDetails.from_json(json)
# print the JSON string representation of the object
print(PricePlanDetails.to_json())

# convert the object into a dict
price_plan_details_dict = price_plan_details_instance.to_dict()
# create an instance of PricePlanDetails from a dict
price_plan_details_from_dict = PricePlanDetails.from_dict(price_plan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


