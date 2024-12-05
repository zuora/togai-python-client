# Credit


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
**id** | **str** | Identifier of credits | 
**customer_id** | **str** |  | 
**status** | **str** |  | 
**credit_unit** | **str** |  | [optional] 
**hold_amount** | **float** |  | [optional] 
**consumed_amount** | **float** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from togai_client.models.credit import Credit

# TODO update the JSON string below
json = "{}"
# create an instance of Credit from a JSON string
credit_instance = Credit.from_json(json)
# print the JSON string representation of the object
print(Credit.to_json())

# convert the object into a dict
credit_dict = credit_instance.to_dict()
# create an instance of Credit from a dict
credit_from_dict = Credit.from_dict(credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

