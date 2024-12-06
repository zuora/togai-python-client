# CreateAccountRequest

Payload to create account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the account | 
**name** | **str** | Name of the Account | 
**invoice_currency** | **str** | Use [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code in which the account must be invoiced.   For example: AED is the currency code for United Arab Emirates dirham.  | [optional] 
**aliases** | **List[str]** | Aliases are tags that are associated with an account. Multiple aliases are allowed for a single account. | [optional] 
**account_aliases** | [**List[CreateAccountAliasRequest]**](CreateAccountAliasRequest.md) | Aliases which effective range | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**primary_email** | **str** | Primary email of the account | [optional] 
**billing_information** | [**AccountsBillingInformation**](AccountsBillingInformation.md) |  | [optional] 
**settings** | [**List[CreateEntitySetting]**](CreateEntitySetting.md) |  | [optional] 
**net_term_days** | **int** | Net term for the invoices of the account | [optional] 
**metadata** | **Dict[str, str]** | Additional information associated with the account. Example: GSTN, VATN  | [optional] 
**tags** | **List[str]** | Tag for accounts are stored in lowercase | [optional] 
**status** | **str** | Status of the created account defaults to ACTIVE | [optional] 
**customer_id** | **str** | Customer Identifier for whom the account is being created | 

## Example

```python
from togai_client.models.create_account_request import CreateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountRequest from a JSON string
create_account_request_instance = CreateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccountRequest.to_json())

# convert the object into a dict
create_account_request_dict = create_account_request_instance.to_dict()
# create an instance of CreateAccountRequest from a dict
create_account_request_from_dict = CreateAccountRequest.from_dict(create_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


