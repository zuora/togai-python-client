# RemoveAccountAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Alias identifier (UUID) | 
**var_from** | **datetime** | Alias will be deleted from this date, If not provided, it will be deleted from now | [optional] 

## Example

```python
from togai_client.models.remove_account_alias_request import RemoveAccountAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAccountAliasRequest from a JSON string
remove_account_alias_request_instance = RemoveAccountAliasRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveAccountAliasRequest.to_json())

# convert the object into a dict
remove_account_alias_request_dict = remove_account_alias_request_instance.to_dict()
# create an instance of RemoveAccountAliasRequest from a dict
remove_account_alias_request_from_dict = RemoveAccountAliasRequest.from_dict(remove_account_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


