# InvoiceDetailsInvoiceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | [optional] 
**daily_invoice_consolidation** | **bool** |  | 
**invoice_currency** | **str** |  | 
**address** | [**Address**](Address.md) |  | 

## Example

```python
from togai_client.models.invoice_details_invoice_group import InvoiceDetailsInvoiceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsInvoiceGroup from a JSON string
invoice_details_invoice_group_instance = InvoiceDetailsInvoiceGroup.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsInvoiceGroup.to_json())

# convert the object into a dict
invoice_details_invoice_group_dict = invoice_details_invoice_group_instance.to_dict()
# create an instance of InvoiceDetailsInvoiceGroup from a dict
invoice_details_invoice_group_from_dict = InvoiceDetailsInvoiceGroup.from_dict(invoice_details_invoice_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


