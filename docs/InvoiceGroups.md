# InvoiceGroups


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
**accounts_count** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from togai_client.models.invoice_groups import InvoiceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGroups from a JSON string
invoice_groups_instance = InvoiceGroups.from_json(json)
# print the JSON string representation of the object
print(InvoiceGroups.to_json())

# convert the object into a dict
invoice_groups_dict = invoice_groups_instance.to_dict()
# create an instance of InvoiceGroups from a dict
invoice_groups_from_dict = InvoiceGroups.from_dict(invoice_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


