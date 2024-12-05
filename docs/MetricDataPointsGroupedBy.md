# MetricDataPointsGroupedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**field_value** | **str** |  | 

## Example

```python
from togai_client.models.metric_data_points_grouped_by import MetricDataPointsGroupedBy

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDataPointsGroupedBy from a JSON string
metric_data_points_grouped_by_instance = MetricDataPointsGroupedBy.from_json(json)
# print the JSON string representation of the object
print(MetricDataPointsGroupedBy.to_json())

# convert the object into a dict
metric_data_points_grouped_by_dict = metric_data_points_grouped_by_instance.to_dict()
# create an instance of MetricDataPointsGroupedBy from a dict
metric_data_points_grouped_by_from_dict = MetricDataPointsGroupedBy.from_dict(metric_data_points_grouped_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


