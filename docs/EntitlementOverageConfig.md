# EntitlementOverageConfig

Configuration for getting the entitlement overages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the entitlement overages for the entitlement overage rate cards - CUSTOM: Use the entitlement overages provided in the request - LOOKUP_CYCLE: Use the entitlement overages of a given account for the specified cycle  | 
**custom** | [**List[EntitlementOverageEntry]**](EntitlementOverageEntry.md) | Quantity of entitlement overages, this will be considered if mode is CUSTOM | [optional] 
**lookup_cycle** | [**EntitlementOverageConfigLookupCycle**](EntitlementOverageConfigLookupCycle.md) |  | [optional] 

## Example

```python
from togai_client.models.entitlement_overage_config import EntitlementOverageConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverageConfig from a JSON string
entitlement_overage_config_instance = EntitlementOverageConfig.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverageConfig.to_json())

# convert the object into a dict
entitlement_overage_config_dict = entitlement_overage_config_instance.to_dict()
# create an instance of EntitlementOverageConfig from a dict
entitlement_overage_config_from_dict = EntitlementOverageConfig.from_dict(entitlement_overage_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


