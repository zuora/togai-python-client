# CreateFeatureRequest

Create a Feature stand-alone or associate it with schemas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the feature | 
**billable_name** | **str** | Billable name of feature. Billable name takes precedence over name to display in invoice. | [optional] 
**schema_associations** | [**List[EventSchemasForFeature]**](EventSchemasForFeature.md) | Association of a feature with event_schemas | 

## Example

```python
from togai_client.models.create_feature_request import CreateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeatureRequest from a JSON string
create_feature_request_instance = CreateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFeatureRequest.to_json())

# convert the object into a dict
create_feature_request_dict = create_feature_request_instance.to_dict()
# create an instance of CreateFeatureRequest from a dict
create_feature_request_from_dict = CreateFeatureRequest.from_dict(create_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


