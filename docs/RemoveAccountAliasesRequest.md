# RemoveAccountAliasesRequest

Payload to remove account aliases

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** |  | [optional] 
**account_aliases** | [**List[RemoveAccountAliasRequest]**](RemoveAccountAliasRequest.md) |  | [optional] 

## Example

```python
from togai_client.models.remove_account_aliases_request import RemoveAccountAliasesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAccountAliasesRequest from a JSON string
remove_account_aliases_request_instance = RemoveAccountAliasesRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveAccountAliasesRequest.to_json())

# convert the object into a dict
remove_account_aliases_request_dict = remove_account_aliases_request_instance.to_dict()
# create an instance of RemoveAccountAliasesRequest from a dict
remove_account_aliases_request_from_dict = RemoveAccountAliasesRequest.from_dict(remove_account_aliases_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


