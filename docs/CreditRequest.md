# CreditRequest

Payload to grant Credits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**purpose** | **str** |  | 
**applicable_entity_ids** | **List[str]** | List of entity ids for which the credit is applicable. If null or empty, the credit is applicable to all ids. This list can accept special values like: - ALL_USAGE_METER_RATE_CARDS: To apply the credit to all usage meter rate cards - ALL_FIXED_FEE_RATE_CARDS: To apply the credit to all fixed fee rate cards  | [optional] 
**effective_from** | **date** |  | 
**effective_until** | **date** |  | [optional] 
**credit_amount** | **float** |  | [optional] 
**priority** | **int** |  | 
**grantor_id** | **str** | The entity through which the credit has been granted | [optional] 
**idempotency_key** | **str** | The idempotency key for uniqueness of the credit record | [optional] 

## Example

```python
from togai_client.models.credit_request import CreditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditRequest from a JSON string
credit_request_instance = CreditRequest.from_json(json)
# print the JSON string representation of the object
print(CreditRequest.to_json())

# convert the object into a dict
credit_request_dict = credit_request_instance.to_dict()
# create an instance of CreditRequest from a dict
credit_request_from_dict = CreditRequest.from_dict(credit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


