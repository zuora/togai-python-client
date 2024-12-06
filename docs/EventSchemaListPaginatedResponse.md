# EventSchemaListPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventSchemaListData]**](EventSchemaListData.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.event_schema_list_paginated_response import EventSchemaListPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaListPaginatedResponse from a JSON string
event_schema_list_paginated_response_instance = EventSchemaListPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(EventSchemaListPaginatedResponse.to_json())

# convert the object into a dict
event_schema_list_paginated_response_dict = event_schema_list_paginated_response_instance.to_dict()
# create an instance of EventSchemaListPaginatedResponse from a dict
event_schema_list_paginated_response_from_dict = EventSchemaListPaginatedResponse.from_dict(event_schema_list_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


