# WalletEntriesPaginatedResponse

List wallet entries response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WalletEntry]**](WalletEntry.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.wallet_entries_paginated_response import WalletEntriesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletEntriesPaginatedResponse from a JSON string
wallet_entries_paginated_response_instance = WalletEntriesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(WalletEntriesPaginatedResponse.to_json())

# convert the object into a dict
wallet_entries_paginated_response_dict = wallet_entries_paginated_response_instance.to_dict()
# create an instance of WalletEntriesPaginatedResponse from a dict
wallet_entries_paginated_response_from_dict = WalletEntriesPaginatedResponse.from_dict(wallet_entries_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


