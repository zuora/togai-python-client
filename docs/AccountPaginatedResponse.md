# AccountPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Account]**](Account.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.account_paginated_response import AccountPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPaginatedResponse from a JSON string
account_paginated_response_instance = AccountPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AccountPaginatedResponse.to_json())

# convert the object into a dict
account_paginated_response_dict = account_paginated_response_instance.to_dict()
# create an instance of AccountPaginatedResponse from a dict
account_paginated_response_from_dict = AccountPaginatedResponse.from_dict(account_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


