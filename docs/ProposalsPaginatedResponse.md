# ProposalsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProposalsListResponse]**](ProposalsListResponse.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.proposals_paginated_response import ProposalsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProposalsPaginatedResponse from a JSON string
proposals_paginated_response_instance = ProposalsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(ProposalsPaginatedResponse.to_json())

# convert the object into a dict
proposals_paginated_response_dict = proposals_paginated_response_instance.to_dict()
# create an instance of ProposalsPaginatedResponse from a dict
proposals_paginated_response_from_dict = ProposalsPaginatedResponse.from_dict(proposals_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


