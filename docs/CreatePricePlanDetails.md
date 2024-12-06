# CreatePricePlanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_cycle_config** | [**PricingCycleConfig**](PricingCycleConfig.md) |  | [optional] 
**supported_currencies** | **List[str]** | List of currencies supported by the price plan | 
**usage_rate_cards** | [**List[UsageRateCard]**](UsageRateCard.md) | List of usage rate cards | [optional] 
**fixed_fee_rate_cards** | [**List[FixedFeeRateCard]**](FixedFeeRateCard.md) |  | [optional] 
**license_rate_cards** | [**List[LicenseRateCard]**](LicenseRateCard.md) |  | [optional] 
**billing_entitlement_rate_cards** | [**List[BillingEntitlementRateCard]**](BillingEntitlementRateCard.md) |  | [optional] 
**minimum_commitment** | [**MinimumCommitment**](MinimumCommitment.md) |  | [optional] 
**credit_grant_rate_cards** | [**List[CreditGrantRateCard]**](CreditGrantRateCard.md) |  | [optional] 
**entitlement_overage_rate_cards** | [**List[EntitlementOverageRateCard]**](EntitlementOverageRateCard.md) |  | [optional] 
**deferred_revenue** | **bool** | This option can be enabled while creating a price plan to opt for deferred revenue finalization. i.e, Togai will assume that the price plan may change any time during the pricing cycle and  thereby does not compute the revenue in near-real time.  This gives the flexibility of editing rate cards in price plan from beginning of the pricing cycle. Enabling this mode comes with the following limitations. 1. Following rate cards are not supported under a &#x60;deferredRevenue&#x60; plan     * creditGrantRateCards,     * billingEntitlementRateCards,     * entitlementOverageRateCards,     * IN_ADVANCE fixedFeeRateCards,     * IN_ADVANCE licenseRateCards 2. Metrics API return revenue metrics only after the grace period of the account&#39;s pricing cycle  (i.e, only once the invoice becomes DUE)  | [optional] 
**allow_ongoing_cycle_updates** | **bool** | Allow changes to price plan from the beginning of the ongoing cycle.  | [optional] 

## Example

```python
from togai_client.models.create_price_plan_details import CreatePricePlanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePricePlanDetails from a JSON string
create_price_plan_details_instance = CreatePricePlanDetails.from_json(json)
# print the JSON string representation of the object
print(CreatePricePlanDetails.to_json())

# convert the object into a dict
create_price_plan_details_dict = create_price_plan_details_instance.to_dict()
# create an instance of CreatePricePlanDetails from a dict
create_price_plan_details_from_dict = CreatePricePlanDetails.from_dict(create_price_plan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


