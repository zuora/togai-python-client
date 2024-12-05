# AccountAliasesPaginatedResponse

Paginated response for account aliases

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountAlias]**](AccountAlias.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.account_aliases_paginated_response import AccountAliasesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAliasesPaginatedResponse from a JSON string
account_aliases_paginated_response_instance = AccountAliasesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AccountAliasesPaginatedResponse.to_json())

# convert the object into a dict
account_aliases_paginated_response_dict = account_aliases_paginated_response_instance.to_dict()
# create an instance of AccountAliasesPaginatedResponse from a dict
account_aliases_paginated_response_from_dict = AccountAliasesPaginatedResponse.from_dict(account_aliases_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


