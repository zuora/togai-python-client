# CustomInvoiceLineItem

Custom line item. Either `value` or `quantity` + `valuePerQuantity` is required. In case `quantity` and `valuePerQuantity` are provided, `value` is computed as (`quantity` X `valuePerQuantity`) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**value_per_quantity** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**value** | **float** |  | [optional] 
**billable_id** | **str** |  | [optional] 

## Example

```python
from togai_client.models.custom_invoice_line_item import CustomInvoiceLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoiceLineItem from a JSON string
custom_invoice_line_item_instance = CustomInvoiceLineItem.from_json(json)
# print the JSON string representation of the object
print(CustomInvoiceLineItem.to_json())

# convert the object into a dict
custom_invoice_line_item_dict = custom_invoice_line_item_instance.to_dict()
# create an instance of CustomInvoiceLineItem from a dict
custom_invoice_line_item_from_dict = CustomInvoiceLineItem.from_dict(custom_invoice_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


