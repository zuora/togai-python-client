# RevenueInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_rate_card** | [**UsageRateCard**](UsageRateCard.md) |  | [optional] 
**fixed_fee_rate_card** | [**FixedFeeRateCard**](FixedFeeRateCard.md) |  | [optional] 
**license_rate_card** | [**LicenseRateCard**](LicenseRateCard.md) |  | [optional] 
**billing_entitlement_rate_card** | [**BillingEntitlementRateCard**](BillingEntitlementRateCard.md) |  | [optional] 
**credit_grant_rate_card** | [**CreditGrantRateCard**](CreditGrantRateCard.md) |  | [optional] 
**entitlement_overage_rate_card** | [**EntitlementOverageRateCard**](EntitlementOverageRateCard.md) |  | [optional] 
**usages** | **Dict[str, float]** |  | 
**fixed_fee_revenue_summary** | [**FixedFeeRevenueSummary**](FixedFeeRevenueSummary.md) |  | [optional] 
**license_revenue_summary** | [**List[SlabRevenueSummary]**](SlabRevenueSummary.md) |  | [optional] 
**billing_entitlement_revenue_summary** | [**BillingEntitlementRevenueSummary**](BillingEntitlementRevenueSummary.md) |  | [optional] 
**credit_grant_revenue_summary** | [**CreditGrantRevenueSummary**](CreditGrantRevenueSummary.md) |  | [optional] 
**entitlement_overage_revenue_summary** | [**EntitlementOverageRevenueSummary**](EntitlementOverageRevenueSummary.md) |  | [optional] 
**slab_revenue_summaries** | [**List[SlabRevenueSummary]**](SlabRevenueSummary.md) |  | [optional] 

## Example

```python
from togai_client.models.revenue_info import RevenueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueInfo from a JSON string
revenue_info_instance = RevenueInfo.from_json(json)
# print the JSON string representation of the object
print(RevenueInfo.to_json())

# convert the object into a dict
revenue_info_dict = revenue_info_instance.to_dict()
# create an instance of RevenueInfo from a dict
revenue_info_from_dict = RevenueInfo.from_dict(revenue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


