# PricePlanV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the price plan | 
**description** | **str** | Description of price plan | [optional] 
**type** | [**PricePlanType**](PricePlanType.md) |  | 
**pricing_cycle_config** | [**PricingCycleConfig**](PricingCycleConfig.md) |  | [optional] 
**supported_currencies** | **List[str]** | List of currencies supported by the price plan | 
**deferred_revenue** | **bool** | This option can be enabled while creating a price plan to opt for deferred revenue finalization. i.e, Togai will assume that the price plan may change any time during the pricing cycle and  thereby does not compute the revenue in near-real time.  This gives the flexibility of editing rate cards in price plan from beginning of the pricing cycle. Enabling this mode comes with the following limitations. 1. Following rate cards are not supported under a &#x60;deferredRevenue&#x60; plan     * creditGrantRateCards,     * billingEntitlementRateCards,     * entitlementOverageRateCards,     * IN_ADVANCE fixedFeeRateCards,     * IN_ADVANCE licenseRateCards 2. Metrics API return revenue metrics only after the grace period of the account&#39;s pricing cycle  (i.e, only once the invoice becomes DUE)  | [optional] 
**allow_ongoing_cycle_updates** | **bool** | Allow changes to price plan from the beginning of the ongoing cycle.  | [optional] 
**id** | **str** |  | 
**reference_id** | **str** |  | 
**version** | **int** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from togai_client.models.price_plan_v2 import PricePlanV2

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanV2 from a JSON string
price_plan_v2_instance = PricePlanV2.from_json(json)
# print the JSON string representation of the object
print(PricePlanV2.to_json())

# convert the object into a dict
price_plan_v2_dict = price_plan_v2_instance.to_dict()
# create an instance of PricePlanV2 from a dict
price_plan_v2_from_dict = PricePlanV2.from_dict(price_plan_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


