# IngestEventRequest

Payload for ingesting events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**Event**](Event.md) |  | 

## Example

```python
from togai_client.models.ingest_event_request import IngestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IngestEventRequest from a JSON string
ingest_event_request_instance = IngestEventRequest.from_json(json)
# print the JSON string representation of the object
print(IngestEventRequest.to_json())

# convert the object into a dict
ingest_event_request_dict = ingest_event_request_instance.to_dict()
# create an instance of IngestEventRequest from a dict
ingest_event_request_from_dict = IngestEventRequest.from_dict(ingest_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


