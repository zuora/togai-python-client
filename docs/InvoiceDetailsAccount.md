# InvoiceDetailsAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**invoice_currency** | **str** |  | 
**address** | [**Address**](Address.md) |  | 
**primary_email** | **str** |  | 

## Example

```python
from togai_client.models.invoice_details_account import InvoiceDetailsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsAccount from a JSON string
invoice_details_account_instance = InvoiceDetailsAccount.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsAccount.to_json())

# convert the object into a dict
invoice_details_account_dict = invoice_details_account_instance.to_dict()
# create an instance of InvoiceDetailsAccount from a dict
invoice_details_account_from_dict = InvoiceDetailsAccount.from_dict(invoice_details_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


