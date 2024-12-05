# BillingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | Represents the number of pricing cycles after which the rate card will be billed | [optional] 
**start_offset** | **int** | Represents the offset for pricing cycles after which the rate card will be billed | [optional] 

## Example

```python
from togai_client.models.billing_config import BillingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BillingConfig from a JSON string
billing_config_instance = BillingConfig.from_json(json)
# print the JSON string representation of the object
print(BillingConfig.to_json())

# convert the object into a dict
billing_config_dict = billing_config_instance.to_dict()
# create an instance of BillingConfig from a dict
billing_config_from_dict = BillingConfig.from_dict(billing_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


