# CreditBalanceResponse

Credit Balance response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_credits** | **float** |  | 
**available_balance** | **float** |  | 
**running_balance** | **float** |  | 
**inapplicable_credits** | **float** |  | 
**unit** | **str** |  | 
**last_updated_at** | **datetime** |  | 

## Example

```python
from togai_client.models.credit_balance_response import CreditBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditBalanceResponse from a JSON string
credit_balance_response_instance = CreditBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(CreditBalanceResponse.to_json())

# convert the object into a dict
credit_balance_response_dict = credit_balance_response_instance.to_dict()
# create an instance of CreditBalanceResponse from a dict
credit_balance_response_from_dict = CreditBalanceResponse.from_dict(credit_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


