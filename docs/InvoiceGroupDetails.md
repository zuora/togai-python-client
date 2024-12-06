# InvoiceGroupDetails

Invoice group details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**daily_invoice_consolidation** | **bool** |  | 
**net_term_days** | **int** |  | [optional] 
**invoice_currency** | **str** |  | 
**billing_address** | [**Address**](Address.md) |  | 

## Example

```python
from togai_client.models.invoice_group_details import InvoiceGroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGroupDetails from a JSON string
invoice_group_details_instance = InvoiceGroupDetails.from_json(json)
# print the JSON string representation of the object
print(InvoiceGroupDetails.to_json())

# convert the object into a dict
invoice_group_details_dict = invoice_group_details_instance.to_dict()
# create an instance of InvoiceGroupDetails from a dict
invoice_group_details_from_dict = InvoiceGroupDetails.from_dict(invoice_group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


