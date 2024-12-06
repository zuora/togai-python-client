# LicenseRateCardConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_quantity** | **int** | Max allowed quantity for a particular license in a price plan | [optional] 
**max_quantity_breach_action** | [**MaxQuantityBreachAction**](MaxQuantityBreachAction.md) |  | [optional] 

## Example

```python
from togai_client.models.license_rate_card_config import LicenseRateCardConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRateCardConfig from a JSON string
license_rate_card_config_instance = LicenseRateCardConfig.from_json(json)
# print the JSON string representation of the object
print(LicenseRateCardConfig.to_json())

# convert the object into a dict
license_rate_card_config_dict = license_rate_card_config_instance.to_dict()
# create an instance of LicenseRateCardConfig from a dict
license_rate_card_config_from_dict = LicenseRateCardConfig.from_dict(license_rate_card_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


