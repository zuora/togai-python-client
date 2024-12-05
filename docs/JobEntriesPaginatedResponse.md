# JobEntriesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobEntriesResponse]**](JobEntriesResponse.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.job_entries_paginated_response import JobEntriesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobEntriesPaginatedResponse from a JSON string
job_entries_paginated_response_instance = JobEntriesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(JobEntriesPaginatedResponse.to_json())

# convert the object into a dict
job_entries_paginated_response_dict = job_entries_paginated_response_instance.to_dict()
# create an instance of JobEntriesPaginatedResponse from a dict
job_entries_paginated_response_from_dict = JobEntriesPaginatedResponse.from_dict(job_entries_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


