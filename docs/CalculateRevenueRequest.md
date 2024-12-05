# CalculateRevenueRequest

Request to get revenue details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_config** | [**CurrencyConfig**](CurrencyConfig.md) |  | 
**price_plan_details_config** | [**PricePlanDetailsConfig**](PricePlanDetailsConfig.md) |  | 
**usage_config** | [**UsageConfig**](UsageConfig.md) |  | 
**license_entries_config** | [**LicenseEntriesConfig**](LicenseEntriesConfig.md) |  | 
**named_license_entries_config** | [**NamedLicenseEntriesConfig**](NamedLicenseEntriesConfig.md) |  | [optional] 
**proration_config** | [**ProrationConfig**](ProrationConfig.md) |  | [optional] 
**entitlement_overage_config** | [**EntitlementOverageConfig**](EntitlementOverageConfig.md) |  | [optional] 

## Example

```python
from togai_client.models.calculate_revenue_request import CalculateRevenueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateRevenueRequest from a JSON string
calculate_revenue_request_instance = CalculateRevenueRequest.from_json(json)
# print the JSON string representation of the object
print(CalculateRevenueRequest.to_json())

# convert the object into a dict
calculate_revenue_request_dict = calculate_revenue_request_instance.to_dict()
# create an instance of CalculateRevenueRequest from a dict
calculate_revenue_request_from_dict = CalculateRevenueRequest.from_dict(calculate_revenue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


