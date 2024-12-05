# InvoiceGroupAccountsPaginatedResponse


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
**accounts** | **List[str]** |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.invoice_group_accounts_paginated_response import InvoiceGroupAccountsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGroupAccountsPaginatedResponse from a JSON string
invoice_group_accounts_paginated_response_instance = InvoiceGroupAccountsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceGroupAccountsPaginatedResponse.to_json())

# convert the object into a dict
invoice_group_accounts_paginated_response_dict = invoice_group_accounts_paginated_response_instance.to_dict()
# create an instance of InvoiceGroupAccountsPaginatedResponse from a dict
invoice_group_accounts_paginated_response_from_dict = InvoiceGroupAccountsPaginatedResponse.from_dict(invoice_group_accounts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


