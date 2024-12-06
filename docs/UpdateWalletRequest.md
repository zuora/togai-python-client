# UpdateWalletRequest

Payload to update wallet of an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** |  | [optional] 
**status** | [**WalletStatus**](WalletStatus.md) |  | [optional] 

## Example

```python
from togai_client.models.update_wallet_request import UpdateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletRequest from a JSON string
update_wallet_request_instance = UpdateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletRequest.to_json())

# convert the object into a dict
update_wallet_request_dict = update_wallet_request_instance.to_dict()
# create an instance of UpdateWalletRequest from a dict
update_wallet_request_from_dict = UpdateWalletRequest.from_dict(update_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


