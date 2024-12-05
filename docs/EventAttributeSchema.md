# EventAttributeSchema

Structure of an event attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event attribute. | 
**default_unit** | **str** | Unit for the attribute | [optional] 

## Example

```python
from togai_client.models.event_attribute_schema import EventAttributeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttributeSchema from a JSON string
event_attribute_schema_instance = EventAttributeSchema.from_json(json)
# print the JSON string representation of the object
print(EventAttributeSchema.to_json())

# convert the object into a dict
event_attribute_schema_dict = event_attribute_schema_instance.to_dict()
# create an instance of EventAttributeSchema from a dict
event_attribute_schema_from_dict = EventAttributeSchema.from_dict(event_attribute_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


