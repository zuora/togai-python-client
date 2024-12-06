# CreatePricingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the pricing rule | 
**order** | **int** | Order of the pricing rule | 
**invoice_timing** | [**PricingRuleTiming**](PricingRuleTiming.md) |  | [optional] 
**condition** | **str** | JSON logic condition deciding whether to compute this pricing rule or not | [optional] 
**computation** | **str** | JSON logic to be computed | 
**action** | [**PricingRuleAction**](PricingRuleAction.md) |  | 

## Example

```python
from togai_client.models.create_pricing_rule import CreatePricingRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePricingRule from a JSON string
create_pricing_rule_instance = CreatePricingRule.from_json(json)
# print the JSON string representation of the object
print(CreatePricingRule.to_json())

# convert the object into a dict
create_pricing_rule_dict = create_pricing_rule_instance.to_dict()
# create an instance of CreatePricingRule from a dict
create_pricing_rule_from_dict = CreatePricingRule.from_dict(create_pricing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


