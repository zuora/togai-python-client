# MiscellaneousChargesResponse

Miscellaneous charges response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MiscellaneousCharge]**](MiscellaneousCharge.md) |  | 

## Example

```python
from togai_client.models.miscellaneous_charges_response import MiscellaneousChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MiscellaneousChargesResponse from a JSON string
miscellaneous_charges_response_instance = MiscellaneousChargesResponse.from_json(json)
# print the JSON string representation of the object
print(MiscellaneousChargesResponse.to_json())

# convert the object into a dict
miscellaneous_charges_response_dict = miscellaneous_charges_response_instance.to_dict()
# create an instance of MiscellaneousChargesResponse from a dict
miscellaneous_charges_response_from_dict = MiscellaneousChargesResponse.from_dict(miscellaneous_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


