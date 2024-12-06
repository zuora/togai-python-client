# EventPipelineInfoAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**alias** | **str** |  | [optional] 

## Example

```python
from togai_client.models.event_pipeline_info_account import EventPipelineInfoAccount

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoAccount from a JSON string
event_pipeline_info_account_instance = EventPipelineInfoAccount.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoAccount.to_json())

# convert the object into a dict
event_pipeline_info_account_dict = event_pipeline_info_account_instance.to_dict()
# create an instance of EventPipelineInfoAccount from a dict
event_pipeline_info_account_from_dict = EventPipelineInfoAccount.from_dict(event_pipeline_info_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


