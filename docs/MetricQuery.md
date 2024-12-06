# MetricQuery

Object representing a single metrics query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Mandatory  for all request.  User defined ID for identifying the request for your internal reference  | 
**name** | [**MetricName**](MetricName.md) |  | [default to MetricName.EVENTS]
**aggregation_period** | **str** | Set the aggregation period. Allowed periods are HOUR, DAY, WEEK, MONTH | [default to 'DAY']
**group_by** | **str** | Group your metric with a groupBy field.  Allowed fields are  ACCOUNT_ID EVENT_STATUS  SCHEMA_NAME  USAGE_METER_ID [Use BILLABLE_ID as this will be deprecated soon...] BILLABLE_ID RAW_EVENT_STATUS Please refer the table above for the list of combinations allowed in the groupBy  | [optional] 
**configs** | **Dict[str, str]** | Configurations. | Metric Name       | Config Key | Allowed Values  | Default value |              Description          | |-------------------|------------|-----------------|---------------|-----------------------------------| | REVENUE           | CURRENCY   | BASE or INVOICE | BASE          | currency to return the revenue in | | REVENUE_FOR_CYCLE | CURRENCY   | BASE or INVOICE | BASE          | currency to return the revenue in |  | [optional] 
**filters** | [**List[MetricQueryFilterEntry]**](MetricQueryFilterEntry.md) | Filter on specific fields.  Refer possible fieldNames and fieldValues from the table above.  | [optional] 

## Example

```python
from togai_client.models.metric_query import MetricQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricQuery from a JSON string
metric_query_instance = MetricQuery.from_json(json)
# print the JSON string representation of the object
print(MetricQuery.to_json())

# convert the object into a dict
metric_query_dict = metric_query_instance.to_dict()
# create an instance of MetricQuery from a dict
metric_query_from_dict = MetricQuery.from_dict(metric_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


