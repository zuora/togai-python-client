# UpdateEventSchemaRequest

Request to update event schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the event | [optional] 
**attributes** | [**List[EventAttributeSchema]**](EventAttributeSchema.md) |  | [optional] 
**dimensions** | [**List[DimensionsSchema]**](DimensionsSchema.md) |  | [optional] 
**enrichments** | [**Enrichments**](Enrichments.md) |  | [optional] 
**filter_fields** | **List[str]** | List of fields that can be used for filtering in usage meter | [optional] 
**event_id_template** | **str** | Template used to generate event id based on event payload | [optional] 

## Example

```python
from togai_client.models.update_event_schema_request import UpdateEventSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEventSchemaRequest from a JSON string
update_event_schema_request_instance = UpdateEventSchemaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEventSchemaRequest.to_json())

# convert the object into a dict
update_event_schema_request_dict = update_event_schema_request_instance.to_dict()
# create an instance of UpdateEventSchemaRequest from a dict
update_event_schema_request_from_dict = UpdateEventSchemaRequest.from_dict(update_event_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


