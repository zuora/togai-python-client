# CurrencyRateValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**rate** | **float** |  | 

## Example

```python
from togai_client.models.currency_rate_value import CurrencyRateValue

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyRateValue from a JSON string
currency_rate_value_instance = CurrencyRateValue.from_json(json)
# print the JSON string representation of the object
print(CurrencyRateValue.to_json())

# convert the object into a dict
currency_rate_value_dict = currency_rate_value_instance.to_dict()
# create an instance of CurrencyRateValue from a dict
currency_rate_value_from_dict = CurrencyRateValue.from_dict(currency_rate_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


