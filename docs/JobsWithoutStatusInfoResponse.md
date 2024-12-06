# JobsWithoutStatusInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from togai_client.models.jobs_without_status_info_response import JobsWithoutStatusInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobsWithoutStatusInfoResponse from a JSON string
jobs_without_status_info_response_instance = JobsWithoutStatusInfoResponse.from_json(json)
# print the JSON string representation of the object
print(JobsWithoutStatusInfoResponse.to_json())

# convert the object into a dict
jobs_without_status_info_response_dict = jobs_without_status_info_response_instance.to_dict()
# create an instance of JobsWithoutStatusInfoResponse from a dict
jobs_without_status_info_response_from_dict = JobsWithoutStatusInfoResponse.from_dict(jobs_without_status_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


