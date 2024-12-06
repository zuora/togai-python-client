# AddOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of addon | 
**type** | [**AddOnType**](AddOnType.md) |  | 
**billable_name** | **str** | Billable name of addon. Billable name takes precedence over name to display in invoice. | [optional] 
**id** | **str** | Id of addon | 
**created_at** | **datetime** | Created Time of addon | 
**status** | **str** | status of addon | 
**display_name** | **str** | Display name of addon. This is an auto-generated field which contains billableName of addon. If billableName is not provided, name will be used as display name.  | 

## Example

```python
from togai_client.models.add_on import AddOn

# TODO update the JSON string below
json = "{}"
# create an instance of AddOn from a JSON string
add_on_instance = AddOn.from_json(json)
# print the JSON string representation of the object
print(AddOn.to_json())

# convert the object into a dict
add_on_dict = add_on_instance.to_dict()
# create an instance of AddOn from a dict
add_on_from_dict = AddOn.from_dict(add_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


