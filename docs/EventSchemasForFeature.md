# EventSchemasForFeature

event_schema details that are in association with feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_name** | **str** |  | 
**attribute_name** | **str** |  | 

## Example

```python
from togai_client.models.event_schemas_for_feature import EventSchemasForFeature

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemasForFeature from a JSON string
event_schemas_for_feature_instance = EventSchemasForFeature.from_json(json)
# print the JSON string representation of the object
print(EventSchemasForFeature.to_json())

# convert the object into a dict
event_schemas_for_feature_dict = event_schemas_for_feature_instance.to_dict()
# create an instance of EventSchemasForFeature from a dict
event_schemas_for_feature_from_dict = EventSchemasForFeature.from_dict(event_schemas_for_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


