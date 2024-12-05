# EventsCorrectionResponse

Events Correction response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventCorrectionInfo]**](EventCorrectionInfo.md) |  | 

## Example

```python
from togai_client.models.events_correction_response import EventsCorrectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventsCorrectionResponse from a JSON string
events_correction_response_instance = EventsCorrectionResponse.from_json(json)
# print the JSON string representation of the object
print(EventsCorrectionResponse.to_json())

# convert the object into a dict
events_correction_response_dict = events_correction_response_instance.to_dict()
# create an instance of EventsCorrectionResponse from a dict
events_correction_response_from_dict = EventsCorrectionResponse.from_dict(events_correction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


