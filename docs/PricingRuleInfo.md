# PricingRuleInfo

Pricing Rule Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**condition** | **str** |  | [optional] 
**computation** | **str** |  | [optional] 

## Example

```python
from togai_client.models.pricing_rule_info import PricingRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRuleInfo from a JSON string
pricing_rule_info_instance = PricingRuleInfo.from_json(json)
# print the JSON string representation of the object
print(PricingRuleInfo.to_json())

# convert the object into a dict
pricing_rule_info_dict = pricing_rule_info_instance.to_dict()
# create an instance of PricingRuleInfo from a dict
pricing_rule_info_from_dict = PricingRuleInfo.from_dict(pricing_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


