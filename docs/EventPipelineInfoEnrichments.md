# EventPipelineInfoEnrichments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[EnrichedField]**](EnrichedField.md) |  | [optional] 
**dimensions** | [**List[EnrichedField]**](EnrichedField.md) |  | [optional] 
**dependencies** | [**List[EnrichmentDependency]**](EnrichmentDependency.md) |  | [optional] 

## Example

```python
from togai_client.models.event_pipeline_info_enrichments import EventPipelineInfoEnrichments

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoEnrichments from a JSON string
event_pipeline_info_enrichments_instance = EventPipelineInfoEnrichments.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoEnrichments.to_json())

# convert the object into a dict
event_pipeline_info_enrichments_dict = event_pipeline_info_enrichments_instance.to_dict()
# create an instance of EventPipelineInfoEnrichments from a dict
event_pipeline_info_enrichments_from_dict = EventPipelineInfoEnrichments.from_dict(event_pipeline_info_enrichments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


