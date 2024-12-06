# EventPipelineInfoPricePlans


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**schedule_id** | **str** |  | 
**cycle_start** | **date** |  | 
**cycle_end** | **date** |  | 
**usage_meters** | **List[str]** |  | [optional] 

## Example

```python
from togai_client.models.event_pipeline_info_price_plans import EventPipelineInfoPricePlans

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoPricePlans from a JSON string
event_pipeline_info_price_plans_instance = EventPipelineInfoPricePlans.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoPricePlans.to_json())

# convert the object into a dict
event_pipeline_info_price_plans_dict = event_pipeline_info_price_plans_instance.to_dict()
# create an instance of EventPipelineInfoPricePlans from a dict
event_pipeline_info_price_plans_from_dict = EventPipelineInfoPricePlans.from_dict(event_pipeline_info_price_plans_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


