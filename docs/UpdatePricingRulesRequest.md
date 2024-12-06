# UpdatePricingRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_rules** | [**List[CreatePricingRule]**](CreatePricingRule.md) |  | [optional] 

## Example

```python
from togai_client.models.update_pricing_rules_request import UpdatePricingRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricingRulesRequest from a JSON string
update_pricing_rules_request_instance = UpdatePricingRulesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePricingRulesRequest.to_json())

# convert the object into a dict
update_pricing_rules_request_dict = update_pricing_rules_request_instance.to_dict()
# create an instance of UpdatePricingRulesRequest from a dict
update_pricing_rules_request_from_dict = UpdatePricingRulesRequest.from_dict(update_pricing_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


