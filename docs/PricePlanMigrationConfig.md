# PricePlanMigrationConfig

Migrate all account associations of a price plan to another price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Id of source price plan | 
**source_version** | **int** | Version of the source price plan | 
**target_id** | **str** | Id of target price plan | [optional] 
**target_version** | **int** | Version of the target price plan | [optional] 
**migration_mode** | **str** |  | 
**retain_start_offsets** | **bool** | If this flag is true, current pricing cycle of the account on the date of association will continue rather  than the configurations of the newly associated price plan. Pricing cycle overrides specified  using  &#x60;pricePlanDetailsOverride&#x60; will take precedence over the pricing cycle configurations of  the new price plan that the account needs to migrate to. PricingCycleInterval of the existing plan and  the new plan must be same for this to work. We&#39;ll return a &#x60;400 BadRequest&#x60; otherwise. Examples:   - Ongoing plan (1st Oct to 30th Oct) - {dayOffset: 1, monthOffset: NIL}     New association (15th Oct to 15th Nov) of different price plan with retainStartOffsets option true      will use the same pricing cycle configuration {dayOffset: 1, monthOffset: NIL} rather than using the     pricing cycle configuration of the new price plan that the account needs to migrate to.   - Ongoing plan (1st Oct to 30th Oct) - {dayOffset: 1, monthOffset: NIL}     New association (1st Nov to 30th Nov) of different price plan with retainStartOffsets option true will     throw a &#x60;400 BadRequest&#x60; as no existing price plan configuration found on date of association  | [optional] 
**is_price_plan_v2_migration** | **bool** | If this flag is true, the migration will be done for price plan v2. Default value is false  | [optional] 

## Example

```python
from togai_client.models.price_plan_migration_config import PricePlanMigrationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanMigrationConfig from a JSON string
price_plan_migration_config_instance = PricePlanMigrationConfig.from_json(json)
# print the JSON string representation of the object
print(PricePlanMigrationConfig.to_json())

# convert the object into a dict
price_plan_migration_config_dict = price_plan_migration_config_instance.to_dict()
# create an instance of PricePlanMigrationConfig from a dict
price_plan_migration_config_from_dict = PricePlanMigrationConfig.from_dict(price_plan_migration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


