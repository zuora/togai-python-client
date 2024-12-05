# EventPipelineInfoEventSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from togai_client.models.event_pipeline_info_event_schema import EventPipelineInfoEventSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoEventSchema from a JSON string
event_pipeline_info_event_schema_instance = EventPipelineInfoEventSchema.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoEventSchema.to_json())

# convert the object into a dict
event_pipeline_info_event_schema_dict = event_pipeline_info_event_schema_instance.to_dict()
# create an instance of EventPipelineInfoEventSchema from a dict
event_pipeline_info_event_schema_from_dict = EventPipelineInfoEventSchema.from_dict(event_pipeline_info_event_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


