# CreatePricePlanV2Request

Request to create a price plan

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

## Example

```python
from togai_client.models.create_price_plan_v2_request import CreatePricePlanV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePricePlanV2Request from a JSON string
create_price_plan_v2_request_instance = CreatePricePlanV2Request.from_json(json)
# print the JSON string representation of the object
print(CreatePricePlanV2Request.to_json())

# convert the object into a dict
create_price_plan_v2_request_dict = create_price_plan_v2_request_instance.to_dict()
# create an instance of CreatePricePlanV2Request from a dict
create_price_plan_v2_request_from_dict = CreatePricePlanV2Request.from_dict(create_price_plan_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


