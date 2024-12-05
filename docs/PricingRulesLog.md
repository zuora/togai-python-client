# PricingRulesLog

Pricing Rules Logs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**order** | **int** |  | 
**changes** | [**PricingRuleChangesLog**](PricingRuleChangesLog.md) |  | 
**rule** | [**PricingRuleInfo**](PricingRuleInfo.md) |  | [optional] 
**variables_value** | [**Dict[str, PricingRulesValues]**](PricingRulesValues.md) |  | [optional] 

## Example

```python
from togai_client.models.pricing_rules_log import PricingRulesLog

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRulesLog from a JSON string
pricing_rules_log_instance = PricingRulesLog.from_json(json)
# print the JSON string representation of the object
print(PricingRulesLog.to_json())

# convert the object into a dict
pricing_rules_log_dict = pricing_rules_log_instance.to_dict()
# create an instance of PricingRulesLog from a dict
pricing_rules_log_from_dict = PricingRulesLog.from_dict(pricing_rules_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


