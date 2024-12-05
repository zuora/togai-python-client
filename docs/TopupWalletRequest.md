# TopupWalletRequest

Payload to topup wallet of an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topup_amount** | **float** |  | 

## Example

```python
from togai_client.models.topup_wallet_request import TopupWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TopupWalletRequest from a JSON string
topup_wallet_request_instance = TopupWalletRequest.from_json(json)
# print the JSON string representation of the object
print(TopupWalletRequest.to_json())

# convert the object into a dict
topup_wallet_request_dict = topup_wallet_request_instance.to_dict()
# create an instance of TopupWalletRequest from a dict
topup_wallet_request_from_dict = TopupWalletRequest.from_dict(topup_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


