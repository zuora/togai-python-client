# GetEntitlementValuesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** | Feature ID | 
**value** | **str** | Value of the feature | 

## Example

```python
from togai_client.models.get_entitlement_values_response_data_inner import GetEntitlementValuesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntitlementValuesResponseDataInner from a JSON string
get_entitlement_values_response_data_inner_instance = GetEntitlementValuesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetEntitlementValuesResponseDataInner.to_json())

# convert the object into a dict
get_entitlement_values_response_data_inner_dict = get_entitlement_values_response_data_inner_instance.to_dict()
# create an instance of GetEntitlementValuesResponseDataInner from a dict
get_entitlement_values_response_data_inner_from_dict = GetEntitlementValuesResponseDataInner.from_dict(get_entitlement_values_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


