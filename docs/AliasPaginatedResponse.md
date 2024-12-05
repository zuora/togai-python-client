# AliasPaginatedResponse

Represents for list response of alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Alias]**](Alias.md) |  | [optional] 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.alias_paginated_response import AliasPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AliasPaginatedResponse from a JSON string
alias_paginated_response_instance = AliasPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AliasPaginatedResponse.to_json())

# convert the object into a dict
alias_paginated_response_dict = alias_paginated_response_instance.to_dict()
# create an instance of AliasPaginatedResponse from a dict
alias_paginated_response_from_dict = AliasPaginatedResponse.from_dict(alias_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


