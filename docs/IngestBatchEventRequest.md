# IngestBatchEventRequest

Payload for ingesting batch events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[Event]**](Event.md) |  | 

## Example

```python
from togai_client.models.ingest_batch_event_request import IngestBatchEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IngestBatchEventRequest from a JSON string
ingest_batch_event_request_instance = IngestBatchEventRequest.from_json(json)
# print the JSON string representation of the object
print(IngestBatchEventRequest.to_json())

# convert the object into a dict
ingest_batch_event_request_dict = ingest_batch_event_request_instance.to_dict()
# create an instance of IngestBatchEventRequest from a dict
ingest_batch_event_request_from_dict = IngestBatchEventRequest.from_dict(ingest_batch_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


