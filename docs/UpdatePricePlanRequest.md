# UpdatePricePlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_mode** | [**MigrationMode**](MigrationMode.md) |  | [optional] 
**versions_to_migrate** | [**VersionsToMigrate**](VersionsToMigrate.md) |  | [optional] 
**description** | **str** | Description of price plan | [optional] 
**price_plan_details** | [**CreatePricePlanDetailsOverride**](CreatePricePlanDetailsOverride.md) |  | [optional] 
**pricing_rules** | [**List[CreatePricingRule]**](CreatePricingRule.md) |  | [optional] 

## Example

```python
from togai_client.models.update_price_plan_request import UpdatePricePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricePlanRequest from a JSON string
update_price_plan_request_instance = UpdatePricePlanRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePricePlanRequest.to_json())

# convert the object into a dict
update_price_plan_request_dict = update_price_plan_request_instance.to_dict()
# create an instance of UpdatePricePlanRequest from a dict
update_price_plan_request_from_dict = UpdatePricePlanRequest.from_dict(update_price_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


