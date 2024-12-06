# CreateAccountAliasRequest

An alternative account identifier for event ingestion with a defined effective duration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**effective_from** | **datetime** | Effective from date, if not provided, it will be set to -infinity | [optional] 
**effective_until** | **datetime** | Effective until date, if not provided, it will be set to +infinity | [optional] 

## Example

```python
from togai_client.models.create_account_alias_request import CreateAccountAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountAliasRequest from a JSON string
create_account_alias_request_instance = CreateAccountAliasRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccountAliasRequest.to_json())

# convert the object into a dict
create_account_alias_request_dict = create_account_alias_request_instance.to_dict()
# create an instance of CreateAccountAliasRequest from a dict
create_account_alias_request_from_dict = CreateAccountAliasRequest.from_dict(create_account_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


