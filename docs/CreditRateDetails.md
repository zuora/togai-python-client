# CreditRateDetails

Amount to be credited

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_model** | [**PricingModel**](PricingModel.md) |  | 
**currency_slab_rate_details** | [**List[CurrencySlabRateDetail]**](CurrencySlabRateDetail.md) |  | 

## Example

```python
from togai_client.models.credit_rate_details import CreditRateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreditRateDetails from a JSON string
credit_rate_details_instance = CreditRateDetails.from_json(json)
# print the JSON string representation of the object
print(CreditRateDetails.to_json())

# convert the object into a dict
credit_rate_details_dict = credit_rate_details_instance.to_dict()
# create an instance of CreditRateDetails from a dict
credit_rate_details_from_dict = CreditRateDetails.from_dict(credit_rate_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


