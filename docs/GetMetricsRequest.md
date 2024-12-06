# GetMetricsRequest

Request to get metrics from togai

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | Start date time of the query (inclusive) | 
**end_time** | **datetime** | End date time of the query (exclusive) | 
**metric_queries** | [**List[MetricQuery]**](MetricQuery.md) |  | 

## Example

```python
from togai_client.models.get_metrics_request import GetMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsRequest from a JSON string
get_metrics_request_instance = GetMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMetricsRequest.to_json())

# convert the object into a dict
get_metrics_request_dict = get_metrics_request_instance.to_dict()
# create an instance of GetMetricsRequest from a dict
get_metrics_request_from_dict = GetMetricsRequest.from_dict(get_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


