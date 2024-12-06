# EventPipelineInfoFeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** |  | 
**mapped_attribute** | **str** |  | 
**overage_in_cycle** | **float** |  | [optional] 
**overage_in_event** | **float** |  | [optional] 

## Example

```python
from togai_client.models.event_pipeline_info_feature_details import EventPipelineInfoFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoFeatureDetails from a JSON string
event_pipeline_info_feature_details_instance = EventPipelineInfoFeatureDetails.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoFeatureDetails.to_json())

# convert the object into a dict
event_pipeline_info_feature_details_dict = event_pipeline_info_feature_details_instance.to_dict()
# create an instance of EventPipelineInfoFeatureDetails from a dict
event_pipeline_info_feature_details_from_dict = EventPipelineInfoFeatureDetails.from_dict(event_pipeline_info_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


