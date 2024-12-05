# CreatePricePlanMigrationRequest

Request to create price plan migration request

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
**require_confirmation** | **bool** | This field specifies whether to process job or to wait till the job is confirmed. Default value: false  | [optional] 

## Example

```python
from togai_client.models.create_price_plan_migration_request import CreatePricePlanMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePricePlanMigrationRequest from a JSON string
create_price_plan_migration_request_instance = CreatePricePlanMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePricePlanMigrationRequest.to_json())

# convert the object into a dict
create_price_plan_migration_request_dict = create_price_plan_migration_request_instance.to_dict()
# create an instance of CreatePricePlanMigrationRequest from a dict
create_price_plan_migration_request_from_dict = CreatePricePlanMigrationRequest.from_dict(create_price_plan_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


