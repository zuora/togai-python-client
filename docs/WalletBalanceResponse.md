# WalletBalanceResponse

Wallet Balance response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**customer_id** | **str** |  | 
**balance** | **float** | This amount is the difference of total credited amount and sum of consumed, hold amount. ie. credit amount - (consumed amount + hold amount)  | 
**credit_unit** | **str** |  | 
**external_id** | **str** |  | [optional] 
**status** | [**WalletStatus**](WalletStatus.md) |  | 
**hold_amount** | **float** |  | [optional] 
**effective_from** | **datetime** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from togai_client.models.wallet_balance_response import WalletBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletBalanceResponse from a JSON string
wallet_balance_response_instance = WalletBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(WalletBalanceResponse.to_json())

# convert the object into a dict
wallet_balance_response_dict = wallet_balance_response_instance.to_dict()
# create an instance of WalletBalanceResponse from a dict
wallet_balance_response_from_dict = WalletBalanceResponse.from_dict(wallet_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


