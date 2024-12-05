# EventPipelineInfoUsageMeters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**version** | **int** |  | 
**status** | **str** |  | 
**units** | **float** |  | [optional] 

## Example

```python
from togai_client.models.event_pipeline_info_usage_meters import EventPipelineInfoUsageMeters

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoUsageMeters from a JSON string
event_pipeline_info_usage_meters_instance = EventPipelineInfoUsageMeters.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoUsageMeters.to_json())

# convert the object into a dict
event_pipeline_info_usage_meters_dict = event_pipeline_info_usage_meters_instance.to_dict()
# create an instance of EventPipelineInfoUsageMeters from a dict
event_pipeline_info_usage_meters_from_dict = EventPipelineInfoUsageMeters.from_dict(event_pipeline_info_usage_meters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


