# EventPipelineInfo

Information related to ingestion of an event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_schema** | [**EventPipelineInfoEventSchema**](EventPipelineInfoEventSchema.md) |  | [optional] 
**usage_meters** | [**List[EventPipelineInfoUsageMeters]**](EventPipelineInfoUsageMeters.md) |  | [optional] 
**price_plans** | [**List[EventPipelineInfoPricePlans]**](EventPipelineInfoPricePlans.md) |  | [optional] 
**account** | [**EventPipelineInfoAccount**](EventPipelineInfoAccount.md) |  | [optional] 
**customer** | [**EventPipelineInfoCustomer**](EventPipelineInfoCustomer.md) |  | [optional] 
**feature_details** | [**EventPipelineInfoFeatureDetails**](EventPipelineInfoFeatureDetails.md) |  | [optional] 
**enrichments** | [**EventPipelineInfoEnrichments**](EventPipelineInfoEnrichments.md) |  | [optional] 
**revenue_details** | [**List[EventPipelineInfoRevenueDetails]**](EventPipelineInfoRevenueDetails.md) |  | [optional] 
**status_before_reverting** | **str** |  | [optional] 
**base_currency** | **str** |  | [optional] 
**invoice_currency** | **str** |  | [optional] 

## Example

```python
from togai_client.models.event_pipeline_info import EventPipelineInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfo from a JSON string
event_pipeline_info_instance = EventPipelineInfo.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfo.to_json())

# convert the object into a dict
event_pipeline_info_dict = event_pipeline_info_instance.to_dict()
# create an instance of EventPipelineInfo from a dict
event_pipeline_info_from_dict = EventPipelineInfo.from_dict(event_pipeline_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


