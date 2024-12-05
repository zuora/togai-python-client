# AccountAlias

Account Alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Alias identifier (UUID) | 
**value** | **str** | Alias value | 
**effective_from** | **datetime** | Effective from date | 
**effective_until** | **datetime** | Effective until date | 
**created_at** | **datetime** | Alias creation date | 
**updated_at** | **datetime** | Alias update date | [optional] 

## Example

```python
from togai_client.models.account_alias import AccountAlias

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAlias from a JSON string
account_alias_instance = AccountAlias.from_json(json)
# print the JSON string representation of the object
print(AccountAlias.to_json())

# convert the object into a dict
account_alias_dict = account_alias_instance.to_dict()
# create an instance of AccountAlias from a dict
account_alias_from_dict = AccountAlias.from_dict(account_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


