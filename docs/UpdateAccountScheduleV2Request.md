# UpdateAccountScheduleV2Request

Request to dis/associate one or more schedules to an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode of request to create dis/association | [optional] 
**effective_from** | **date** | Date of effectiveness of the association. The date is expected in YYYY-MM-DD format - Editing of a BILLING plan with deferredRevenue can be achieved with    effectiveFrom as start date of current cycle or using &#x60;retainStartOffset&#x60; option.  | 
**effective_until** | **date** | Date until which the association must be effective. The date is expected in YYYY-MM-DD format  | 
**association_config** | [**AssociationConfig**](AssociationConfig.md) |  | [optional] 
**merge_schedules** | **bool** | If this flag is true, the schedules will be merged with the existing schedules of the account if possible. If this flag is false, the existing schedules will be replaced with the new schedules. Default value is false  | [optional] 

## Example

```python
from togai_client.models.update_account_schedule_v2_request import UpdateAccountScheduleV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountScheduleV2Request from a JSON string
update_account_schedule_v2_request_instance = UpdateAccountScheduleV2Request.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountScheduleV2Request.to_json())

# convert the object into a dict
update_account_schedule_v2_request_dict = update_account_schedule_v2_request_instance.to_dict()
# create an instance of UpdateAccountScheduleV2Request from a dict
update_account_schedule_v2_request_from_dict = UpdateAccountScheduleV2Request.from_dict(update_account_schedule_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


