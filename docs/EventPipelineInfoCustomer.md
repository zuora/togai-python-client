# EventPipelineInfoCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from togai_client.models.event_pipeline_info_customer import EventPipelineInfoCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of EventPipelineInfoCustomer from a JSON string
event_pipeline_info_customer_instance = EventPipelineInfoCustomer.from_json(json)
# print the JSON string representation of the object
print(EventPipelineInfoCustomer.to_json())

# convert the object into a dict
event_pipeline_info_customer_dict = event_pipeline_info_customer_instance.to_dict()
# create an instance of EventPipelineInfoCustomer from a dict
event_pipeline_info_customer_from_dict = EventPipelineInfoCustomer.from_dict(event_pipeline_info_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


