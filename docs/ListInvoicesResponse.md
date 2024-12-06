# ListInvoicesResponse

List invoices response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InvoiceSummary]**](InvoiceSummary.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.list_invoices_response import ListInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoicesResponse from a JSON string
list_invoices_response_instance = ListInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(ListInvoicesResponse.to_json())

# convert the object into a dict
list_invoices_response_dict = list_invoices_response_instance.to_dict()
# create an instance of ListInvoicesResponse from a dict
list_invoices_response_from_dict = ListInvoicesResponse.from_dict(list_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


