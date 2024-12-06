# UpdateAccountRequest

Payload to update account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Account | [optional] 
**status** | **str** |  | [optional] 
**invoice_currency** | **str** | [ISO_4217](https://en.wikipedia.org/wiki/ISO_4217) code of the currency in which the account must be invoiced Defaults to Base currency.  | [optional] 
**net_term_days** | **int** |  | [optional] 
**primary_email** | **str** | Primary email of the account | [optional] 
**billing_information** | [**AccountsBillingInformation**](AccountsBillingInformation.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**metadata** | **Dict[str, str]** | Additional information associated with the account. Example: GSTN, VATN NOTE: This replaces the existing metadata if the metadata in the request is not null.  To remove all existing metadata, use empty object  | [optional] 
**tags** | **List[str]** | Tag for accounts are stored in lowercase | [optional] 

## Example

```python
from togai_client.models.update_account_request import UpdateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountRequest from a JSON string
update_account_request_instance = UpdateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountRequest.to_json())

# convert the object into a dict
update_account_request_dict = update_account_request_instance.to_dict()
# create an instance of UpdateAccountRequest from a dict
update_account_request_from_dict = UpdateAccountRequest.from_dict(update_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


