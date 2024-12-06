# PurchasePlanOverride

entitlements override options for purchase of a price plan for an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_fee_rate_cards** | [**List[FixedFeeRateCard]**](FixedFeeRateCard.md) |  | [optional] 
**billing_entitlement_rate_cards** | [**List[BillingEntitlementRateCard]**](BillingEntitlementRateCard.md) |  | [optional] 
**credit_grant_rate_cards** | [**List[CreditGrantRateCard]**](CreditGrantRateCard.md) |  | [optional] 

## Example

```python
from togai_client.models.purchase_plan_override import PurchasePlanOverride

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasePlanOverride from a JSON string
purchase_plan_override_instance = PurchasePlanOverride.from_json(json)
# print the JSON string representation of the object
print(PurchasePlanOverride.to_json())

# convert the object into a dict
purchase_plan_override_dict = purchase_plan_override_instance.to_dict()
# create an instance of PurchasePlanOverride from a dict
purchase_plan_override_from_dict = PurchasePlanOverride.from_dict(purchase_plan_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


