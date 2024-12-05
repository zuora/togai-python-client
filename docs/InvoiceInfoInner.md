# InvoiceInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the information | 
**value** | **str** | Value of the information | 

## Example

```python
from togai_client.models.invoice_info_inner import InvoiceInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceInfoInner from a JSON string
invoice_info_inner_instance = InvoiceInfoInner.from_json(json)
# print the JSON string representation of the object
print(InvoiceInfoInner.to_json())

# convert the object into a dict
invoice_info_inner_dict = invoice_info_inner_instance.to_dict()
# create an instance of InvoiceInfoInner from a dict
invoice_info_inner_from_dict = InvoiceInfoInner.from_dict(invoice_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


