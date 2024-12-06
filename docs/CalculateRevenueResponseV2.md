# CalculateRevenueResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**usage_lookup_range** | [**UsageLookupRange**](UsageLookupRange.md) |  | [optional] 
**revenue_info** | [**List[RevenueInfoV2]**](RevenueInfoV2.md) |  | 

## Example

```python
from togai_client.models.calculate_revenue_response_v2 import CalculateRevenueResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateRevenueResponseV2 from a JSON string
calculate_revenue_response_v2_instance = CalculateRevenueResponseV2.from_json(json)
# print the JSON string representation of the object
print(CalculateRevenueResponseV2.to_json())

# convert the object into a dict
calculate_revenue_response_v2_dict = calculate_revenue_response_v2_instance.to_dict()
# create an instance of CalculateRevenueResponseV2 from a dict
calculate_revenue_response_v2_from_dict = CalculateRevenueResponseV2.from_dict(calculate_revenue_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


