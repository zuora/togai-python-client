# Feature

Represents a Feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**billable_name** | **str** |  | [optional] 
**display_name** | **str** | Display name of feature. This is an auto-generated field which contains billableName of feature. If billableName is not provided, name will be used as display name.  | 
**schema_associations** | [**List[EventSchemasForFeature]**](EventSchemasForFeature.md) | Association of a feature with event_schemas | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from togai_client.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print(Feature.to_json())

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_from_dict = Feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


