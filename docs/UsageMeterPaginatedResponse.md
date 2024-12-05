# UsageMeterPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsageMeter]**](UsageMeter.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.usage_meter_paginated_response import UsageMeterPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeterPaginatedResponse from a JSON string
usage_meter_paginated_response_instance = UsageMeterPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(UsageMeterPaginatedResponse.to_json())

# convert the object into a dict
usage_meter_paginated_response_dict = usage_meter_paginated_response_instance.to_dict()
# create an instance of UsageMeterPaginatedResponse from a dict
usage_meter_paginated_response_from_dict = UsageMeterPaginatedResponse.from_dict(usage_meter_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


