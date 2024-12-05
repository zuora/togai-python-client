# WalletEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of credit transactions | 
**description** | **str** | description of the entry | [optional] 
**wallet_id** | **str** |  | 
**transaction_type** | **str** |  | 
**status** | **str** |  | 
**entity_id** | **str** |  | [optional] 
**amount** | **float** |  | 
**created_at** | **datetime** |  | 
**closing_balance** | **float** |  | 

## Example

```python
from togai_client.models.wallet_entry import WalletEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WalletEntry from a JSON string
wallet_entry_instance = WalletEntry.from_json(json)
# print the JSON string representation of the object
print(WalletEntry.to_json())

# convert the object into a dict
wallet_entry_dict = wallet_entry_instance.to_dict()
# create an instance of WalletEntry from a dict
wallet_entry_from_dict = WalletEntry.from_dict(wallet_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


