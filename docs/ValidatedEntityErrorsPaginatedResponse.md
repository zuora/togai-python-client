# ValidatedEntityErrorsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ValidatedEntityError]**](ValidatedEntityError.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.validated_entity_errors_paginated_response import ValidatedEntityErrorsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedEntityErrorsPaginatedResponse from a JSON string
validated_entity_errors_paginated_response_instance = ValidatedEntityErrorsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(ValidatedEntityErrorsPaginatedResponse.to_json())

# convert the object into a dict
validated_entity_errors_paginated_response_dict = validated_entity_errors_paginated_response_instance.to_dict()
# create an instance of ValidatedEntityErrorsPaginatedResponse from a dict
validated_entity_errors_paginated_response_from_dict = ValidatedEntityErrorsPaginatedResponse.from_dict(validated_entity_errors_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


