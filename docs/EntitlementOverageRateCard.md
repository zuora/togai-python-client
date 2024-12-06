# EntitlementOverageRateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** | Unique Identifier of the attached Feature | 
**display_name** | **str** | Name to be displayed during invoice | [optional] 
**name** | **str** | Unique identifier for the rate card in a price plan. If left null it is auto-generated. | [optional] 
**tag** | **str** | A tag string to group rate cards | [optional] 
**max_quantity** | **float** | Maximum quantity allowed for the feature, if not specified, unlimited quantity is allowed | [optional] 
**rate_plan** | [**RatePlan**](RatePlan.md) |  | 
**rate_values** | [**List[RateValue]**](RateValue.md) |  | 
**billing_config** | [**BillingConfig**](BillingConfig.md) |  | [optional] 

## Example

```python
from togai_client.models.entitlement_overage_rate_card import EntitlementOverageRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverageRateCard from a JSON string
entitlement_overage_rate_card_instance = EntitlementOverageRateCard.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverageRateCard.to_json())

# convert the object into a dict
entitlement_overage_rate_card_dict = entitlement_overage_rate_card_instance.to_dict()
# create an instance of EntitlementOverageRateCard from a dict
entitlement_overage_rate_card_from_dict = EntitlementOverageRateCard.from_dict(entitlement_overage_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


