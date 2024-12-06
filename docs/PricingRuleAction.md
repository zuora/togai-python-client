# PricingRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**target** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.pricing_rule_action import PricingRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRuleAction from a JSON string
pricing_rule_action_instance = PricingRuleAction.from_json(json)
# print the JSON string representation of the object
print(PricingRuleAction.to_json())

# convert the object into a dict
pricing_rule_action_dict = pricing_rule_action_instance.to_dict()
# create an instance of PricingRuleAction from a dict
pricing_rule_action_from_dict = PricingRuleAction.from_dict(pricing_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


