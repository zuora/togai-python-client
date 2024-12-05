# CreatePaymentRequest

payload to create payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A brief description of the payment | [optional] 
**notes** | **str** | A detailed note about the payment | [optional] 
**account_id** | **str** |  | 
**external_payment_reference** | [**ExternalPaymentReference**](ExternalPaymentReference.md) |  | 
**line_item_records** | [**List[PaymentLineItemRecord]**](PaymentLineItemRecord.md) |  | 
**currency** | **str** |  | 
**total_amount** | **float** |  | 

## Example

```python
from togai_client.models.create_payment_request import CreatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentRequest from a JSON string
create_payment_request_instance = CreatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentRequest.to_json())

# convert the object into a dict
create_payment_request_dict = create_payment_request_instance.to_dict()
# create an instance of CreatePaymentRequest from a dict
create_payment_request_from_dict = CreatePaymentRequest.from_dict(create_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


