# InvoiceDetailsCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**primary_email** | **str** |  | 
**billing_address** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from togai_client.models.invoice_details_customer import InvoiceDetailsCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsCustomer from a JSON string
invoice_details_customer_instance = InvoiceDetailsCustomer.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsCustomer.to_json())

# convert the object into a dict
invoice_details_customer_dict = invoice_details_customer_instance.to_dict()
# create an instance of InvoiceDetailsCustomer from a dict
invoice_details_customer_from_dict = InvoiceDetailsCustomer.from_dict(invoice_details_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


