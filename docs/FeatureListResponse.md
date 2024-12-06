# FeatureListResponse

Represents a Feature for List Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**billable_name** | **str** |  | [optional] 
**display_name** | **str** | Display name of feature. This is an auto-generated field which contains billableName of feature. If billableName is not provided, name will be used as display name.  | 
**schema_count** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from togai_client.models.feature_list_response import FeatureListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureListResponse from a JSON string
feature_list_response_instance = FeatureListResponse.from_json(json)
# print the JSON string representation of the object
print(FeatureListResponse.to_json())

# convert the object into a dict
feature_list_response_dict = feature_list_response_instance.to_dict()
# create an instance of FeatureListResponse from a dict
feature_list_response_from_dict = FeatureListResponse.from_dict(feature_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


