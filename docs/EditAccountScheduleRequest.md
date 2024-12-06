# EditAccountScheduleRequest

Request to dis/associate one or more schedules to an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edits** | [**List[UpdateAccountScheduleV2Request]**](UpdateAccountScheduleV2Request.md) |  | 

## Example

```python
from togai_client.models.edit_account_schedule_request import EditAccountScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditAccountScheduleRequest from a JSON string
edit_account_schedule_request_instance = EditAccountScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(EditAccountScheduleRequest.to_json())

# convert the object into a dict
edit_account_schedule_request_dict = edit_account_schedule_request_instance.to_dict()
# create an instance of EditAccountScheduleRequest from a dict
edit_account_schedule_request_from_dict = EditAccountScheduleRequest.from_dict(edit_account_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


