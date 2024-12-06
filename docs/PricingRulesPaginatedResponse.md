# PricingRulesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PricingRule]**](PricingRule.md) |  | 

## Example

```python
from togai_client.models.pricing_rules_paginated_response import PricingRulesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRulesPaginatedResponse from a JSON string
pricing_rules_paginated_response_instance = PricingRulesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PricingRulesPaginatedResponse.to_json())

# convert the object into a dict
pricing_rules_paginated_response_dict = pricing_rules_paginated_response_instance.to_dict()
# create an instance of PricingRulesPaginatedResponse from a dict
pricing_rules_paginated_response_from_dict = PricingRulesPaginatedResponse.from_dict(pricing_rules_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


