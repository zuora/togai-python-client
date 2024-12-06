# AlertsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Alert]**](Alert.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.alerts_paginated_response import AlertsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsPaginatedResponse from a JSON string
alerts_paginated_response_instance = AlertsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AlertsPaginatedResponse.to_json())

# convert the object into a dict
alerts_paginated_response_dict = alerts_paginated_response_instance.to_dict()
# create an instance of AlertsPaginatedResponse from a dict
alerts_paginated_response_from_dict = AlertsPaginatedResponse.from_dict(alerts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


