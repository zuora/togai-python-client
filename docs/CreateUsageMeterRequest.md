# CreateUsageMeterRequest

Request to create usage meter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the usage meter. Must be unique for an organization. | 
**billable_name** | **str** | Billable name of usage meter. Billable name takes precedence over name to display in invoice. | [optional] 
**description** | **str** | Description of the usage meter | [optional] 
**filters** | [**List[UsageMeterFilterEntry]**](UsageMeterFilterEntry.md) | The usage meter&#39;s applicability will be determined by comparing the filter condition agianst the events. | [optional] 
**type** | **str** | Type of usage meter | 
**aggregation** | [**UsageMeterAggregation**](UsageMeterAggregation.md) |  | 
**computations** | [**List[Computation]**](Computation.md) |  | [optional] 
**event_schema_name** | **str** | Event Schema Identifier | [optional] 

## Example

```python
from togai_client.models.create_usage_meter_request import CreateUsageMeterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsageMeterRequest from a JSON string
create_usage_meter_request_instance = CreateUsageMeterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUsageMeterRequest.to_json())

# convert the object into a dict
create_usage_meter_request_dict = create_usage_meter_request_instance.to_dict()
# create an instance of CreateUsageMeterRequest from a dict
create_usage_meter_request_from_dict = CreateUsageMeterRequest.from_dict(create_usage_meter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


