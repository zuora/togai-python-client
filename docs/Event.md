# Event

Contents of the event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_name** | **str** | Name of the Event Schema.  Know more about [event schema](https://docs.togai.com/docs/event-schemas)  | 
**id** | **str** | Togai restricts users to ingest events with same id within a period of *45 days*. This restriction is common for [/entitled API](/api-reference/entitlements/ingest-event-if-a-user-is-entitled-to-a-feature), [/ingest API](/api-reference/event-ingestion/ingest-events-to-togai) and [/ingestBatch API](/api-reference/event-ingestion/ingest-events-to-togai-in-batch). i.e, an id used on /ingest API will not be allowed on /ingestBatch or /entitled APIs | [optional] 
**timestamp** | **datetime** | Source time stamp of the event. This timestamp must be in ISO 8601 format. | 
**account_id** | **str** | The event will be associated with the provided account | 
**attributes** | [**List[Attribute]**](Attribute.md) | Attributes are numeric values. It can be usage metric which you push to Togai | 
**dimensions** | **Dict[str, str]** | Dimensions are tags/labels associated with the events. | 

## Example

```python
from togai_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


