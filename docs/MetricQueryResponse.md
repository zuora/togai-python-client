# MetricQueryResponse

Response to GetMetrics Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | [**MetricName**](MetricName.md) |  | [default to MetricName.EVENTS]
**data** | [**List[MetricDataPoints]**](MetricDataPoints.md) |  | 

## Example

```python
from togai_client.models.metric_query_response import MetricQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetricQueryResponse from a JSON string
metric_query_response_instance = MetricQueryResponse.from_json(json)
# print the JSON string representation of the object
print(MetricQueryResponse.to_json())

# convert the object into a dict
metric_query_response_dict = metric_query_response_instance.to_dict()
# create an instance of MetricQueryResponse from a dict
metric_query_response_from_dict = MetricQueryResponse.from_dict(metric_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


