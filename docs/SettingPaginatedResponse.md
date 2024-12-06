# SettingPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Setting]**](Setting.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.setting_paginated_response import SettingPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingPaginatedResponse from a JSON string
setting_paginated_response_instance = SettingPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SettingPaginatedResponse.to_json())

# convert the object into a dict
setting_paginated_response_dict = setting_paginated_response_instance.to_dict()
# create an instance of SettingPaginatedResponse from a dict
setting_paginated_response_from_dict = SettingPaginatedResponse.from_dict(setting_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


