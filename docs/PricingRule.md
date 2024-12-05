# PricingRule

Represents pricing rules of a price plan. i.e, price plan bound by time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**version** | **int** |  | 
**invoice_timing** | [**PricingRuleTiming**](PricingRuleTiming.md) |  | [optional] 
**order** | **int** |  | 
**condition** | **str** | JSON logic condition deciding whether to compute this pricing rule or not | [optional] 
**computation** | **str** | JSON logic to be computed | 
**action** | [**PricingRuleAction**](PricingRuleAction.md) |  | 

## Example

```python
from togai_client.models.pricing_rule import PricingRule

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRule from a JSON string
pricing_rule_instance = PricingRule.from_json(json)
# print the JSON string representation of the object
print(PricingRule.to_json())

# convert the object into a dict
pricing_rule_dict = pricing_rule_instance.to_dict()
# create an instance of PricingRule from a dict
pricing_rule_from_dict = PricingRule.from_dict(pricing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


