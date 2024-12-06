# CreateCustomInvoiceRequest

Payload to create invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**owner_type** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**idempotency_key** | **str** |  | [optional] 
**status** | **str** | Status to create an invoice in. | 
**line_items** | [**List[CustomInvoiceLineItem]**](CustomInvoiceLineItem.md) |  | 
**auto_advance** | **bool** | This property defines the behaviour of status transition of the invoice. If true, invoice auto transitions from &#x60;DRAFT&#x60; to &#x60;DUE&#x60; or &#x60;PAID&#x60; at the end of pricing cycle. If false, the invoice’s state doesn’t automatically advance without an explicit action. Default: false  | [optional] 
**apply_credits** | **bool** | This property defines the behaviour of whether or not to use credits to net off with the invoice amount. Default: true  | [optional] 
**apply_wallet_balance** | **bool** | This property defines the behaviour of whether or not to use wallet amount to net off with the invoice amount. Default: true  | [optional] 

## Example

```python
from togai_client.models.create_custom_invoice_request import CreateCustomInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomInvoiceRequest from a JSON string
create_custom_invoice_request_instance = CreateCustomInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomInvoiceRequest.to_json())

# convert the object into a dict
create_custom_invoice_request_dict = create_custom_invoice_request_instance.to_dict()
# create an instance of CreateCustomInvoiceRequest from a dict
create_custom_invoice_request_from_dict = CreateCustomInvoiceRequest.from_dict(create_custom_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


