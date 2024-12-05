# UpdateInvoiceRequest

Payload to update an invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**status** | **str** | Status of invoice | [optional] 
**line_items** | [**List[CustomInvoiceLineItem]**](CustomInvoiceLineItem.md) |  | [optional] 
**auto_advance** | **bool** | This property defines the behaviour of status updates of invoices like: Enabling this property to true auto updates the status of invoice to DUE or PAID accordingly But disabling this property of left null does not auto update the custom status  | [optional] 

## Example

```python
from togai_client.models.update_invoice_request import UpdateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoiceRequest from a JSON string
update_invoice_request_instance = UpdateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInvoiceRequest.to_json())

# convert the object into a dict
update_invoice_request_dict = update_invoice_request_instance.to_dict()
# create an instance of UpdateInvoiceRequest from a dict
update_invoice_request_from_dict = UpdateInvoiceRequest.from_dict(update_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


