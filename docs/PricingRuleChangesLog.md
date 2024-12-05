# PricingRuleChangesLog

Pricing Rules Logs Changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**key_name** | **str** |  | [optional] 
**old_revenue** | **float** |  | 
**new_revenue** | **float** |  | 
**old_usage** | **float** |  | [optional] 
**new_usage** | **float** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from togai_client.models.pricing_rule_changes_log import PricingRuleChangesLog

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRuleChangesLog from a JSON string
pricing_rule_changes_log_instance = PricingRuleChangesLog.from_json(json)
# print the JSON string representation of the object
print(PricingRuleChangesLog.to_json())

# convert the object into a dict
pricing_rule_changes_log_dict = pricing_rule_changes_log_instance.to_dict()
# create an instance of PricingRuleChangesLog from a dict
pricing_rule_changes_log_from_dict = PricingRuleChangesLog.from_dict(pricing_rule_changes_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


