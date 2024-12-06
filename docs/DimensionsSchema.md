# DimensionsSchema

Structure of dimensions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event dimension | 

## Example

```python
from togai_client.models.dimensions_schema import DimensionsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionsSchema from a JSON string
dimensions_schema_instance = DimensionsSchema.from_json(json)
# print the JSON string representation of the object
print(DimensionsSchema.to_json())

# convert the object into a dict
dimensions_schema_dict = dimensions_schema_instance.to_dict()
# create an instance of DimensionsSchema from a dict
dimensions_schema_from_dict = DimensionsSchema.from_dict(dimensions_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


