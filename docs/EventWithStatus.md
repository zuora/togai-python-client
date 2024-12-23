# EventWithStatus

Raw usage event ingested by the business team and the status of the event ingestion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | Unique id generated by Togai to identify an event uniquely | 
**event_payload** | [**Event**](Event.md) |  | 
**ingestion_status** | [**IngestionStatus**](IngestionStatus.md) |  | 
**customer_id** | **str** | The associated account belongs to this customer | [optional] 
**source** | [**EventSource**](EventSource.md) |  | [optional] 
**created_at** | **datetime** | Created time stamp of the event. This timestamp must be in ISO 8601 format. | 

## Example

```python
from togai_client.models.event_with_status import EventWithStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EventWithStatus from a JSON string
event_with_status_instance = EventWithStatus.from_json(json)
# print the JSON string representation of the object
print(EventWithStatus.to_json())

# convert the object into a dict
event_with_status_dict = event_with_status_instance.to_dict()
# create an instance of EventWithStatus from a dict
event_with_status_from_dict = EventWithStatus.from_dict(event_with_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


