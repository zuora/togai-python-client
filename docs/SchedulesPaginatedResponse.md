# SchedulesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountSchedule]**](AccountSchedule.md) |  | 
**next_token** | **str** |  | [optional] 
**previous_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.schedules_paginated_response import SchedulesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulesPaginatedResponse from a JSON string
schedules_paginated_response_instance = SchedulesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulesPaginatedResponse.to_json())

# convert the object into a dict
schedules_paginated_response_dict = schedules_paginated_response_instance.to_dict()
# create an instance of SchedulesPaginatedResponse from a dict
schedules_paginated_response_from_dict = SchedulesPaginatedResponse.from_dict(schedules_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


