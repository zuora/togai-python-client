# RateCardDetails

Rate card details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_fee_rate_card** | [**FixedFeeRateCard**](FixedFeeRateCard.md) |  | [optional] 
**billing_entitlement_rate_card** | [**BillingEntitlementRateCard**](BillingEntitlementRateCard.md) |  | [optional] 
**credit_grant_rate_card** | [**CreditGrantRateCard**](CreditGrantRateCard.md) |  | [optional] 
**usage_rate_card** | [**UsageRateCard**](UsageRateCard.md) |  | [optional] 
**license_rate_card** | [**LicenseRateCard**](LicenseRateCard.md) |  | [optional] 
**entitlement_overage_rate_card** | [**EntitlementOverageRateCard**](EntitlementOverageRateCard.md) |  | [optional] 
**minimum_commitment_rate_card** | [**MinimumCommitment**](MinimumCommitment.md) |  | [optional] 

## Example

```python
from togai_client.models.rate_card_details import RateCardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardDetails from a JSON string
rate_card_details_instance = RateCardDetails.from_json(json)
# print the JSON string representation of the object
print(RateCardDetails.to_json())

# convert the object into a dict
rate_card_details_dict = rate_card_details_instance.to_dict()
# create an instance of RateCardDetails from a dict
rate_card_details_from_dict = RateCardDetails.from_dict(rate_card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


