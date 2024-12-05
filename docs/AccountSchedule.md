# AccountSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**price_plan_id** | **str** |  | 
**version** | **int** |  | 
**deferred_revenue** | **bool** |  | 
**price_plan_info** | [**PricePlanInfo**](PricePlanInfo.md) |  | 
**account_schedule_info** | [**ScheduleInfo**](ScheduleInfo.md) |  | 
**is_overridden** | **bool** | Indicates whether the schedule is overridden. Note: A null value for this field does not imply that the schedule is not overridden.  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**allow_ongoing_cycle_updates** | **bool** |  | 

## Example

```python
from togai_client.models.account_schedule import AccountSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSchedule from a JSON string
account_schedule_instance = AccountSchedule.from_json(json)
# print the JSON string representation of the object
print(AccountSchedule.to_json())

# convert the object into a dict
account_schedule_dict = account_schedule_instance.to_dict()
# create an instance of AccountSchedule from a dict
account_schedule_from_dict = AccountSchedule.from_dict(account_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


