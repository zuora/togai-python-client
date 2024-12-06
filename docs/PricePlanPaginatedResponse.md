# PricePlanPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PricePlanListData]**](PricePlanListData.md) |  | 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.price_plan_paginated_response import PricePlanPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanPaginatedResponse from a JSON string
price_plan_paginated_response_instance = PricePlanPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PricePlanPaginatedResponse.to_json())

# convert the object into a dict
price_plan_paginated_response_dict = price_plan_paginated_response_instance.to_dict()
# create an instance of PricePlanPaginatedResponse from a dict
price_plan_paginated_response_from_dict = PricePlanPaginatedResponse.from_dict(price_plan_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


