# GetEventsResponse

Get batch events response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventWithStatus]**](EventWithStatus.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.get_events_response import GetEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsResponse from a JSON string
get_events_response_instance = GetEventsResponse.from_json(json)
# print the JSON string representation of the object
print(GetEventsResponse.to_json())

# convert the object into a dict
get_events_response_dict = get_events_response_instance.to_dict()
# create an instance of GetEventsResponse from a dict
get_events_response_from_dict = GetEventsResponse.from_dict(get_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


