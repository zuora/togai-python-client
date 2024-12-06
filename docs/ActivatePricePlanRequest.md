# ActivatePricePlanRequest

Request to activate currencies of a price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | **List[str]** | List of currencies to activate | 

## Example

```python
from togai_client.models.activate_price_plan_request import ActivatePricePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivatePricePlanRequest from a JSON string
activate_price_plan_request_instance = ActivatePricePlanRequest.from_json(json)
# print the JSON string representation of the object
print(ActivatePricePlanRequest.to_json())

# convert the object into a dict
activate_price_plan_request_dict = activate_price_plan_request_instance.to_dict()
# create an instance of ActivatePricePlanRequest from a dict
activate_price_plan_request_from_dict = ActivatePricePlanRequest.from_dict(activate_price_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


