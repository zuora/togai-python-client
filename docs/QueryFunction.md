# QueryFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**args** | **List[str]** |  | 

## Example

```python
from togai_client.models.query_function import QueryFunction

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFunction from a JSON string
query_function_instance = QueryFunction.from_json(json)
# print the JSON string representation of the object
print(QueryFunction.to_json())

# convert the object into a dict
query_function_dict = query_function_instance.to_dict()
# create an instance of QueryFunction from a dict
query_function_from_dict = QueryFunction.from_dict(query_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


