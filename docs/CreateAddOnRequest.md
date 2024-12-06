# CreateAddOnRequest

Request to create an addon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of addon | 
**type** | [**AddOnType**](AddOnType.md) |  | 
**billable_name** | **str** | Billable name of addon. Billable name takes precedence over name to display in invoice. | [optional] 

## Example

```python
from togai_client.models.create_add_on_request import CreateAddOnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddOnRequest from a JSON string
create_add_on_request_instance = CreateAddOnRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAddOnRequest.to_json())

# convert the object into a dict
create_add_on_request_dict = create_add_on_request_instance.to_dict()
# create an instance of CreateAddOnRequest from a dict
create_add_on_request_from_dict = CreateAddOnRequest.from_dict(create_add_on_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


