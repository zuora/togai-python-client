# UpdateInvoiceGroupAccounts

Add accounts to an invoice group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **List[str]** |  | 

## Example

```python
from togai_client.models.update_invoice_group_accounts import UpdateInvoiceGroupAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoiceGroupAccounts from a JSON string
update_invoice_group_accounts_instance = UpdateInvoiceGroupAccounts.from_json(json)
# print the JSON string representation of the object
print(UpdateInvoiceGroupAccounts.to_json())

# convert the object into a dict
update_invoice_group_accounts_dict = update_invoice_group_accounts_instance.to_dict()
# create an instance of UpdateInvoiceGroupAccounts from a dict
update_invoice_group_accounts_from_dict = UpdateInvoiceGroupAccounts.from_dict(update_invoice_group_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


