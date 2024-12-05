# CreateInvoiceGroupRequest

Create an invoice group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**daily_invoice_consolidation** | **bool** |  | 
**account_ids** | **List[str]** |  | 
**net_term_days** | **int** |  | [optional] 
**address** | [**Address**](Address.md) |  | 

## Example

```python
from togai_client.models.create_invoice_group_request import CreateInvoiceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceGroupRequest from a JSON string
create_invoice_group_request_instance = CreateInvoiceGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceGroupRequest.to_json())

# convert the object into a dict
create_invoice_group_request_dict = create_invoice_group_request_instance.to_dict()
# create an instance of CreateInvoiceGroupRequest from a dict
create_invoice_group_request_from_dict = CreateInvoiceGroupRequest.from_dict(create_invoice_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


