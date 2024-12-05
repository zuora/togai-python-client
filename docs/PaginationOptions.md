# PaginationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**sort_order** | **str** |  | [optional] 

## Example

```python
from togai_client.models.pagination_options import PaginationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationOptions from a JSON string
pagination_options_instance = PaginationOptions.from_json(json)
# print the JSON string representation of the object
print(PaginationOptions.to_json())

# convert the object into a dict
pagination_options_dict = pagination_options_instance.to_dict()
# create an instance of PaginationOptions from a dict
pagination_options_from_dict = PaginationOptions.from_dict(pagination_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


