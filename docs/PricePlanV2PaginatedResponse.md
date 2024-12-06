# PricePlanV2PaginatedResponse

Paginated response for price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PricePlanV2]**](PricePlanV2.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.price_plan_v2_paginated_response import PricePlanV2PaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanV2PaginatedResponse from a JSON string
price_plan_v2_paginated_response_instance = PricePlanV2PaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PricePlanV2PaginatedResponse.to_json())

# convert the object into a dict
price_plan_v2_paginated_response_dict = price_plan_v2_paginated_response_instance.to_dict()
# create an instance of PricePlanV2PaginatedResponse from a dict
price_plan_v2_paginated_response_from_dict = PricePlanV2PaginatedResponse.from_dict(price_plan_v2_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


