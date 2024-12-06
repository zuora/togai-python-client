# GetEntitlementValuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetEntitlementValuesResponseDataInner]**](GetEntitlementValuesResponseDataInner.md) |  | 

## Example

```python
from togai_client.models.get_entitlement_values_response import GetEntitlementValuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntitlementValuesResponse from a JSON string
get_entitlement_values_response_instance = GetEntitlementValuesResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntitlementValuesResponse.to_json())

# convert the object into a dict
get_entitlement_values_response_dict = get_entitlement_values_response_instance.to_dict()
# create an instance of GetEntitlementValuesResponse from a dict
get_entitlement_values_response_from_dict = GetEntitlementValuesResponse.from_dict(get_entitlement_values_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


