# PricingRulesLogsPaginatedResponse

Pricing Rules Logs response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PricingRulesLog]**](PricingRulesLog.md) |  | 

## Example

```python
from togai_client.models.pricing_rules_logs_paginated_response import PricingRulesLogsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRulesLogsPaginatedResponse from a JSON string
pricing_rules_logs_paginated_response_instance = PricingRulesLogsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PricingRulesLogsPaginatedResponse.to_json())

# convert the object into a dict
pricing_rules_logs_paginated_response_dict = pricing_rules_logs_paginated_response_instance.to_dict()
# create an instance of PricingRulesLogsPaginatedResponse from a dict
pricing_rules_logs_paginated_response_from_dict = PricingRulesLogsPaginatedResponse.from_dict(pricing_rules_logs_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


