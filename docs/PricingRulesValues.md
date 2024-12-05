# PricingRulesValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from togai_client.models.pricing_rules_values import PricingRulesValues

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRulesValues from a JSON string
pricing_rules_values_instance = PricingRulesValues.from_json(json)
# print the JSON string representation of the object
print(PricingRulesValues.to_json())

# convert the object into a dict
pricing_rules_values_dict = pricing_rules_values_instance.to_dict()
# create an instance of PricingRulesValues from a dict
pricing_rules_values_from_dict = PricingRulesValues.from_dict(pricing_rules_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


