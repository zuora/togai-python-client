# QueryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | [**QueryColumn**](QueryColumn.md) |  | 
**operator** | **str** |  | 
**args** | **List[str]** |  | 

## Example

```python
from togai_client.models.query_filter import QueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilter from a JSON string
query_filter_instance = QueryFilter.from_json(json)
# print the JSON string representation of the object
print(QueryFilter.to_json())

# convert the object into a dict
query_filter_dict = query_filter_instance.to_dict()
# create an instance of QueryFilter from a dict
query_filter_from_dict = QueryFilter.from_dict(query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


