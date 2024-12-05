# RevenueInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_card** | [**RateCard**](RateCard.md) |  | 
**usages** | **Dict[str, float]** |  | 
**fixed_fee_revenue_summary** | [**FixedFeeRevenueSummary**](FixedFeeRevenueSummary.md) |  | [optional] 
**license_revenue_summary** | [**List[SlabRevenueSummary]**](SlabRevenueSummary.md) |  | [optional] 
**billing_entitlement_revenue_summary** | [**BillingEntitlementRevenueSummary**](BillingEntitlementRevenueSummary.md) |  | [optional] 
**credit_grant_revenue_summary** | [**CreditGrantRevenueSummary**](CreditGrantRevenueSummary.md) |  | [optional] 
**entitlement_overage_revenue_summary** | [**EntitlementOverageRevenueSummary**](EntitlementOverageRevenueSummary.md) |  | [optional] 
**slab_revenue_summaries** | [**List[SlabRevenueSummary]**](SlabRevenueSummary.md) |  | [optional] 

## Example

```python
from togai_client.models.revenue_info_v2 import RevenueInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueInfoV2 from a JSON string
revenue_info_v2_instance = RevenueInfoV2.from_json(json)
# print the JSON string representation of the object
print(RevenueInfoV2.to_json())

# convert the object into a dict
revenue_info_v2_dict = revenue_info_v2_instance.to_dict()
# create an instance of RevenueInfoV2 from a dict
revenue_info_v2_from_dict = RevenueInfoV2.from_dict(revenue_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


