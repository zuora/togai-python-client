# AddAccountAliasesRequest

Payload to add aliases from account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** | List of aliases to add | [optional] 
**account_aliases** | [**List[CreateAccountAliasRequest]**](CreateAccountAliasRequest.md) | List of account aliases to add | [optional] 

## Example

```python
from togai_client.models.add_account_aliases_request import AddAccountAliasesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAccountAliasesRequest from a JSON string
add_account_aliases_request_instance = AddAccountAliasesRequest.from_json(json)
# print the JSON string representation of the object
print(AddAccountAliasesRequest.to_json())

# convert the object into a dict
add_account_aliases_request_dict = add_account_aliases_request_instance.to_dict()
# create an instance of AddAccountAliasesRequest from a dict
add_account_aliases_request_from_dict = AddAccountAliasesRequest.from_dict(add_account_aliases_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


