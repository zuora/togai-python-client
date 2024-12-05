# EventPipelineInfoRevenueDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_meter_id** | **str** |  | 
**revenue_base_currency** | **float** |  | 
**revenue_invoice_currency** | **float** |  | 

## Example

```python
from togai_client.models.event_pipeline_info_revenue_details import EventPipelineInfoRevenueDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoRevenueDetails from a JSON string
event_pipeline_info_revenue_details_instance = EventPipelineInfoRevenueDetails.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoRevenueDetails.to_json())

# convert the object into a dict
event_pipeline_info_revenue_details_dict = event_pipeline_info_revenue_details_instance.to_dict()
# create an instance of EventPipelineInfoRevenueDetails from a dict
event_pipeline_info_revenue_details_from_dict = EventPipelineInfoRevenueDetails.from_dict(event_pipeline_info_revenue_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


