# CurrencySlabRateDetail

The association of a currency along with its slab detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**credit_amount** | **float** | The amount of credit that needs to be credited | 
**slab_details** | [**List[SlabDetail]**](SlabDetail.md) |  | 
**rate_config** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.currency_slab_rate_detail import CurrencySlabRateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencySlabRateDetail from a JSON string
currency_slab_rate_detail_instance = CurrencySlabRateDetail.from_json(json)
# print the JSON string representation of the object
print(CurrencySlabRateDetail.to_json())

# convert the object into a dict
currency_slab_rate_detail_dict = currency_slab_rate_detail_instance.to_dict()
# create an instance of CurrencySlabRateDetail from a dict
currency_slab_rate_detail_from_dict = CurrencySlabRateDetail.from_dict(currency_slab_rate_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


