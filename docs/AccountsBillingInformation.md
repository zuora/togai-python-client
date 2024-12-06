# AccountsBillingInformation

Billing information of an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_recipients** | **List[str]** |  | [optional] 
**additional_email_recipients** | **List[str]** |  | [optional] 

## Example

```python
from togai_client.models.accounts_billing_information import AccountsBillingInformation

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsBillingInformation from a JSON string
accounts_billing_information_instance = AccountsBillingInformation.from_json(json)
# print the JSON string representation of the object
print(AccountsBillingInformation.to_json())

# convert the object into a dict
accounts_billing_information_dict = accounts_billing_information_instance.to_dict()
# create an instance of AccountsBillingInformation from a dict
accounts_billing_information_from_dict = AccountsBillingInformation.from_dict(accounts_billing_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


