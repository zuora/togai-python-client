# FinalizeAccountSchedules

Request to finalize account schedules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_schedules** | **bool** | If this flag is true, the schedules will be merged with the existing schedules of the account if possible. If this flag is false, the existing schedules will be replaced with the new schedules. Default value is false  | [optional] 
**pre_actions** | [**List[PreAction]**](PreAction.md) | Pre actions to be performed before association or disassociation | [optional] 

## Example

```python
from togai_client.models.finalize_account_schedules import FinalizeAccountSchedules

# TODO update the JSON string below
json = "{}"
# create an instance of FinalizeAccountSchedules from a JSON string
finalize_account_schedules_instance = FinalizeAccountSchedules.from_json(json)
# print the JSON string representation of the object
print(FinalizeAccountSchedules.to_json())

# convert the object into a dict
finalize_account_schedules_dict = finalize_account_schedules_instance.to_dict()
# create an instance of FinalizeAccountSchedules from a dict
finalize_account_schedules_from_dict = FinalizeAccountSchedules.from_dict(finalize_account_schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


