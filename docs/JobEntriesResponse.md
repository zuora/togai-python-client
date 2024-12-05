# JobEntriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**job_id** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.job_entries_response import JobEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobEntriesResponse from a JSON string
job_entries_response_instance = JobEntriesResponse.from_json(json)
# print the JSON string representation of the object
print(JobEntriesResponse.to_json())

# convert the object into a dict
job_entries_response_dict = job_entries_response_instance.to_dict()
# create an instance of JobEntriesResponse from a dict
job_entries_response_from_dict = JobEntriesResponse.from_dict(job_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


