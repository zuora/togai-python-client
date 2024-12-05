# RateCardOperation

Rate card operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Operation type | 
**rate_card_name** | **str** | Required for UPDATE and DELETE operations | 
**rate_card** | [**RateCardData**](RateCardData.md) |  | [optional] 

## Example

```python
from togai_client.models.rate_card_operation import RateCardOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardOperation from a JSON string
rate_card_operation_instance = RateCardOperation.from_json(json)
# print the JSON string representation of the object
print(RateCardOperation.to_json())

# convert the object into a dict
rate_card_operation_dict = rate_card_operation_instance.to_dict()
# create an instance of RateCardOperation from a dict
rate_card_operation_from_dict = RateCardOperation.from_dict(rate_card_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


