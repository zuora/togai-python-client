# UpdateAddOnRequest

Request to update an addon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of addon | [optional] 
**billable_name** | **str** | Billable name of addon. Billable name takes precedence over name to display in invoice. | [optional] 

## Example

```python
from togai_client.models.update_add_on_request import UpdateAddOnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAddOnRequest from a JSON string
update_add_on_request_instance = UpdateAddOnRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAddOnRequest.to_json())

# convert the object into a dict
update_add_on_request_dict = update_add_on_request_instance.to_dict()
# create an instance of UpdateAddOnRequest from a dict
update_add_on_request_from_dict = UpdateAddOnRequest.from_dict(update_add_on_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


