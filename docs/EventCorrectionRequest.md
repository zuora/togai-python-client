# EventCorrectionRequest

Event Correction Payload for event correction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**Event**](Event.md) |  | [optional] 

## Example

```python
from togai_client.models.event_correction_request import EventCorrectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventCorrectionRequest from a JSON string
event_correction_request_instance = EventCorrectionRequest.from_json(json)
# print the JSON string representation of the object
print(EventCorrectionRequest.to_json())

# convert the object into a dict
event_correction_request_dict = event_correction_request_instance.to_dict()
# create an instance of EventCorrectionRequest from a dict
event_correction_request_from_dict = EventCorrectionRequest.from_dict(event_correction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


