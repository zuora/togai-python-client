# EntitlementOverageEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** |  | 
**quantity** | **float** |  | 

## Example

```python
from togai_client.models.entitlement_overage_entry import EntitlementOverageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverageEntry from a JSON string
entitlement_overage_entry_instance = EntitlementOverageEntry.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverageEntry.to_json())

# convert the object into a dict
entitlement_overage_entry_dict = entitlement_overage_entry_instance.to_dict()
# create an instance of EntitlementOverageEntry from a dict
entitlement_overage_entry_from_dict = EntitlementOverageEntry.from_dict(entitlement_overage_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


