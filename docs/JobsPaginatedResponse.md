# JobsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobsWithoutStatusInfoResponse]**](JobsWithoutStatusInfoResponse.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.jobs_paginated_response import JobsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobsPaginatedResponse from a JSON string
jobs_paginated_response_instance = JobsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(JobsPaginatedResponse.to_json())

# convert the object into a dict
jobs_paginated_response_dict = jobs_paginated_response_instance.to_dict()
# create an instance of JobsPaginatedResponse from a dict
jobs_paginated_response_from_dict = JobsPaginatedResponse.from_dict(jobs_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


