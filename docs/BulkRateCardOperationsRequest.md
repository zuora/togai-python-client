# BulkRateCardOperationsRequest

Bulk rate card operations for price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[RateCardOperation]**](RateCardOperation.md) |  | 

## Example

```python
from togai_client.models.bulk_rate_card_operations_request import BulkRateCardOperationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRateCardOperationsRequest from a JSON string
bulk_rate_card_operations_request_instance = BulkRateCardOperationsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkRateCardOperationsRequest.to_json())

# convert the object into a dict
bulk_rate_card_operations_request_dict = bulk_rate_card_operations_request_instance.to_dict()
# create an instance of BulkRateCardOperationsRequest from a dict
bulk_rate_card_operations_request_from_dict = BulkRateCardOperationsRequest.from_dict(bulk_rate_card_operations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


