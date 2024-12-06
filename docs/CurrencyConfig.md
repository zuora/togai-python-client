# CurrencyConfig

Configuration for getting the currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode to get the currency - CUSTOM: Use the currency provided in the request - ACCOUNT_INVOICE: Use the invoice currency of the given account  | 
**currency** | **str** | Currency to be used, this will be considered if mode is CUSTOM | [optional] 
**account_id** | **str** | Id of the account of which invoice currency will be used, this will be considered if mode is ACCOUNT_INVOICE | [optional] 

## Example

```python
from togai_client.models.currency_config import CurrencyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConfig from a JSON string
currency_config_instance = CurrencyConfig.from_json(json)
# print the JSON string representation of the object
print(CurrencyConfig.to_json())

# convert the object into a dict
currency_config_dict = currency_config_instance.to_dict()
# create an instance of CurrencyConfig from a dict
currency_config_from_dict = CurrencyConfig.from_dict(currency_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


