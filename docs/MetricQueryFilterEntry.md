# MetricQueryFilterEntry

 | Metric Name       | FilterEntry Name |    Allowed groupBy fields                                           |      Default Values      |                 Allowed Values                                  | |-------------------|------------------|---------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------| | EVENTS            | ACCOUNT_ID       | ACCOUNT_ID, EVENT_STATUS, SCHEMA_NAME, RAW_EVENT_STATUS             | None                     | *\\<one or more valid account IDs>                               | | EVENTS            | CUSTOMER_ID      | ACCOUNT_ID, EVENT_STATUS, SCHEMA_NAME, RAW_EVENT_STATUS             | None                     | *\\<one or more valid customer IDs>                              | | EVENTS            | SCHEMA_NAME      | ACCOUNT_ID, EVENT_STATUS, SCHEMA_NAME, RAW_EVENT_STATUS             | None                     | *\\<at most one valid schema names>                              | | EVENTS            | EVENT_STATUS     | ACCOUNT_ID, EVENT_STATUS, SCHEMA_NAME, RAW_EVENT_STATUS             | [PROCESSED, UNPROCESSED] | oneOrMoreOf PROCESSED, UNPROCESSED, IN_PROGRESS, IngestionStatus|       | USAGE             | ACCOUNT_ID       | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid account IDs>                               | | USAGE             | CUSTOMER_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid customer IDs>                              | | USAGE             | USAGE_METER_ID   | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | USAGE             | BILLABLE_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | REVENUE           | ACCOUNT_ID       | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid account IDs>                               | | REVENUE           | CUSTOMER_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid customer IDs>                              | | REVENUE           | USAGE_METER_ID   | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | REVENUE           | BILLABLE_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | EVENTS            | ORGANIZATION_ID  | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | <From auth token>        |                                                                 | | USAGE             | ORGANIZATION_ID  | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | <From auth token>        |                                                                 | | REVENUE           | ORGANIZATION_ID  | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | <From auth token>        |                                                                 | | USAGE_FOR_CYCLE   | ACCOUNT_ID       | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid account IDs>                               | | USAGE_FOR_CYCLE   | CUSTOMER_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid customer IDs>                              | | USAGE_FOR_CYCLE   | USAGE_METER_ID   | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | USAGE_FOR_CYCLE   | BILLABLE_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | REVENUE_FOR_CYCLE | ACCOUNT_ID       | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid account IDs>                               | | REVENUE_FOR_CYCLE | CUSTOMER_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid customer IDs>                              | | REVENUE_FOR_CYCLE | USAGE_METER_ID   | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | | REVENUE_FOR_CYCLE | BILLABLE_ID      | ACCOUNT_ID, USAGE_METER_ID, BILLABLE_ID CUSTOMER_ID                 | None                     | *\\<one or more valid usage meter name>                          | 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**field_values** | **List[str]** |  | 

## Example

```python
from togai_client.models.metric_query_filter_entry import MetricQueryFilterEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MetricQueryFilterEntry from a JSON string
metric_query_filter_entry_instance = MetricQueryFilterEntry.from_json(json)
# print the JSON string representation of the object
print(MetricQueryFilterEntry.to_json())

# convert the object into a dict
metric_query_filter_entry_dict = metric_query_filter_entry_instance.to_dict()
# create an instance of MetricQueryFilterEntry from a dict
metric_query_filter_entry_from_dict = MetricQueryFilterEntry.from_dict(metric_query_filter_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


