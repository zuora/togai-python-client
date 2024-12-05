# EventSchemaVersionsResponse

Response for event schema versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventSchema]**](EventSchema.md) |  | 

## Example

```python
from togai_client.models.event_schema_versions_response import EventSchemaVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaVersionsResponse from a JSON string
event_schema_versions_response_instance = EventSchemaVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(EventSchemaVersionsResponse.to_json())

# convert the object into a dict
event_schema_versions_response_dict = event_schema_versions_response_instance.to_dict()
# create an instance of EventSchemaVersionsResponse from a dict
event_schema_versions_response_from_dict = EventSchemaVersionsResponse.from_dict(event_schema_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


