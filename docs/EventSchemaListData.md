# EventSchemaListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event. Must be unique for an organization. | 
**description** | **str** | Description of the event | [optional] 
**version** | **int** | Version of event schema | 
**status** | **str** | Status of event schema * DRAFT - Schema is in draft state  * ACTIVE - Schema is currently active  * INACTIVE - Schema is currently inactive * ARCHIVED - Older version of event schema  | [optional] 
**attributes** | [**List[EventAttributeSchema]**](EventAttributeSchema.md) |  | [optional] 
**dimensions** | [**List[DimensionsSchema]**](DimensionsSchema.md) |  | [optional] 
**filter_fields** | **List[str]** |  | [optional] 
**feature_details** | [**FeatureDetails**](FeatureDetails.md) |  | [optional] 
**enrichments** | [**Enrichments**](Enrichments.md) |  | [optional] 
**event_id_template** | **str** | Template used to generate event id based on event payload | [optional] 
**event_level_revenue** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**usage_meters_count** | **int** |  | [optional] 

## Example

```python
from togai_client.models.event_schema_list_data import EventSchemaListData

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaListData from a JSON string
event_schema_list_data_instance = EventSchemaListData.from_json(json)
# print the JSON string representation of the object
print(EventSchemaListData.to_json())

# convert the object into a dict
event_schema_list_data_dict = event_schema_list_data_instance.to_dict()
# create an instance of EventSchemaListData from a dict
event_schema_list_data_from_dict = EventSchemaListData.from_dict(event_schema_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


