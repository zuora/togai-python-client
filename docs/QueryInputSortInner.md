# QueryInputSortInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | [**QueryColumn**](QueryColumn.md) |  | 
**sort_order** | **str** |  | 

## Example

```python
from togai_client.models.query_input_sort_inner import QueryInputSortInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryInputSortInner from a JSON string
query_input_sort_inner_instance = QueryInputSortInner.from_json(json)
# print the JSON string representation of the object
print(QueryInputSortInner.to_json())

# convert the object into a dict
query_input_sort_inner_dict = query_input_sort_inner_instance.to_dict()
# create an instance of QueryInputSortInner from a dict
query_input_sort_inner_from_dict = QueryInputSortInner.from_dict(query_input_sort_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


