# CreateEventSchemaRequest

Request to create event schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event. Must be unique for an organization. | 
**description** | **str** | Description of the event | [optional] 
**attributes** | [**List[EventAttributeSchema]**](EventAttributeSchema.md) |  | 
**dimensions** | [**List[DimensionsSchema]**](DimensionsSchema.md) |  | 
**enrichments** | [**Enrichments**](Enrichments.md) |  | [optional] 
**filter_fields** | **List[str]** | List of fields that can be used for filtering in usage meter | [optional] 
**event_id_template** | **str** | Template used to generate event id based on event payload | [optional] 

## Example

```python
from togai_client.models.create_event_schema_request import CreateEventSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventSchemaRequest from a JSON string
create_event_schema_request_instance = CreateEventSchemaRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEventSchemaRequest.to_json())

# convert the object into a dict
create_event_schema_request_dict = create_event_schema_request_instance.to_dict()
# create an instance of CreateEventSchemaRequest from a dict
create_event_schema_request_from_dict = CreateEventSchemaRequest.from_dict(create_event_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


