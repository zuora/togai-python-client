# UpdateUsageMeterRequest

Request to update usage meter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of usage meter. | [optional] 
**billable_name** | **str** | Billable name of usage meter. Billable name takes precedence over name to display in invoice. | [optional] 
**description** | **str** | Description of the usage meter | [optional] 
**event_schema_name** | **str** | Event Schema Identifier | [optional] 
**type** | **str** | Type of usage meter * COUNTER - Count usage  | [optional] 
**aggregation** | [**UsageMeterAggregation**](UsageMeterAggregation.md) |  | [optional] 
**computations** | [**List[Computation]**](Computation.md) |  | [optional] 
**filters** | [**List[UsageMeterFilterEntry]**](UsageMeterFilterEntry.md) |  | [optional] 

## Example

```python
from togai_client.models.update_usage_meter_request import UpdateUsageMeterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUsageMeterRequest from a JSON string
update_usage_meter_request_instance = UpdateUsageMeterRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUsageMeterRequest.to_json())

# convert the object into a dict
update_usage_meter_request_dict = update_usage_meter_request_instance.to_dict()
# create an instance of UpdateUsageMeterRequest from a dict
update_usage_meter_request_from_dict = UpdateUsageMeterRequest.from_dict(update_usage_meter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


