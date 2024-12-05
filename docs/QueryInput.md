# QueryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selects** | [**List[QueryColumn]**](QueryColumn.md) |  | 
**query_filters** | [**List[QueryFilter]**](QueryFilter.md) |  | [optional] 
**base_data_source** | **str** |  | 
**sort** | [**List[QueryInputSortInner]**](QueryInputSortInner.md) |  | 
**seek_values** | **List[str]** |  | [optional] 
**limit** | **int** |  | 

## Example

```python
from togai_client.models.query_input import QueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of QueryInput from a JSON string
query_input_instance = QueryInput.from_json(json)
# print the JSON string representation of the object
print(QueryInput.to_json())

# convert the object into a dict
query_input_dict = query_input_instance.to_dict()
# create an instance of QueryInput from a dict
query_input_from_dict = QueryInput.from_dict(query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


