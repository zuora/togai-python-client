# Payment

Payment object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**account_id** | **str** |  | 
**external_payment_references** | [**ExternalPaymentReference**](ExternalPaymentReference.md) |  | 
**line_item_records** | [**List[PaymentLineItemRecord]**](PaymentLineItemRecord.md) |  | 
**total_amount** | **float** |  | 
**currency** | **str** |  | 
**version** | **float** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from togai_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


