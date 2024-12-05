# InvoiceGroupPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InvoiceGroups]**](InvoiceGroups.md) |  | [optional] 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.invoice_group_paginated_response import InvoiceGroupPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGroupPaginatedResponse from a JSON string
invoice_group_paginated_response_instance = InvoiceGroupPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceGroupPaginatedResponse.to_json())

# convert the object into a dict
invoice_group_paginated_response_dict = invoice_group_paginated_response_instance.to_dict()
# create an instance of InvoiceGroupPaginatedResponse from a dict
invoice_group_paginated_response_from_dict = InvoiceGroupPaginatedResponse.from_dict(invoice_group_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


