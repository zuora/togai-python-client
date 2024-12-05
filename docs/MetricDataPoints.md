# MetricDataPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grouped_by** | [**MetricDataPointsGroupedBy**](MetricDataPointsGroupedBy.md) |  | [optional] 
**timestamps** | **List[datetime]** |  | 
**metric_values** | **List[float]** |  | 

## Example

```python
from togai_client.models.metric_data_points import MetricDataPoints

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDataPoints from a JSON string
metric_data_points_instance = MetricDataPoints.from_json(json)
# print the JSON string representation of the object
print(MetricDataPoints.to_json())

# convert the object into a dict
metric_data_points_dict = metric_data_points_instance.to_dict()
# create an instance of MetricDataPoints from a dict
metric_data_points_from_dict = MetricDataPoints.from_dict(metric_data_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


