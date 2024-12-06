# GetCustomerPortalDelegateTokenRequest

Request to get delegate token for customer portal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Identifier of the customer | 
**account_ids** | **List[str]** | Identifier of the accounts under the customer for which access is requested. Maximum of 5 account ids can be provided  | [optional] 
**all_accounts_access** | **bool** | Flag to specify if access for every account under the customer is required | [optional] 
**expiry** | **int** | Expiry in seconds from the time of generation.  If not provided, generated token will have the expiry of the token used for requesting.  | [optional] 

## Example

```python
from togai_client.models.get_customer_portal_delegate_token_request import GetCustomerPortalDelegateTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerPortalDelegateTokenRequest from a JSON string
get_customer_portal_delegate_token_request_instance = GetCustomerPortalDelegateTokenRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerPortalDelegateTokenRequest.to_json())

# convert the object into a dict
get_customer_portal_delegate_token_request_dict = get_customer_portal_delegate_token_request_instance.to_dict()
# create an instance of GetCustomerPortalDelegateTokenRequest from a dict
get_customer_portal_delegate_token_request_from_dict = GetCustomerPortalDelegateTokenRequest.from_dict(get_customer_portal_delegate_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


