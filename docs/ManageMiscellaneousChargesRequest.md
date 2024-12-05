# ManageMiscellaneousChargesRequest

Payload to update custom line items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MiscellaneousCharge]**](MiscellaneousCharge.md) |  | 

## Example

```python
from togai_client.models.manage_miscellaneous_charges_request import ManageMiscellaneousChargesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManageMiscellaneousChargesRequest from a JSON string
manage_miscellaneous_charges_request_instance = ManageMiscellaneousChargesRequest.from_json(json)
# print the JSON string representation of the object
print(ManageMiscellaneousChargesRequest.to_json())

# convert the object into a dict
manage_miscellaneous_charges_request_dict = manage_miscellaneous_charges_request_instance.to_dict()
# create an instance of ManageMiscellaneousChargesRequest from a dict
manage_miscellaneous_charges_request_from_dict = ManageMiscellaneousChargesRequest.from_dict(manage_miscellaneous_charges_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


