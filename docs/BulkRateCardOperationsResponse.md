# BulkRateCardOperationsResponse

Bulk rate card operations response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_cards** | [**List[RateCard]**](RateCard.md) |  | 

## Example

```python
from togai_client.models.bulk_rate_card_operations_response import BulkRateCardOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRateCardOperationsResponse from a JSON string
bulk_rate_card_operations_response_instance = BulkRateCardOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkRateCardOperationsResponse.to_json())

# convert the object into a dict
bulk_rate_card_operations_response_dict = bulk_rate_card_operations_response_instance.to_dict()
# create an instance of BulkRateCardOperationsResponse from a dict
bulk_rate_card_operations_response_from_dict = BulkRateCardOperationsResponse.from_dict(bulk_rate_card_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


