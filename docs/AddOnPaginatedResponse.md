# AddOnPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AddOn]**](AddOn.md) |  | 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.add_on_paginated_response import AddOnPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnPaginatedResponse from a JSON string
add_on_paginated_response_instance = AddOnPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AddOnPaginatedResponse.to_json())

# convert the object into a dict
add_on_paginated_response_dict = add_on_paginated_response_instance.to_dict()
# create an instance of AddOnPaginatedResponse from a dict
add_on_paginated_response_from_dict = AddOnPaginatedResponse.from_dict(add_on_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


