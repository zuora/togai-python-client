# Account

Structure of an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the account | 
**togai_account_id** | **str** | Unique identifier of the account | 
**togai_customer_id** | **str** | Unique identifier of the customer | 
**name** | **str** | Name of the Account | 
**customer_id** | **str** | Identifier of the customer | 
**invoice_currency** | **str** | [ISO_4217](https://en.wikipedia.org/wiki/ISO_4217) code of the currency in which the account must be invoiced Defaults to Base currency.  | [optional] 
**aliases** | [**List[AccountAliases]**](AccountAliases.md) | list of aliases of the account | [optional] 
**net_term_days** | **int** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**primary_email** | **str** | Primary email of the customer | [optional] 
**billing_information** | [**AccountsBillingInformation**](AccountsBillingInformation.md) |  | [optional] 
**status** | **str** | Status of the account | 
**settings** | [**List[CreateEntitySetting]**](CreateEntitySetting.md) |  | [optional] 
**invoice_group_details** | [**InvoiceGroupDetails**](InvoiceGroupDetails.md) |  | [optional] 
**metadata** | **Dict[str, str]** | Additional information associated with the account. Example: GSTN, VATN  | [optional] 
**tags** | **List[str]** | Tag for accounts are stored in lowercase | [optional] 

## Example

```python
from togai_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


