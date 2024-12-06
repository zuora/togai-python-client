# GetEventResponse

Get single event response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventWithStatusAndEventPipelineInfo]**](EventWithStatusAndEventPipelineInfo.md) |  | 

## Example

```python
from togai_client.models.get_event_response import GetEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventResponse from a JSON string
get_event_response_instance = GetEventResponse.from_json(json)
# print the JSON string representation of the object
print(GetEventResponse.to_json())

# convert the object into a dict
get_event_response_dict = get_event_response_instance.to_dict()
# create an instance of GetEventResponse from a dict
get_event_response_from_dict = GetEventResponse.from_dict(get_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


