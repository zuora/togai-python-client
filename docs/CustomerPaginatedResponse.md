# CustomerPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Customer]**](Customer.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.customer_paginated_response import CustomerPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPaginatedResponse from a JSON string
customer_paginated_response_instance = CustomerPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerPaginatedResponse.to_json())

# convert the object into a dict
customer_paginated_response_dict = customer_paginated_response_instance.to_dict()
# create an instance of CustomerPaginatedResponse from a dict
customer_paginated_response_from_dict = CustomerPaginatedResponse.from_dict(customer_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


