# WalletTopupDetails

Information related to wallet topup purchase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_amount** | **float** | Specifies the amount to be paid to top up wallet with the specified top up amount.  If left null, purchase amount will be same as top up amount  | [optional] 
**topup_amount** | **float** | Specifies the value to be topped up in the wallet | 

## Example

```python
from togai_client.models.wallet_topup_details import WalletTopupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletTopupDetails from a JSON string
wallet_topup_details_instance = WalletTopupDetails.from_json(json)
# print the JSON string representation of the object
print(WalletTopupDetails.to_json())

# convert the object into a dict
wallet_topup_details_dict = wallet_topup_details_instance.to_dict()
# create an instance of WalletTopupDetails from a dict
wallet_topup_details_from_dict = WalletTopupDetails.from_dict(wallet_topup_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


