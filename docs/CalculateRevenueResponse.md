# CalculateRevenueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**usage_lookup_range** | [**UsageLookupRange**](UsageLookupRange.md) |  | [optional] 
**price_plan_details** | [**PricePlanDetails**](PricePlanDetails.md) |  | 
**revenue_info** | [**List[RevenueInfo]**](RevenueInfo.md) |  | 

## Example

```python
from togai_client.models.calculate_revenue_response import CalculateRevenueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateRevenueResponse from a JSON string
calculate_revenue_response_instance = CalculateRevenueResponse.from_json(json)
# print the JSON string representation of the object
print(CalculateRevenueResponse.to_json())

# convert the object into a dict
calculate_revenue_response_dict = calculate_revenue_response_instance.to_dict()
# create an instance of CalculateRevenueResponse from a dict
calculate_revenue_response_from_dict = CalculateRevenueResponse.from_dict(calculate_revenue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


