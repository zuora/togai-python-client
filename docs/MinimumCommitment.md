# MinimumCommitment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**rate_values** | [**List[CurrencyRateValue]**](CurrencyRateValue.md) |  | 

## Example

```python
from togai_client.models.minimum_commitment import MinimumCommitment

# TODO update the JSON string below
json = "{}"
# create an instance of MinimumCommitment from a JSON string
minimum_commitment_instance = MinimumCommitment.from_json(json)
# print the JSON string representation of the object
print(MinimumCommitment.to_json())

# convert the object into a dict
minimum_commitment_dict = minimum_commitment_instance.to_dict()
# create an instance of MinimumCommitment from a dict
minimum_commitment_from_dict = MinimumCommitment.from_dict(minimum_commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


