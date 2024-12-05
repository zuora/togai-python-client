# EntitlementOverageConfigLookupCycle

Billing cycle of entitlement overages to be looked up, this will be considered if mode is LOOKUP_CYCLE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle_end_date** | **datetime** | Effective date of the cycle, will be used to get the license entries of the cycle | 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.entitlement_overage_config_lookup_cycle import EntitlementOverageConfigLookupCycle

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverageConfigLookupCycle from a JSON string
entitlement_overage_config_lookup_cycle_instance = EntitlementOverageConfigLookupCycle.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverageConfigLookupCycle.to_json())

# convert the object into a dict
entitlement_overage_config_lookup_cycle_dict = entitlement_overage_config_lookup_cycle_instance.to_dict()
# create an instance of EntitlementOverageConfigLookupCycle from a dict
entitlement_overage_config_lookup_cycle_from_dict = EntitlementOverageConfigLookupCycle.from_dict(entitlement_overage_config_lookup_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


