# PaymentLineItemRecord

payment line item record object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**togai_id** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**order** | **int** |  | 

## Example

```python
from togai_client.models.payment_line_item_record import PaymentLineItemRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLineItemRecord from a JSON string
payment_line_item_record_instance = PaymentLineItemRecord.from_json(json)
# print the JSON string representation of the object
print(PaymentLineItemRecord.to_json())

# convert the object into a dict
payment_line_item_record_dict = payment_line_item_record_instance.to_dict()
# create an instance of PaymentLineItemRecord from a dict
payment_line_item_record_from_dict = PaymentLineItemRecord.from_dict(payment_line_item_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


