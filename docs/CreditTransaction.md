# CreditTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of credit transactions | 
**credit_id** | **str** |  | 
**transaction_type** | **str** |  | 
**invoice_id** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**amount** | **float** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from togai_client.models.credit_transaction import CreditTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CreditTransaction from a JSON string
credit_transaction_instance = CreditTransaction.from_json(json)
# print the JSON string representation of the object
print(CreditTransaction.to_json())

# convert the object into a dict
credit_transaction_dict = credit_transaction_instance.to_dict()
# create an instance of CreditTransaction from a dict
credit_transaction_from_dict = CreditTransaction.from_dict(credit_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


