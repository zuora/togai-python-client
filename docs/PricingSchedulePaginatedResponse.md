# PricingSchedulePaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PricingScheduleWithPricePlanId]**](PricingScheduleWithPricePlanId.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**previous_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.pricing_schedule_paginated_response import PricingSchedulePaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingSchedulePaginatedResponse from a JSON string
pricing_schedule_paginated_response_instance = PricingSchedulePaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PricingSchedulePaginatedResponse.to_json())

# convert the object into a dict
pricing_schedule_paginated_response_dict = pricing_schedule_paginated_response_instance.to_dict()
# create an instance of PricingSchedulePaginatedResponse from a dict
pricing_schedule_paginated_response_from_dict = PricingSchedulePaginatedResponse.from_dict(pricing_schedule_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


