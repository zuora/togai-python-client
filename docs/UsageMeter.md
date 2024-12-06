# UsageMeter

Structure of usage meter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the usage meter | 
**name** | **str** | Name of the usage meter | 
**billable_name** | **str** | Billable name of addon. Billable name takes precedence over name to display in invoice. | [optional] 
**display_name** | **str** | Display name of usage meter. This is an auto-generated field which contains billableName of usage meter. If billableName is not provided, name will be used as display name.  | 
**description** | **str** |  | [optional] 
**filters** | [**List[UsageMeterFilterEntry]**](UsageMeterFilterEntry.md) |  | [optional] 
**type** | **str** | Type of usage meter | 
**status** | **str** | Status of usage meter | [optional] 
**aggregation** | [**UsageMeterAggregation**](UsageMeterAggregation.md) |  | 
**computations** | [**List[Computation]**](Computation.md) |  | [optional] 
**event_schema** | [**EventSchema**](EventSchema.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_activated_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from togai_client.models.usage_meter import UsageMeter

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeter from a JSON string
usage_meter_instance = UsageMeter.from_json(json)
# print the JSON string representation of the object
print(UsageMeter.to_json())

# convert the object into a dict
usage_meter_dict = usage_meter_instance.to_dict()
# create an instance of UsageMeter from a dict
usage_meter_from_dict = UsageMeter.from_dict(usage_meter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


