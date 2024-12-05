# Invoice

Structure of invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of invoice | 
**customer_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**price_plan_id** | **str** |  | [optional] 
**usage_info** | [**List[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**revenue_info** | [**InvoiceLineItem**](InvoiceLineItem.md) |  | [optional] 
**invoice_details** | [**InvoiceDetails**](InvoiceDetails.md) |  | [optional] 
**status** | [**InvoicesStatus**](InvoicesStatus.md) |  | 
**finalizing_status** | **str** |  | [optional] 
**invoice_class** | [**InvoicesClass**](InvoicesClass.md) |  | 
**invoice_type** | [**InvoicesType**](InvoicesType.md) |  | 
**auto_advance** | **bool** |  | [optional] 
**start_date** | **datetime** | Start date of the invoice | [optional] 
**end_date** | **datetime** | End date of the invoice | [optional] 
**end_date_inclusive** | **datetime** | Inclusive end date of the invoice | [optional] 
**invoice_date** | **datetime** | Invoice date of the invoice | 
**due_date** | **datetime** | Due date of the invoice | [optional] 
**generated_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**info** | [**List[InvoiceInfoInner]**](InvoiceInfoInner.md) |  | [optional] 
**sequence_id** | **str** | Sequence id of the invoice | [optional] 
**pdf_url** | **str** | Download URL of the pdf file corresponding to the invoice | [optional] 
**total_amount** | **float** |  | 
**paid_amount** | **float** |  | 
**net_term_days** | **int** | Number of days from the invoice date after which an invoice is considered overdue. | 

## Example

```python
from togai_client.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print(Invoice.to_json())

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_from_dict = Invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


