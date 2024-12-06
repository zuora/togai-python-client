# UpdateFeatureRequest

Update a Feature properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the feature | [optional] 
**billable_name** | **str** | Billable name of addon. Billable name takes precedence over name to display in invoice. | [optional] 
**schema_associations** | [**List[EventSchemasForFeature]**](EventSchemasForFeature.md) | Association of a feature with event_schemas | [optional] 

## Example

```python
from togai_client.models.update_feature_request import UpdateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureRequest from a JSON string
update_feature_request_instance = UpdateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureRequest.to_json())

# convert the object into a dict
update_feature_request_dict = update_feature_request_instance.to_dict()
# create an instance of UpdateFeatureRequest from a dict
update_feature_request_from_dict = UpdateFeatureRequest.from_dict(update_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


