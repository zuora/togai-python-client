# ValidateEntitlementValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the entitlement | 

## Example

```python
from togai_client.models.validate_entitlement_value_request import ValidateEntitlementValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateEntitlementValueRequest from a JSON string
validate_entitlement_value_request_instance = ValidateEntitlementValueRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateEntitlementValueRequest.to_json())

# convert the object into a dict
validate_entitlement_value_request_dict = validate_entitlement_value_request_instance.to_dict()
# create an instance of ValidateEntitlementValueRequest from a dict
validate_entitlement_value_request_from_dict = ValidateEntitlementValueRequest.from_dict(validate_entitlement_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


