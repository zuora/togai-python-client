# FinalizePricePlanRequest

Request to finalize a price plan version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_mode** | [**MigrationMode**](MigrationMode.md) |  | [optional] 
**versions_to_migrate** | [**VersionsToMigrate**](VersionsToMigrate.md) |  | [optional] 

## Example

```python
from togai_client.models.finalize_price_plan_request import FinalizePricePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FinalizePricePlanRequest from a JSON string
finalize_price_plan_request_instance = FinalizePricePlanRequest.from_json(json)
# print the JSON string representation of the object
print(FinalizePricePlanRequest.to_json())

# convert the object into a dict
finalize_price_plan_request_dict = finalize_price_plan_request_instance.to_dict()
# create an instance of FinalizePricePlanRequest from a dict
finalize_price_plan_request_from_dict = FinalizePricePlanRequest.from_dict(finalize_price_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


